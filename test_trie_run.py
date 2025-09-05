import pandas as pd
from core.trie import Trie

# Load CSV
df = pd.read_csv("data/hockey_stats.csv")

# Initialize Trie
player_trie = Trie()

# Insert players into Trie
for _, row in df.iterrows():
    player_name = row["Player"].strip()  # Remove leading/trailing spaces
    player_trie.insert(player_name, row.to_dict())

# Test autocomplete with log_nodes
test_prefix = "Con"
results, nodes_visited = player_trie.autocomplete(test_prefix, log_nodes=True)

print(f"Results for '{test_prefix}':")
for player in results:
    print(f"- {player['Player']} ({player['team']})")

print(f"Nodes visited: {nodes_visited}")
