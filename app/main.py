from fastapi import FastAPI
import pandas as pd
from core.trie import Trie
from core.ranking import top_k_players

app = FastAPI(title="Hockey Analytics Search System")

# Load sample dataset
df = pd.read_csv("data/hockey_stats.csv")

# Build Trie for player names
player_trie = Trie()
for _, row in df.iterrows():
    player_trie.insert(row['Player'], row.to_dict())

@app.get("/")
def root():
    return {"message": "Hockey Analytics Search System is live!"}

@app.get("/players")
def get_players(prefix: str = None, top_k: int = 5, metric: str = "Points"):
    if prefix:
        matches = player_trie.autocomplete(prefix)
        top_results = top_k_players(matches, key_metric=metric, k=top_k)
        return top_results
    else:
        return df.to_dict(orient="records")
