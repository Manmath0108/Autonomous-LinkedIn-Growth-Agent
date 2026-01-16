from core.state import State, AuditorOutput
from core.prompts import AUDITOR_PROMPT

from typing import Dict, Optional
from langchain_openai import ChatOpenAI

def auditor_agent(state: State, llm: ChatOpenAI) -> Dict[str, Optional[AuditorOutput]]:
    """
    Auditor Agent

    Reads:
    - user_profile

    Writes:
    - auditor_output

    Responsibilities:
    - Identify professional niche
    - Identify content theme
    - Identify tone

    Non-responsbilities:
    - No post generation
    - No RAG
    - No memory
    """
    user_profile = state['user_profile']

    prompt = AUDITOR_PROMPT.format(
        profile_description=user_profile.get("profile_description"),
        expertise=user_profile.get('expertise'),
        target_audience=user_profile.get("target_audience")
    )
    response = llm.invoke(prompt)
    lines = response.content.split("\n")

    parsed = {}
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            parsed[key.strip().lower()] = value.strip()
    
    auditor_output: AuditorOutput = {
        "professional_niche": parsed.get("professional_niche"),
        "content_theme": parsed.get("content theme"),
        "tone": parsed.get("tone")
    }

    return {"auditor_output": auditor_output}