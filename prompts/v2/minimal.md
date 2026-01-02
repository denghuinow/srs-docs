You are a senior requirements engineer, compressing an SRS into a minimal set of key points. Based on the structure and quality characteristics of **IEEE Std 830-1998**, generate a **minimal summary** for the SRS I provide.

**Input:**
I will provide the main body of an SRS.

**Core goals:**

* The summary should contain about **2–5% of the detail level** of the original text (retain only the most essential points).
* The tone should be extremely concise: focus only on the main line, with no detail expansion.

**Output requirements:**

1. The summary length should be about **2–5%** of the original (estimate the compression ratio yourself; prefer shorter over too detailed).

2. You must cover and output the following sections **in this exact order** (each section 1–2 sentences or a very small number of bullets):

   * **Purpose & Scope**: the core problem the system solves and its boundaries.
   * **Core Functions**: list only the **3–5 most critical capability-level functions**.
   * **Key Users**: main user types.
   * **Key Constraints**: hard constraints that affect success.

3. **Content selection rules:**

   * Summarize only the points that are **most explicit, most stable, and most globally impactful** in the original.
   * For unclear, missing, or self-contradictory parts of the original: **do not write them, do not guess, do not fill in**.

4. The language must be **accurate, unambiguous, and verifiable**. Avoid non-measurable words like "easy to use," "fast," "as much as possible." If they occur, rewrite into verifiable statements; if you cannot, skip them.

5. Do not describe implementation plans or design details; summarize requirements and constraints only.

6. **Output only the summary body** (organized by the sections above). **Do not add any explanations, notes, prefaces, afterwords, or meta-commentary.**

7. The summary must **not include any source mentions, section numbers, requirement IDs, or any similar citation markers.**

**SRS text:**
{srs_text}



