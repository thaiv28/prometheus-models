"""Approximate R6 tournament host macro regions."""

from promr6.liquipedia.parse import clean

INTERNATIONAL_COUNTRIES = {"World", "International", "Global", "Americas"}
_REGION_NAMES = {
    "NA": "North America, United States, Canada, NA",
    "EU": "Europe, Europe MENA, EU/MENA, EU-MENA, Europe-MENA, Europe and MENA, MENA, Middle East, Saudi Arabia, United Arab Emirates, Qatar, Kuwait, Jordan, Lebanon, Israel, Egypt, Morocco, Tunisia, Algeria, Turkey, Russia, Ukraine, CIS, Sweden, United Kingdom, Poland, Germany, Portugal, Finland, Denmark, Czech Republic, Romania, France, Spain, Netherlands, Norway, Belgium, Italy, Hungary, Serbia, Bulgaria, Slovakia, Greece, Austria, Switzerland, Croatia, Estonia, Latvia, Lithuania, Ireland, Bosnia and Herzegovina, Slovenia, Montenegro, North Macedonia, Albania, Kosovo, Iceland, Malta, Cyprus, Luxembourg, EU",
    "SA": "South America, Brazil, Argentina, Chile, Peru, Colombia, Uruguay, Paraguay, Bolivia, Ecuador, Venezuela, Latin America, Latin America North, Central America, Mexico, LATAM, SA",
    "APAC": "Asia, Asia-Pacific, APAC, Oceania, Australia, New Zealand, Japan, South Korea, Korea, Taiwan, Hong Kong, Singapore, Malaysia, Indonesia, Philippines, Thailand, Vietnam, Southeast Asia, East Asia, South Asia, India, Mongolia, Pakistan, Bangladesh, Sri Lanka, Nepal",
    "CN": "China, CN",
}
REGIONS = {
    name.strip(): code
    for code, names in _REGION_NAMES.items()
    for name in names.split(",")
}


def region(country):
    return REGIONS.get(clean(country)) if country else None
