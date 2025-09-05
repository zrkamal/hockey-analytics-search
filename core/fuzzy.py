def levenshtein_distance(a: str, b: str) -> int:
    """Compute the Levenshtein distance between two strings."""
    n, m = len(a), len(b)
    if n == 0: return m
    if m == 0: return n

    # Initialize matrix
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1].lower() == b[j - 1].lower():
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )
    return dp[n][m]

def fuzzy_match_score(query: str, target: str) -> float:
    """
    Returns a normalized similarity score between 0 and 1.
    1 = exact match, 0 = completely different
    """
    distance = levenshtein_distance(query, target)
    max_len = max(len(query), len(target))
    return 1 - (distance / max_len)

def fuzzy_search(query: str, items: list, threshold: float = 0.7):
    """
    Return items that match query above threshold.
    Items: list of dicts with 'Player' or 'Team' key
    """
    matches = []
    for item in items:
        name = item.get("Player") or item.get("Team")
        score = fuzzy_match_score(query, name)
        if score >= threshold:
            matches.append((score, item))
    # Sort by score descending
    matches.sort(key=lambda x: x[0], reverse=True)
    return [item for score, item in matches]
