from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your API!"}

@app.get("/generate_caption/")
def generate_caption(topic: str = "food"):
    captions = {
        "food": ["Taste the joy 🍴", "Fuel for the soul 😋"],
        "fitness": ["Stronger every day 💪", "Fuel your hustle 🏋️‍♂️"]
    }
    return {"topic": topic, "caption": captions.get(topic, ["Stay inspired!"])[0]}
