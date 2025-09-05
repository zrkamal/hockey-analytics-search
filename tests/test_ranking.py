import sys
import os
import pytest

# Add project root to PYTHONPATH so core can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.ranking import top_k_players

def test_top_k_points():
    players = [
        {"Player": "A", "Points": 10},
        {"Player": "B", "Points": 20},
        {"Player": "C", "Points": 15},
    ]
    top = top_k_players(players, "Points", k=2)
    top_names = [p["Player"] for p in top]
    assert top_names == ["B", "C"]

def test_top_k_goals():
    players = [
        {"Player": "X", "Goals": 5},
        {"Player": "Y", "Goals": 12},
        {"Player": "Z", "Goals": 8},
    ]
    top = top_k_players(players, "Goals", k=1)
    assert top[0]["Player"] == "Y"
