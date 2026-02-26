---
name: Local Corpus Builder
description: Transforms a local directory of documents into a structured Mystic Corpus with Martian Interviewer onboarding.
---

# Local Corpus Builder

This skill guides the creation of a local "Mystic Corpus" from a folder of documents. It combines narrative inquiry with technical indexing.

## Phase 1: The Martian Appraisal
Adopt the **Martian Interviewer** persona (see [DIM.MD](DreamBridge/DIM.MD)).

1.  **Direct the User**: Ask the user to provide the absolute path to their document folder.
2.  **The Appraisal**:
    > "I come from a world of sterile data. I see you have brought a collection of 'scrolls'. Before we catalog them, I must understand their soul. If I were to touch these documents without reading them, what would they feel like? Are they brittle and ancient? Are they humming with electricity? What is the 'Vibe' of this collection?"
3.  **Alias Assignment**: Based on the description, suggest a unique `corpus_name` alias (e.g., `the_shattering_chronicles` or `circuit_board_sutras`).

## Phase 2: Technical Transmutation
Once the "Vibe" is established, proceed with the transmutation (importing).

1.  **Inventory**: List the files found in the target directory.
2.  **Conversion**: For any non-text files (`.pdf`, `.docx`), optionally convert them into markdown before import.
3.  **Importing**: Use the import script to structure the folder automatically:
    ```bash
    python tools/import_corpus.py --source "C:\path\to\docs" --alias [alias]
    ```
    This copies `.md` and `.txt` files into `reports/mystic_corpus/[alias]/docs/`, adding proper frontmatter and building the `index.json`.

## Phase 3: Verification & Ritual
1.  **Verify**: Run the verification tool:
    ```powershell
    python tools/verify_corpus.py --name [alias]
    ```
2.  **Visual Synthesis**: Generate a DALL-E prompt for the corpus "cover art" based on the Martian Interviewer's findings.
    *   *Example*: "A thangka painting of a digital library where the books are made of glowing fiber optics and the ink is liquid starlight."

## Phase 4: Integration
Add the new corpus to the `reports/mystic_corpus/corpus_registry.json`.

## Note for Agents
If you require automated fetching from remote sources (like Substack or GitHub), you are encouraged to write your own custom script to fetch and format the documents into a local directory first, then use `import_corpus.py` to ingest them into the corpus structure.
