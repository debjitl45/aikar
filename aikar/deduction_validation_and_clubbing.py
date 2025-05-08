# Define the tax deduction categories and their respective limits
from typing import Dict, List

# Grouping of deductions under umbrella sections with limits
DEDUCTION_CATEGORIES = {
    "80C": {
        "aliases": ["ppf", "lic", "elss", "5-year fd", "nsc", "tuition fees", "home loan principal", "nps", "80c",
                    "sukanya samridhi yojna", "scss", "80ccc", "80ccd(1)", "sukanya yojna", "tax saving fd", "80ccd1",
                    "80ccd"],
        "limit": 150000
    },
    "80CCD(1B)": {
        "aliases": ["nps additional", "80ccd(1b)", "80ccd1b", "nps additional"],
        "limit": 50000
    },
    "80CCD(2)": {
        "aliases": ["employer nps", "corporate nps", "80ccd(2)", "80CCD2", "80ccd2"],
        "limit": 200000  # 10% of Basic+DA, handled separately
    },
    "80D": {
        "aliases": ["health insurance", "medical insurance", "80d self", "80d parents", "80d", "80D"],
        "limit": 100000  # max assuming both are senior citizens
    },
    "80EEA": {
        "aliases": ["home loan interest affordable", "80eea"],
        "limit": 150000
    },
    "80EE": {
        "aliases": ["home loan interest first time", "80ee"],
        "limit": 50000
    },
    "80E": {
        "aliases": ["education loan", "80e"],
        "limit": None  # No limit
    },
    "80G": {
        "aliases": ["donation", "80g"],
        "limit": None  # Depends on type of donation
    },
    "80GG": {
        "aliases": ["house rent", "rent without hra", "80gg"],
        "limit": None  # Subject to conditions
    },
    "80TTA": {
        "aliases": ["savings interest", "80tta"],
        "limit": 10000
    },
    "80TTB": {
        "aliases": ["senior citizen savings interest", "80ttb"],
        "limit": 50000
    }
}


def classify_and_sanitize_deductions(user_inputs: Dict[str, int]) -> Dict[str, int]:
    """
    Given user inputs (free-text categories and claimed amounts), group and sanitize them into standard sections.
    """
    section_totals = {key: 0 for key in DEDUCTION_CATEGORIES.keys()}

    for raw_key, amount in user_inputs.items():
        normalized_key = raw_key.strip().lower()
        for section, details in DEDUCTION_CATEGORIES.items():
            if normalized_key in details["aliases"]:
                section_totals[section] += amount
                break

    # Apply 80C group limit
    total_80C = section_totals["80C"]
    if total_80C > DEDUCTION_CATEGORIES["80C"]["limit"]:
        section_totals["80C"] = DEDUCTION_CATEGORIES["80C"]["limit"]

    # Apply other limits
    for section, amount in section_totals.items():
        limit = DEDUCTION_CATEGORIES[section]["limit"]
        if limit is not None and amount > limit:
            section_totals[section] = limit

    return section_totals
