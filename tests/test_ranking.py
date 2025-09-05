from core.ranking import top_k_players

def test_top_k():
    players = [
        {"Player": "A", "Points": 10},
        {"Player": "B", "Points": 20},
        {"Player": "C", "Points": 15},
    ]
    top = top_k_players(players, "Points", k=2)
    assert [p["Player"] for p in top] == ["B", "C"]
