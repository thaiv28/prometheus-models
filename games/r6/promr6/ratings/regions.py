"""R6 event macro-regions; unrecognized hosts have no region."""

REGION_CODES = ("NA", "EU", "SA", "APAC", "CN")
ALIASES = {
    "MENA": "EU",
    "Brazil": "SA",
    "LATAM": "SA",
    "Asia": "APAC",
    "Oceania": "APAC",
    "Japan": "APAC",
    "Korea": "APAC",
}


def macro_region(code):
    return code if code in REGION_CODES else ALIASES.get(code)
