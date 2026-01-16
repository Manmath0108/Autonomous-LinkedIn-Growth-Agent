from typing import Dict
from core.state import State
from core.prompts import CREATOR_PROMPT
from langchain_core.messages import HumanMessage


def creator_agent(base_state: State, plan: dict, llm) -> str:
    """
    Creator Agent (Generative, STRICT TEMPLATE)

    Reads:
    - auditor_output
    - analyst_output
    - topic

    Uses:
    - deterministic 5-day plan (focus, hook_type, cta_rule)

    Outputs:
    - ONE LinkedIn post following:
      HOOK → CONTENT → CTA
    """

    auditor = base_state["auditor_output"]
    analyst = base_state["analyst_output"]

    prompt = CREATOR_PROMPT.format(
        # Core context
        topic=base_state["topic"],
        professional_niche=auditor["professional_niche"],
        content_theme=auditor["content_theme"],
        tone=auditor["tone"],

        # Analyst constraints (patterns, not instructions)
        hook_patterns=analyst["hook_patterns"][:2],
        cta_styles=analyst["cta_styles"][:2],
        keywords=analyst["keywords"],

        # Planning contract
        day=plan["day"],
        focus=plan["focus"],
        hook_type=plan["hook_type"],
        cta_rule=plan["cta_rule"],
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.content.strip()