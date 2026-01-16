class WeekMemory:
    """
    Run-scoped memory for observing and optionally enforcing
    variation across a 5-day LinkedIn content series.

    This memory does NOT control planning.
    It only records what has been used.
    """

    def __init__(self):
        self.used_hook_types = set()
        self.used_cta_rules = set()
        self.used_focus_angles = set()

    def mark_used(self, hook_type: str, cta_rule: str, focus: str):
        """
        Record what was used for a given day.
        """
        self.used_hook_types.add(hook_type)
        self.used_cta_rules.add(cta_rule)
        self.used_focus_angles.add(focus)

    def is_hook_used(self, hook_type: str) -> bool:
        return hook_type in self.used_hook_types

    def is_cta_rule_used(self, cta_rule: str) -> bool:
        return cta_rule in self.used_cta_rules

    def is_focus_used(self, focus: str) -> bool:
        return focus in self.used_focus_angles