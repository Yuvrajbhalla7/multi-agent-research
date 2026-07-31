

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from orchestrator import run_research_pipeline

app = FastAPI(title="Multi-Agent Research Assistant")


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



app.mount("/", StaticFiles(directory="static", html=True), name="static")