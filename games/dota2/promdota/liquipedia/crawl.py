"""Incremental category and tab-subpage wikitext collection."""

import re
from dataclasses import dataclass
from datetime import UTC, datetime

from promdota.liquipedia import cache

CATEGORY = "Category:Tournaments"
BATCH = 50


def utc_now():
    return datetime.now(UTC)


@dataclass
class Summary:
    listed: int = 0
    new: int = 0
    changed: int = 0
    unchanged: int = 0
    subpages: int = 0
    match_pages: int = 0
    missing: int = 0
    fetched: int = 0


def list_category(fetcher, category) -> list[str]:
    titles, continuation = [], {}
    while True:
        result = fetcher.query(
            action="query",
            list="categorymembers",
            cmtitle=category,
            cmlimit=500,
            cmprop="title",
            cmnamespace=0,
            **continuation,
        )
        titles.extend(page["title"] for page in result["query"]["categorymembers"])
        if "cmcontinue" not in result.get("continue", {}):
            return titles
        continuation = result["continue"]


def _pages(fetcher, titles, content=False):
    for offset in range(0, len(titles), BATCH):
        batch = titles[offset : offset + BATCH]
        params = {
            "action": "query",
            "prop": "revisions",
            "titles": "|".join(batch),
            "rvprop": "ids|timestamp|content" if content else "ids|timestamp",
        }
        if content:
            params["rvslots"] = "main"
        query = fetcher.query(**params)["query"]
        normalized = {item["from"]: item["to"] for item in query.get("normalized", [])}
        pages = {page["title"]: page for page in query["pages"].values()}
        for title in batch:
            page = pages.get(normalized.get(title, title))
            if page is not None and "missing" not in page and page.get("revisions"):
                yield title, page, page["revisions"][0]


def revisions(fetcher, titles) -> dict[str, tuple[int, int, str]]:
    return {
        title: (page["pageid"], revision["revid"], revision["timestamp"])
        for title, page, revision in _pages(fetcher, titles)
    }


def contents(fetcher, titles) -> list[dict]:
    records = []
    for title, page, revision in _pages(fetcher, titles, content=True):
        slot = revision["slots"]["main"]
        records.append(
            {
                "title": title,
                "pageid": page["pageid"],
                "revid": revision["revid"],
                "timestamp": revision["timestamp"],
                "wikitext": slot["*"] if "*" in slot else slot["content"],
            }
        )
    return records


def clean_title(title):
    """Drop a #fragment and collapse spacing, as MediaWiki resolves the link."""
    return re.sub(r"\s+", " ", title.split("#")[0].replace("_", " ")).strip()


def list_subpages(fetcher, roots) -> dict[str, str]:
    """Every non-redirect article under a tournament root → its nearest root."""
    roots, found, continuation = set(roots), {}, {}
    while True:
        result = fetcher.query(
            action="query",
            list="allpages",
            apnamespace=0,
            aplimit=500,
            apfilterredir="nonredirects",
            **continuation,
        )
        for page in result["query"]["allpages"]:
            parts = page["title"].split("/")
            for cut in range(len(parts) - 1, 0, -1):
                if "/".join(parts[:cut]) in roots:
                    found[page["title"]] = "/".join(parts[:cut])
                    break
        if "apcontinue" not in result.get("continue", {}):
            return found
        continuation = result["continue"]


def subpage_links(title, wikitext) -> set[str]:
    title = clean_title(title)
    root = title.split("/")[0]
    links = {
        clean_title(match)
        for match in re.findall(r"\|\s*link\d+\s*=\s*([^|}\n]+)", wikitext)
    }
    return {
        link
        for link in links
        if link != title and (link == root or link.startswith(root + "/"))
    }


def crawl(fetcher, limit=None, full=False, now=utc_now, no_matches=False) -> Summary:
    if limit is not None and limit < 0:
        raise ValueError("limit must be nonnegative")
    titles = list(dict.fromkeys(list_category(fetcher, CATEGORY)))
    cache.save_category(CATEGORY, titles)
    index = cache.load_index()
    summary = Summary(listed=len(titles))
    sources = dict.fromkeys(titles, ("category", None))
    sources.update(
        {
            title: ("subpage", entry["parent"])
            for title, entry in index.items()
            if entry["source"] == "subpage" and title not in sources
        }
    )
    # Dota tabs live in per-series templates, so links alone miss stage pages.
    for title, parent in list_subpages(fetcher, titles).items():
        sources.setdefault(title, ("subpage", parent))
    checked, missing = set(), set()
    attempted = 0

    def refresh(candidates, current=None):
        nonlocal attempted
        candidates = [title for title in candidates if title not in checked]
        checked.update(candidates)
        current = revisions(fetcher, candidates) if current is None else current
        missing.update(set(candidates) - current.keys())
        todo = []
        for title, (_, revid, _) in current.items():
            if title not in index or index[title]["revid"] != revid or full:
                todo.append(title)
            else:
                summary.unchanged += 1
        if limit is not None:
            todo = todo[: max(0, limit - attempted)]
        for offset in range(0, len(todo), BATCH):
            batch = todo[offset : offset + BATCH]
            attempted += len(batch)
            records = contents(fetcher, batch)
            missing.update(set(batch) - {record["title"] for record in records})
            for record in records:
                title = record["title"]
                if title not in index:
                    summary.new += 1
                elif index[title]["revid"] != record["revid"]:
                    summary.changed += 1
                record["fetched_at"] = (
                    now().astimezone(UTC).isoformat().replace("+00:00", "Z")
                )
                cache.save_page(record)
                source, parent = sources[title]
                index[title] = {
                    "revid": record["revid"],
                    "file": cache.page_file(title).as_posix(),
                    "source": source,
                    "parent": parent,
                }
                summary.fetched += 1
            cache.save_index(index)

    refresh(list(sources))
    for _ in range(3):
        discovered = []
        for title in sorted(index):
            record = cache.read_page(title)
            if record is None:
                continue
            for link in sorted(subpage_links(title, record["wikitext"])):
                if link not in sources:
                    sources[link] = ("subpage", title)
                    discovered.append(link)
        if not discovered:
            break
        refresh(discovered)
    if not no_matches:
        match_revisions, continuation = {}, {}
        while True:
            result = fetcher.query(
                action="query",
                generator="allpages",
                gapnamespace=130,
                gaplimit=500,
                prop="info",
                **continuation,
            )
            for page in result.get("query", {}).get("pages", {}).values():
                title = page["title"]
                match_revisions[title] = (page["pageid"], page["lastrevid"], None)
                sources[title] = ("match", None)
            continuation = result.get("continue", {})
            if "gapcontinue" not in continuation:
                break
        refresh(list(match_revisions), match_revisions)
        for title in match_revisions:
            if title in index:
                index[title].update(source="match", parent=None)
    # Keep category membership authoritative even if a former subpage now belongs
    # to the category and its revision did not change.
    for title in titles:
        if title in index:
            index[title].update(source="category", parent=None)
    cache.save_index(index)
    summary.subpages = sum(entry["source"] == "subpage" for entry in index.values())
    summary.match_pages = sum(entry["source"] == "match" for entry in index.values())
    summary.missing = len(missing)
    return summary
