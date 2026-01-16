from core.state import State
from core.memory import WeekMemory
from core.llm import groq_llm

from graph.pipeline import build_pipeline
from planner.five_day_plan import five_day_plan
from agents.creator import creator_agent
from rag.retriever import get_retriever


def generate_week(user_profile: dict):
    """
    MVP end-to-end execution:
    - Runs analysis pipeline once
    - Generates 5 LinkedIn posts
    """

    llm = groq_llm()
    retriever = get_retriever()

    app = build_pipeline(llm=llm, retriever=retriever)

    initial_state: State = {
        "user_profile": user_profile,
        "auditor_output": None,
        "analyst_output": None,
    }

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

        memory.mark_used(
            day_plan["hook_type"],
            day_plan["structure"],
            day_plan["focus"],
        )

        posts.append({
            "day": day_plan["day"],
            "post": post
        })

    return posts