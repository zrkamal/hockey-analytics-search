import sys
import os
import pytest

# Add project root to PYTHONPATH so core can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.trie import Trie

def test_autocomplete_single_player():
    trie = Trie()
    trie.insert("Connor McDavid", {"Player": "Connor McDavid", "Goals": 64})
    trie.insert("Auston Matthews", {"Player": "Auston Matthews", "Goals": 60})

    results = trie.autocomplete("Con")
    assert len(results) == 1
    assert results[0]["Player"] == "Connor McDavid"

def test_autocomplete_multiple_players():
    trie = Trie()
    trie.insert("Connor McDavid", {"Player": "Connor McDavid", "Goals": 64})
    trie.insert("Connor Brown", {"Player": "Connor Brown", "Goals": 20})

    results = trie.autocomplete("Con")
    assert len(results) == 2
    player_names = [p["Player"] for p in results]
    assert "Connor McDavid" in player_names
    assert "Connor Brown" in player_names
