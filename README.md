# 📘 README — Autonomous LinkedIn Growth Agent

🚀 Autonomous LinkedIn Growth Agent (LangGraph + RAG)
*An agentic, multi-stage LinkedIn content automation system built using LangGraph, Retrieval-Augmented Generation (RAG), and deterministic planning.*

This project is a pipeline-level autonomous agent system designed to:
* Analyze a user’s domain and audience
* Extract winning content patterns from real LinkedIn posts
* Plan a coherent multi-day content narrative
* Generate high-quality, structured LinkedIn posts with strict constraints
* Enforce variation, topic adherence, and narrative continuity


### 🧠 System Philosophy
This system is built on explicit control, not prompt magic.

Key principles:
* Separation of concerns between agents
* Deterministic planning outside LLMs
* LLMs used only where generation is required
* Validation and control prioritized over creativity
* Scalability-first architecture


### 🧩 Architecture Overview

User Input
   │
   ▼
Auditor Agent
   │  (Extracts niche, theme, tone)
   ▼
Analyst Agent
   │  (RAG → patterns: hooks, structures, CTAs, keywords)
   ▼
Deterministic Planner (5-Day Plan)
   │
   ▼
Creator Agent (per day)
   │
   ▼
Weekly LinkedIn Posts


### 🤖 Agents

1. **Auditor Agent**
* Purpose: Strategic extraction
* Reads: User profile
* Writes: Professional niche, content theme, tone
* Does NOT:
* Generate posts
* Use RAG
* Access memory

2. **Analyst Agent**
* Purpose: Pattern mining via RAG
* Reads: Auditor output
* Writes:
1. Hook patterns
2. Post structures
3. CTA styles
4. Keywords
* Uses: Vector store of high-performing LinkedIn posts
* Does NOT: Generate content or strategy

3. **Creator Agent**
* Purpose: Controlled content generation
* Reads: Auditor + Analyst outputs
* Uses: External daily plan (day, focus, hook type, CTA rule)
* Guarantees:
1. Hook → Body → CTA template
2. Topic adherence
3. Series continuity
4. Academic / expert tone


### 🗂️ Planning & Memory
Deterministic Five-Day Planner
Planning is explicit and external to agents.
Each day specifies:
* Focus angle
* Hook intent
* CTA rule

This ensures:
Narrative coherence
No missing days
No creative drift
WeekMemory (Run-Scoped)
Tracks usage of:
Hook types
Structures
Focus angles
Used for variation control, not recall.


### 📚 RAG (Retrieval-Augmented Generation)
* Corpus: Real LinkedIn posts (txt-based, chunked)
* Embeddings: Free embedding service (no OpenAI dependency)
* Retrieval used for pattern grounding, not factual QA
* RAG enriches style and structure, not knowledge.


### ⚙️ Tech Stack
* LangGraph — agent orchestration
* LangChain — LLM abstraction
* Groq LLM — fast inference
* Vector Store — pattern retrieval
* Python — script-based architecture
* uv — execution environment


### 📦 Project Structure (Simplified)

core/
  ├── state.py
  ├── prompts.py
  ├── llm.py
  ├── memory.py

agents/
  ├── auditor.py
  ├── analyst.py
  ├── creator.py

planner/
  └── five_day_plan.py

rag/
  ├── loader.py
  ├── embeddings.py
  └── retriever.py

graph/
  └── pipeline.py

run/
  └── generate_week.py


### ▶️ Usage

uv run python -m run.generate_week

Input:
User profile
Topic


### Output:
5 high-quality, coherent LinkedIn posts
One per day, fully structured
🎯 Current Status (MVP)
* ✔ Multi-agent LangGraph pipeline
* ✔ Deterministic planning
* ✔ RAG-backed pattern extraction
* ✔ Variation control via memory
* ✔ Topic-conditioned generation
* ✔ Script-based (API-ready)


### 🧠 Who This Is For
1. Agentic AI engineers
2. Systems-focused LLM developers
3. Anyone who wants control, not demos