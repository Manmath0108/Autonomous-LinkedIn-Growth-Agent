from typing import TypedDict, Optional, List

class UserProfile(TypedDict):
    profile_description: Optional[str]
    expertise: Optional[str]
    target_audience: Optional[str]

class AuditorOutput(TypedDict):
    professional_niche: Optional[str]
    content_theme: Optional[str]
    tone: Optional[str]

class AnalystOutput(TypedDict):
    hook_patterns: Optional[List[str]]
    post_structures: Optional[List[str]]
    cta_styles: Optional[List[str]]
    keywords: Optional[List[str]]

class State(TypedDict):
    user_profile: UserProfile
    topic: str
    auditor_output: Optional[AuditorOutput]
    analyst_output: Optional[AnalystOutput]
    creator_output: Optional[str]