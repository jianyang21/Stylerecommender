from fastapi import FastAPI
from pydantic import BaseModel
from model import FashionRecommender
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# load ML model
recommender = FashionRecommender("synthetic_fashion_dataset.csv")

class UserInput(BaseModel):
    preference: str

@app.post("/recommend")
def get_recommendations(data: UserInput):
    results = recommender.recommend(data.preference)
    return {"recommendations": results}
