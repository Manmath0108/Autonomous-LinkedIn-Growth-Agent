def five_day_plan():
    """
    Deterministic 5-day LinkedIn content plan.
    Planning logic lives outside agents and LangGraph.
    """

    return [
        {
            "day": 1,
            "focus": "conceptual framing",
            "hook_type": "question_framing",
            "cta_rule": "neutral_continuation"
        },
        {
            "day": 2,
            "focus": "theoretical depth",
            "hook_type": "continuation_reference",
            "cta_rule": "reference_tomorrow"
        },
        {
            "day": 3,
            "focus": "expert perspective",
            "hook_type": "authority_framing",
            "cta_rule": "invite_reflection"
        },
        {
            "day": 4,
            "focus": "practical synthesis",
            "hook_type": "directive_framing",
            "cta_rule": "reflective_synthesis"
        },
        {
            "day": 5,
            "focus": "closure",
            "hook_type": "reflective_synthesis",
            "cta_rule": "definitive_close"
        },
    ]
    