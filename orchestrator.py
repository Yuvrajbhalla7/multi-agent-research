"""
Orchestrator.
This is the actual "multi-agent" piece: it runs the three agents in
sequence, loops the Writer/Critic pair until the report is approved
(or a max round limit is hit), and returns both the final report and
the step-by-step trace — useful for demoing how the agents collaborated.
"""

from agents.researcher import research
from agents.writer import write, revise
from agents.critic import critique, is_approved

MAX_REVISION_ROUNDS = 2


def run_research_pipeline(topic: str) -> dict:
    trace = []

    # Step 1: Researcher gathers facts
    research_notes = research(topic)
    trace.append({"agent": "researcher", "output": research_notes})

    # Step 2: Writer drafts the report
    draft = write(topic, research_notes)
    trace.append({"agent": "writer", "output": draft})

    # Step 3: Critic reviews, Writer revises, up to MAX_REVISION_ROUNDS times
    approved = False
    for round_num in range(1, MAX_REVISION_ROUNDS + 1):
        feedback = critique(draft, research_notes)
        trace.append({"agent": "critic", "round": round_num, "output": feedback})

        if is_approved(feedback):
            approved = True
            break

        draft = revise(draft, feedback)
        trace.append({"agent": "writer", "round": round_num, "output": draft})

    return {
        "topic": topic,
        "final_report": draft,
        "approved": approved,
        "trace": trace,
    }