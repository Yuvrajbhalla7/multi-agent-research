"""
Researcher agent.
Job: take a topic, search the web, and condense raw results into
a clean list of key facts with sources. This is the only agent
that touches the search tool.
"""

from agents.llm import call_llm
from tools.search import search

SYSTEM_PROMPT = """You are a research assistant. You will be given raw \
search result snippets about a topic. Your job is to extract the most \
important, relevant facts and present them as a concise bullet list. \
Each bullet should be one fact, and end with its source in parentheses. \
Ignore snippets that are irrelevant or low quality. Do not add facts \
that aren't in the provided snippets."""


def research(topic: str) -> str:
    """Search for a topic and return a bullet-point fact list with sources."""
    raw_results = search(topic, max_results=6)

    if not raw_results:
        return f"No search results found for: {topic}"

    combined = "\n\n".join(raw_results)
    user_prompt = f"Topic: {topic}\n\nSearch results:\n{combined}"

    return call_llm(SYSTEM_PROMPT, user_prompt)