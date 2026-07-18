"""
Writer agent.
Job: turn the Researcher's fact list into a structured report.
Also handles revisions when the Critic sends back feedback.
"""

from agents.llm import call_llm

SYSTEM_PROMPT = """You are a report writer. You will be given a topic and \
a list of researched facts with sources. Write a clear, well-structured \
report with:
- A short introduction
- 2-4 body sections with headers, covering the facts logically
- A brief conclusion
Keep it factual and grounded only in the provided research. Use markdown \
formatting (## headers)."""

REVISION_SYSTEM_PROMPT = """You are a report writer revising a draft based \
on editor feedback. Keep everything that wasn't criticized, and fix only \
what the feedback points out. Return the full revised report, not just \
the changed parts."""


def write(topic: str, research_notes: str) -> str:
    """Write a first-draft report from research notes."""
    user_prompt = f"Topic: {topic}\n\nResearch notes:\n{research_notes}"
    return call_llm(SYSTEM_PROMPT, user_prompt)


def revise(draft: str, feedback: str) -> str:
    """Revise a draft based on critic feedback."""
    user_prompt = f"Draft:\n{draft}\n\nEditor feedback:\n{feedback}"
    return call_llm(REVISION_SYSTEM_PROMPT, user_prompt)