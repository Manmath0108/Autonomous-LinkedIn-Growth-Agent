from core.state import State
from core.memory import WeekMemory
from core.llm import groq_llm

from graph.pipeline import build_pipeline
from planner.five_day_plan import five_day_plan
from agents.creator import creator_agent
from rag.retriever import get_retriever


def generate_week(user_profile: dict, topic: str):
    """
    MVP end-to-end execution:
    - Runs Auditor + Analyst once
    - Generates 5 LinkedIn posts using a deterministic 5-day plan
    """

    llm = groq_llm()
    retriever = get_retriever()

    app = build_pipeline(llm=llm, retriever=retriever)

    initial_state: State = {
        "user_profile": user_profile,
        "topic": topic,
        "auditor_output": None,
        "analyst_output": None,
    }

    # Run analysis pipeline once
    base_state = app.invoke(initial_state)

    memory = WeekMemory()
    plan = five_day_plan()

    posts = []

    for day_plan in plan:
        post = creator_agent(
            base_state=base_state,
            plan=day_plan,
            llm=llm,
        )

        # Lightweight variation tracking (MVP)
        memory.mark_used(
            hook_type=day_plan["hook_type"],
            focus=day_plan["focus"],
            cta_rule=day_plan["cta_rule"],
        )

        posts.append({
            "day": day_plan["day"],
            "post": post
        })

    return posts


if __name__ == "__main__":
    user_profile = {
        "profile_description": "AI Enthuthiast, Knowledgeable in Neural Networks",
        "expertise": "Transformer Neural Network, Attention Mechanisms",
        "target_audience": "Students, Undergraduates"
    }

    posts = generate_week(user_profile, topic="Data Science in Modern AI")

    for p in posts:
        print(f"\n--- DAY {p['day']} ---\n")
        print(p["post"])
        print("\n" + "-" * 50)