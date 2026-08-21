# Multi-Agent Research Assistant

An AI system where multiple specialized agents collaborate to research a topic and produce a polished, fact-checked report — inspired by AutoGen's AutoBuild pattern.

## What it does

Give the system a research topic or question, and instead of a single LLM call producing one draft, three agents work in sequence — each responsible for a distinct stage of the process — to produce a higher-quality final report than a single-pass approach could.

## Architecture

```
User Query
    │
    ▼
┌─────────────────┐
│  Search Agent    │  → gathers information from available sources
└────────┬─────────┘
         ▼
┌─────────────────┐
│  Draft Agent     │  → synthesizes findings into a structured report
└────────┬─────────┘
         ▼
┌─────────────────┐
│  Critique Agent  │  → reviews the draft, flags gaps/errors, refines it
└────────┬─────────┘
         ▼
   Final Report
```

- **`orchestrator.py`** — coordinates handoffs between agents and manages shared state/context across the pipeline
- **`agents/`** — individual agent definitions (search/gather, draft, critique/refine)
- **`tools/`** — utilities the agents call (e.g. search, data retrieval)
- **`static/`** — frontend UI
- **`main.py`** — FastAPI entry point, exposes the `/research` endpoint

## Tech stack

- **Backend:** FastAPI (Python)
- **Orchestration:** Custom multi-agent orchestrator (AutoBuild-inspired role pattern)
- **Frontend:** HTML/CSS/JS calling the FastAPI backend

## Key technical challenges

- **Agent role coordination** — ensuring each agent has the right context from the previous stage without redundant or lost information as it passes through the pipeline.
- **State management across handoffs** — maintaining shared context (search results, draft versions) as data flows from search → draft → critique.
- **Orchestration logic** — sequencing agent calls reliably so the pipeline completes end-to-end without manual intervention.

## Getting started

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open the frontend and submit a research query to see the agents work through the pipeline.

## Status

Running end-to-end. Built as a portfolio project demonstrating agentic AI system design beyond single-prompt LLM applications.
