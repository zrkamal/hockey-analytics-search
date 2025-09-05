from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Hockey Analytics Search System")

# Load sample dataset
df = pd.read_csv("data/hockey_stats.csv")

@app.get("/")
def root():
    return {"message": "Hockey Analytics Search System is live!"}

@app.get("/players")
def get_players():
    return df.to_dict(orient="records")
