from typing import Dict, Optional, List
from core.state import State, AnalystOutput

def analyst_agent(state: State, retriever) -> Dict[str, Optional[AnalystOutput]]:
    """
    Analyst Agent

    Reads:
    - auditor_output

    Writes:
    - analyst_output

    Responsibilities:
    - Retrieve similar high-performing LinkedIn posts
    - Extract winning patterns:
        * hooks
        * post structures
        * CTA styles
        * keywords

    Non-responsibilities:
    - No post generation
    - No strategy decisions
    - No memory
    """

    auditor_output = state["auditor_output"]

    query = f"""
    High-performing LinkedIn posts about {auditor_output['professional_niche']}
    written in a {auditor_output['tone']} tone.
    """

    retrieved_docs = retriever.invoke(query)

    hooks: List[str] = []
    structures: List[str] = []
    ctas: List[str] = []
    keywords: List[str] = []

    for doc in retrieved_docs:
        text = doc.page_content.strip()

        # --- Hook extraction (first paragraph) ---
        first_paragraph = text.split("\n\n")[0].strip()
        hooks.append(first_paragraph)

        # --- Post structure (heuristic classification) ---
        if text.count("\n") > 6:
            structures.append("Explanatory essay")
        elif "?" in first_paragraph:
            structures.append("Provocative question")
        else:
            structures.append("Short-form insight")

        # --- CTA extraction (last block) ---
        last_block = text.split("\n\n")[-1].strip()
        ctas.append(last_block)

        words = [
            w.lower().strip(".,()")
            for w in text.split()
            if len(w) > 6
        ]
        keywords.extend(words)

    analyst_output: AnalystOutput = {
        "hook_patterns": hooks,
        "post_structures": structures,
        "cta_styles": ctas,
        "keywords": list(set(keywords))[:20],
    }

    return {"analyst_output": analyst_output}