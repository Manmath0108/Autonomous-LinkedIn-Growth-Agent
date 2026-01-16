from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from run.generate_week import generate_week

app = FastAPI(
    title="Autonomous LinkedIn Growth Agent",
    description="Multi-agent LangGraph pipeline for LinkedIn content automation",
    version="0.1.0"
)

class GenerateWeekRequest(BaseModel):
    profile_description: str
    expertise: str
    target_audience: str
    topic: str

class GeneratedPost(BaseModel):
    day: int
    post: str

class GenerateWeekResponse(BaseModel):
    posts: List[GeneratedPost]

@app.post("/generate-week", response_model=GenerateWeekResponse)
def generate_week_endpoint(payload: GenerateWeekRequest):
    try:
        user_profile = {
            "profile_description": payload.profile_description,
            "expertise": payload.expertise,
            "target_audience": payload.target_audience,
        }
        posts = generate_week(
            user_profile=user_profile,
            topic=payload.topic
        )

        return {"posts": posts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))