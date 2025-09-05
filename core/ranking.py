import heapq

def top_k_players(players: list, key_metric: str, k: int = 5):
    """
    Return top-k players based on a key metric (e.g., 'Points', 'Goals').

    players: list of dicts [{'Player':..., 'Goals':..., 'Points':...}]
    key_metric: string metric to rank by
    k: number of top results
    """
    if not players or k <= 0:
        return []

    # heapq.nlargest returns top k elements based on key function
    return heapq.nlargest(k, players, key=lambda x: x.get(key_metric, 0))
