from typing import Dict
from core.state import State
from langchain_core.messages import HumanMessage


def creator_agent(
    base_state: State,
    plan: Dict,
    llm,
) -> str:
    """
    Creator Agent (Generative):
    - Reads: auditor_output, analyst_output
    - Uses: external plan (day, hook_type, structure, focus, cta intent)
    - Generates: ONE LinkedIn post
    - Does NOT manage memory, looping, or scheduling
    """

    auditor = base_state["auditor_output"]
    analyst = base_state["analyst_output"]

    prompt = f"""
    You are a LinkedIn content creator writing for an expert audience.

    CONTEXT:
    - Professional Niche: {auditor["professional_niche"]}
    - Content Theme: {auditor["content_theme"]}
    - Tone: {auditor["tone"]}

    WINNING PATTERNS (from analysis of high-performing posts):
    - Hooks: {analyst["hook_patterns"]}
    - Common Structures: {analyst["post_structures"]}
    - Common CTAs: {analyst["cta_styles"]}
    - Keywords: {analyst["keywords"]}

    TODAY'S PLAN:
    - Day: {plan["day"]}
    - Focus: {plan["focus"]}
    - Hook Type: {plan["hook_type"]}
    - Structure: {plan["structure"]}

    TASK:
    Write ONE high-quality LinkedIn post that:
    - Matches the professional niche, theme, and tone
    - Uses ONE hook style consistent with the plan
    - Follows the specified structure
    - Is original and non-repetitive
    - Is written for an academic / expert audience
    - Avoids emojis, slang, and casual language

    CTA INSTRUCTIONS (STRICT):

    You are writing Day {plan["day"]} of a 5-day LinkedIn series.

    Follow these rules exactly:

    - Day 1:
    End with a neutral continuation statement.
    Do NOT ask a question.
    Example: “This sets the stage for deeper exploration in the coming days.”

    - Day 2:
    End by referencing tomorrow’s focus.
    Do NOT ask for engagement.
    Example: “Tomorrow, we examine how these ideas manifest in practice.”

    - Day 3:
    You MAY invite reflection or discussion.
    At most ONE sentence.
    Academic tone only.

    - Day 4:
    End with a reflective synthesis statement.
    No engagement request.

    - Day 5:
    End with a definitive conclusion.
    Do NOT ask questions.
    Do NOT suggest future posts.
    The series must feel complete.

    OUTPUT RULES:
    - Do NOT label sections
    - Do NOT explain your reasoning
    - Output ONLY the LinkedIn post text
    """

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.content.strip()