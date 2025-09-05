# app/main.py
from fastapi import FastAPI, Query
import pandas as pd
from core.trie import Trie
from core.fuzzy import fuzzy_search
from core.ranking import top_k_players
from time import perf_counter
from pathlib import Path
import csv
import time

# --- CONFIG ---
QUERY_LOG_FILE = Path("data/query_log.csv")

# Initialize CSV if it doesn't exist
if not QUERY_LOG_FILE.exists():
    with open(QUERY_LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "query_type", "query", "num_results", "nodes_visited", "latency_ms"])

def log_query(query_type, query, num_results, nodes_visited, latency_ms):
    """Append a query entry to query_log.csv"""
    with open(QUERY_LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), query_type, query, num_results, nodes_visited, latency_ms])

# --- LOAD DATA ---
df = pd.read_csv("data/hockey_stats.csv")

# Strip headers and player names
df.columns = df.columns.str.strip()
if "Player" not in df.columns:
    raise ValueError("CSV must have a 'Player' column")

df = df[df["Player"].notna()]  # filter out empty names

# Initialize Trie
player_trie = Trie()
for _, row in df.iterrows():
    name = str(row["Player"]).strip()
    if name:
        player_trie.insert(name, row.to_dict())

# Quick sanity test (optional)
test_results, nodes = player_trie.autocomplete("Way", log_nodes=True)
print("Sanity test autocomplete results:", test_results)
print("Nodes visited:", nodes)

# --- FASTAPI APP ---
app = FastAPI(title="Hockey Analytics Search API")

@app.get("/")
def root():
    return {"message": "Hockey Analytics Search API is running!"}

@app.get("/players/search")
def search_players(prefix: str = Query(..., description="Prefix for player search")):
    start = perf_counter()
    results, nodes_visited = player_trie.autocomplete(prefix, log_nodes=True)
    latency = (perf_counter() - start) * 1000  # milliseconds
    log_query("prefix_search", prefix, len(results), nodes_visited, latency)
    return {"results": results, "nodes_visited": nodes_visited, "latency_ms": latency}

@app.get("/players/fuzzy")
def fuzzy_players(query: str = Query(..., description="Fuzzy search query"),
                  top_k: int = Query(3, description="Number of top matches"),
                  metric: str = Query("points", description="Metric to rank by")):
    """Fuzzy search with top-k ranking"""
    player_names = df["Player"].tolist()
    matches = fuzzy_search(query, player_names, n=top_k)
    matched_df = df[df["Player"].isin(matches)]
    ranked = top_k_players(matched_df, metric=metric, k=top_k)
    return ranked

@app.get("/players/top")
def top_players(metric: str = Query("points", description="Metric to rank by"),
                k: int = Query(5, description="Number of top players")):
    """Return top-k players by metric"""
    ranked = top_k_players(df, metric=metric, k=k)
    return ranked
