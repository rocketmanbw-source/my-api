from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Marketing Analytics API")

# Load sample data
df = pd.read_csv("data/posts.csv")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Marketing Analytics API!"}

@app.get("/total_engagement/")
def total_engagement():
    total_likes = int(df["likes"].sum())
    total_comments = int(df["comments"].sum())
    total_shares = int(df["shares"].sum())
    return {
        "total_likes": total_likes,
        "total_comments": total_comments,
        "total_shares": total_shares
    }

@app.get("/top_post/")
def top_post():
    df["engagement"] = df["likes"] + df["comments"] + df["shares"]
    top = df.loc[df["engagement"].idxmax()]
    return {
        "post_id": int(top["post_id"]),
        "content": top["content"],
        "total_engagement": int(top["engagement"])
    }

@app.get("/average_engagement/")
def average_engagement():
    avg_likes = df["likes"].mean()
    avg_comments = df["comments"].mean()
    avg_shares = df["shares"].mean()
    return {
        "average_likes": round(avg_likes, 2),
        "average_comments": round(avg_comments, 2),
        "average_shares": round(avg_shares, 2)
    }
