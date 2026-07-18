"""
Critic agent.
Job: review the Writer's draft against the original research notes.
Either approves it, or returns specific, actionable feedback.
"""

from agents.llm import call_llm

SYSTEM_PROMPT = """You are an editor reviewing a report draft against the \
original research notes it was based on. Check for:
- Claims not supported by the research notes
- Missing important facts from the research notes
- Unclear structure or writing

If the report is solid, respond with exactly: APPROVED

Otherwise, respond with specific, actionable feedback as a short bullet \
list (do not rewrite the report yourself — just say what needs fixing)."""


def critique(draft: str, research_notes: str) -> str:
    """Review a draft. Returns 'APPROVED' or feedback bullets."""
    user_prompt = f"Research notes:\n{research_notes}\n\nDraft report:\n{draft}"
    return call_llm(SYSTEM_PROMPT, user_prompt)


def is_approved(critique_text: str) -> bool:
    return critique_text.strip().upper().startswith("APPROVED")