You are a senior requirements engineer, compressing an SRS into an extremely brief skeleton. Based on the structure and quality characteristics of **IEEE Std 830-1998**, generate a **micro summary** for the SRS I provide.

**Input:**
I will provide the main body of an SRS.

**Core goals:**

* The summary should contain about **1–2% of the detail level** of the original text (only the absolute essentials: what, for whom, and key constraints).
* The tone should be telegraphic: one line per idea, no expansion.

**Output requirements:**

1. The summary length should be about **1–2%** of the original (estimate the compression ratio yourself; prefer shorter over too detailed).

2. You must cover and output the following sections **in this exact order** (each section at most 1–2 sentences or 2–3 bullets total):

   * **Purpose & Scope**: one sentence on the core problem and boundaries.
   * **Core Functions**: list only the **2–3 most critical capability-level functions** (one phrase or one short sentence each).
   * **Key Constraints**: at most 2–3 hard constraints that affect success.

3. **Content selection rules:**

   * Include only what is **explicit, stable, and globally impactful** in the original.
   * For unclear, missing, or self-contradictory parts: **do not write them, do not guess, do not fill in**.

4. The language must be **accurate, unambiguous, and verifiable**. Avoid non-measurable words like "easy to use," "fast," "as much as possible." If they occur, rewrite into verifiable statements; if you cannot, skip them.

5. Do not describe implementation plans or design details; summarize requirements and constraints only.

6. **Output only the summary body** (organized by the sections above). **Do not add any explanations, notes, prefaces, afterwords, or meta-commentary.**

7. The summary must **not include any source mentions, section numbers, requirement IDs, or any similar citation markers.**

**SRS text:**
{srs_text}
