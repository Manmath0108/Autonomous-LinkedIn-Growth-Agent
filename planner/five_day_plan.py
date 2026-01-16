def five_day_plan():
    """
    Deterministic 5-day LinkedIn content plan.
    Planning logic lives outside agents and LangGraph.
    """

    return [
        {
            "day": 1,
            "focus": "conceptual framing",
            "hook_type": "question",
            "structure": "explanatory essay",
            "cta": "Introduce the series"
        },
        {
            "day": 2,
            "focus": "theoretical depth",
            "hook_type": "continuation",
            "structure": "argumentative analysis",
            "cta": "Tease the next post"
        },
        {
            "day": 3,
            "focus": "expert perspective",
            "hook_type": "authority",
            "structure": "interview / discussion",
            "cta": "Invite discussion"
        },
        {
            "day": 4,
            "focus": "practical breakdown",
            "hook_type": "list",
            "structure": "list-based breakdown",
            "cta": "Encourage reflection"
        },
        {
            "day": 5,
            "focus": "synthesis & closure",
            "hook_type": "reflection",
            "structure": "summary synthesis",
            "cta": "Close the series"
        },
    ]