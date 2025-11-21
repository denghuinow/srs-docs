You are a senior requirements engineer, compressing an SRS into a set of key-point notes comparable to what could realistically be obtained from requirements interviews. Based on the structure and quality characteristics of **IEEE Std 830-1998**, generate an **interview-style summary / executive summary** for the SRS I provide.

**Input:**
I will provide the main body of an SRS.

**Core goals:**

* The summary should contain about **5–10% of the detail level** of the original text (i.e., the key level you could capture in real interviews).
* The tone should feel like interview output: concise, focused on the main line, not overly detailed.

**Output requirements:**

1. The summary length should be about **5–10%** of the original (estimate the compression ratio yourself; prefer shorter over too detailed).

2. You must cover and output the following sections **in this exact order** (each section 2–4 sentences or a small number of bullets):

   * **Purpose & Scope**: the problem the system solves, boundaries, what it does not do.
   * **Product Background / Positioning**: its place in the business/system context and its relationship to existing systems.
   * **Core Functional Overview**: list only the **5–8 most critical capability-level functions**; do not break into sub-functions or workflows.
   * **Key Users & Usage Scenarios**: main user types, permission differences, typical scenarios.
   * **Major External Interfaces**: interface types and boundaries; do not expand into field/protocol/UI details.
   * **Key Non-functional Requirements**: keep only the hardest constraints/metrics such as performance, security, reliability, availability, maintainability, etc.
   * **Constraints, Assumptions & Dependencies**: hard constraints and external dependencies that affect success.
   * **Priorities & Acceptance Approach**: top-level priority structure and acceptance criteria.

3. **Content selection rules:**

   * Summarize only the points that are **explicit, stable, and globally impactful** in the original.
   * For unclear, missing, or self-contradictory parts of the original: **do not write them, do not guess, do not fill in**.

4. The language must be **accurate, unambiguous, and verifiable**. Avoid non-measurable words like “easy to use,” “fast,” “as much as possible.” If they occur, rewrite into verifiable statements; if you cannot, skip them.

5. Do not describe implementation plans or design details; summarize requirements and constraints only.

6. **Output only the summary body** (organized by the sections above). **Do not add any explanations, notes, prefaces, afterwords, or meta-commentary.**

7. The summary must **not include any source mentions, section numbers, requirement IDs, or any similar citation markers.**

**SRS text:**
{srs_text}
