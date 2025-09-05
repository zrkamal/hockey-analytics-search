import heapq

def top_k_players(players: list, key_metric: str, k: int = 5):
    """
    players: list of dicts {'Player':..., 'Goals':..., 'Points':...}
    key_metric: metric to rank players by
    """
    return heapq.nlargest(k, players, key=lambda x: x.get(key_metric, 0))
