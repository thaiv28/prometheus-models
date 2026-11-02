PRAGMA foreign_keys = ON;
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY, title TEXT UNIQUE NOT NULL, parent_title TEXT,
    name TEXT, tier TEXT, tier_type TEXT, section TEXT NOT NULL, country TEXT,
    region TEXT, international INTEGER NOT NULL, online INTEGER,
    start_date TEXT, end_date TEXT, mode TEXT, prize_usd REAL,
    excluded INTEGER NOT NULL, revid INTEGER, leagueid INTEGER
);
CREATE TABLE teams (team_id INTEGER PRIMARY KEY, key TEXT UNIQUE NOT NULL, name TEXT);
CREATE TABLE players (player_id INTEGER PRIMARY KEY, key TEXT UNIQUE NOT NULL, name TEXT);
CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY, event_id INTEGER NOT NULL REFERENCES events,
    page TEXT NOT NULL, ordinal INTEGER NOT NULL, start_utc TEXT NOT NULL,
    time_known INTEGER NOT NULL, best_of INTEGER,
    team1_id INTEGER NOT NULL REFERENCES teams, team2_id INTEGER NOT NULL REFERENCES teams,
    score1 INTEGER NOT NULL, score2 INTEGER NOT NULL,
    winner INTEGER CHECK (winner IN (1, 2)), siegegg_id INTEGER,
    walkover INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE maps (
    map_id INTEGER PRIMARY KEY, match_id INTEGER NOT NULL REFERENCES matches,
    map_order INTEGER NOT NULL CHECK (map_order BETWEEN 1 AND 9), map_name TEXT,
    rounds1 INTEGER, rounds2 INTEGER, winner INTEGER CHECK (winner IN (1, 2)),
    t1_atk INTEGER, t1_def INTEGER, t1_ot INTEGER,
    t2_atk INTEGER, t2_def INTEGER, t2_ot INTEGER, t1_first_side TEXT,
    UNIQUE (match_id, map_order), CHECK (map_id = match_id * 10 + map_order)
);
CREATE TABLE rosters (
    event_id INTEGER REFERENCES events, team_id INTEGER REFERENCES teams,
    slot INTEGER, player_id INTEGER REFERENCES players,
    complete INTEGER NOT NULL,
    PRIMARY KEY (event_id, team_id, slot)
);
CREATE TABLE player_maps (
    map_id INTEGER REFERENCES maps, team_side INTEGER CHECK (team_side IN (1, 2)),
    player_id INTEGER REFERENCES players, source TEXT,
    PRIMARY KEY (map_id, team_side, player_id)
);
CREATE TABLE match_substitutions (
    match_id INTEGER REFERENCES matches, side INTEGER CHECK (side IN (1, 2)),
    player_in TEXT, player_out TEXT,
    PRIMARY KEY (match_id, side, player_in, player_out)
);
CREATE TABLE kalshi_markets (
    ticker TEXT PRIMARY KEY, series TEXT NOT NULL, event_ticker TEXT NOT NULL,
    kind TEXT NOT NULL CHECK (kind IN ('series', 'map')), map_number INTEGER,
    team_code TEXT, team_name TEXT, competitor_id TEXT, scheduled_utc TEXT,
    event_name TEXT, status TEXT, result TEXT, volume REAL,
    open_time TEXT, close_time TEXT
);
CREATE TABLE team_aliases (
    competitor_id TEXT PRIMARY KEY, kalshi_name TEXT, kalshi_code TEXT,
    liquipedia_team_id INTEGER, liquipedia_name TEXT, events INTEGER
);
CREATE TABLE kalshi_links (
    event_ticker TEXT PRIMARY KEY, match_id INTEGER REFERENCES matches,
    map_id INTEGER REFERENCES maps,
    kind TEXT CHECK (kind IN ('series', 'map')), method TEXT, reason TEXT
);
CREATE INDEX matches_start_utc ON matches(start_utc);
CREATE INDEX maps_match_id ON maps(match_id);
CREATE INDEX matches_siegegg_id ON matches(siegegg_id);
