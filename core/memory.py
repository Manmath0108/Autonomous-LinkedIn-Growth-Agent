class WeekMemory:
    """
    Run-scoped memory for enforcing strict variation
    across a 5-day LinkedIn content series.
    """

    def __init__(self):
        self.used_hook_types = set()
        self.used_structures = set()
        self.used_focus_angles = set()

    def mark_used(self, hook_type: str, structure: str, focus: str):
        self.used_hook_types.add(hook_type)
        self.used_structures.add(structure)
        self.used_focus_angles.add(focus)

    def is_hook_used(self, hook_type: str) -> bool:
        return hook_type in self.used_hook_types

    def is_structure_used(self, structure: str) -> bool:
        return structure in self.used_structures

    def is_focus_used(self, focus: str) -> bool:
        return focus in self.used_focus_angles