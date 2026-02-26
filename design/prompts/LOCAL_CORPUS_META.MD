# Local Corpus Meta-Prompt
This document serves as the design specification and implementation logic for the `LOCAL_CORPUS.MD` skill.

## Objective
Enable users to transform a local directory of documents (PDF, TXT, MD, etc.) into a structured **Mystic Corpus**, utilizing the **Antigravity** to distill the "Vibe" and essence of the collection.

## 1. The Onboarding Interview
Before indexing, the **Antigravity** (from `skills/DreamBridge/DIM.MD`) must interview the user about their collection.

- **The Question**: "I see you have brought a collection of scrolls from your world. If I were to look inside these boxes without knowing your language, what would the *feeling* of this collection be? Is it a 'Golden Treasury' of wisdom, or a 'Dark Archive' of secrets?"
- **Goal**: Establish the metadata "tone" and the `corpus_name` alias.

## 2. Technical Implementation
The `LOCAL_CORPUS.MD` skill must follow the [CORPUS_STRUCTURE.MD](skills/CORPUS_STRUCTURE.MD) strictly.

### Implementation Steps:
1.  **Scan and Map**: Identify all documents in the target folder.
2.  **Convert and Clean**: Use local tools to convert non-markdown files (PDF, DOCX) to clean Markdown.
3.  **Index Creation**: Generate the `index.json` with sequential IDs and appropriate metadata.
4.  **Verification**: Run `tools/verify_corpus.py --name [alias]` to ensure integrity.

## 3. Associated Skill
The output of this meta-prompt is implemented in the [LOCAL_CORPUS.MD](skills/LOCAL_CORPUS.MD) skill.

## 4. Visual Synthesis
Each new local corpus creation concludes with a visual representation of the collection:
> "[DALL-E Prompt for a 'Library of Infinite Possibility' style image, themed based on the Antigravity's findings (e.g., 'A bioluminescent archive of bioluminescent spores' or 'A weathered clockwork vault of forgotten blueprints')]"