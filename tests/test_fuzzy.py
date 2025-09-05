import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from core.fuzzy import fuzzy_search

def test_fuzzy_exact_match():
    players = [{"Player": "Connor McDavid"}, {"Player": "Auston Matthews"}]
    result = fuzzy_search("Connor McDavid", players)
    assert result[0]["Player"] == "Connor McDavid"

def test_fuzzy_typo_match():
    players = [{"Player": "Connor McDavid"}, {"Player": "Auston Matthews"}]
    result = fuzzy_search("Conor McDvaid", players, threshold=0.7)
    assert result[0]["Player"] == "Connor McDavid"

def test_fuzzy_no_match():
    players = [{"Player": "Connor McDavid"}, {"Player": "Auston Matthews"}]
    result = fuzzy_search("Sidney Crosby", players, threshold=0.8)
    assert result == []
