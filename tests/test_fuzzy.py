from core.trie import Trie

def test_autocomplete():
    trie = Trie()
    trie.insert("Connor McDavid", {"Player": "Connor McDavid", "Goals": 64})
    trie.insert("Auston Matthews", {"Player": "Auston Matthews", "Goals": 60})

    results = trie.autocomplete("Co")
    assert len(results) == 1
    assert results[0]["Player"] == "Connor McDavid"
