# reports/utils.py

from rapidfuzz import fuzz
from api.serializer import FoundItemSerializer

def compute_similarity(a: str, b: str) -> float:
    """
    Returns a similarity ratio (0-100) between two strings using rapidfuzz.
    """
    if not a or not b:
        return 0
    return fuzz.token_sort_ratio(a.lower(), b.lower())

def match_lost_item(lost_item, found_items):
    """
    Returns a list of found items serialized, each with an additional 'score' field.
    The list is sorted by score descending.
    """
    matches = []

    for found in found_items:
        score = 0

        # Name similarity (50% weight)
        score += compute_similarity(lost_item.name, found.name) * 0.5

        # Category match (20 points)
        score += 20 if lost_item.category == found.category else 0

        # Location similarity (20% weight)
        score += compute_similarity(lost_item.location, found.location) * 0.2

        # Date proximity (within 7 days, 10 points)
        date_diff = abs((lost_item.date_lost - found.date_found).days)
        if date_diff <= 7:
            score += 10

        # Description similarity (20% weight)
        score += compute_similarity(lost_item.description, found.description) * 0.2

        # Serialize found item and attach score
        serialized = FoundItemSerializer(found).data
        serialized['score'] = round(score, 2)

        matches.append(serialized)

    # Sort by score descending
    matches.sort(key=lambda x: x['score'], reverse=True)

    return matches
