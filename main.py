"""
FastAPI app.
Run with: uvicorn main:app --reload
Then go to http://127.0.0.1:8000/ for the frontend,
or POST to http://127.0.0.1:8000/research with {"topic": "..."}
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from orchestrator import run_research_pipeline

app = FastAPI(title="Multi-Agent Research Assistant")

# Allows the frontend (served separately, or opened as a local file) to
# call this API from the browser. Wide open here since this is a local
# demo project — lock this down before deploying anywhere public.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str


@app.post("/research")
def research_endpoint(req: ResearchRequest):
    result = run_research_pipeline(req.topic)
    return result


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Serves index.html at http://127.0.0.1:8000/ so you don't need a
# separate server for the frontend — this one line handles both.
# IMPORTANT: this must be added AFTER the routes above, or it will
# shadow them (FastAPI matches routes in the order they're registered).
app.mount("/", StaticFiles(directory="static", html=True), name="static")