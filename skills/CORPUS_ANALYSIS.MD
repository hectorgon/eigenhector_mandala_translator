# Corpus Analysis Guidelines

This corpus skill can be used to quickily understand how a mystic talks about different subjects.

## Corpus Structure

Read the corpus structure document for more information: **@[skills/CORPUS_STRUCTURE.MD]**

## Corpus Acquisition

Before starting analysis, ensure you have the target corpus available.

1.  **Import Content:** Use the **@[skills/LOCAL_CORPUS.MD]** skill to import an existing directory.
    -   Example: `python tools/import_corpus.py --source "C:\path\to\docs" --alias example_corpus`

2.  **Verify Integrity:** Run the verification tool to ensure the corpus is complete and valid.
    -   Command: `python tools/verify_corpus.py --name <corpus_name>`
    -   Example: `python tools/verify_corpus.py --name eigenhector`

The imported corpus will be stored in:
`reports/mystic_corpus/<corpus_name>/docs` (e.g., `reports/mystic_corpus/eigenhector/docs`)
Each file will be a Markdown document containing a single post or article.

> [!IMPORTANT]
> **Batch Processing**: When starting an analysis, ask the user for permission to read the entire batch of corpus documents at once. Once the user confirms "batch access", you may proceed to read all files in the directory without asking for permission for each individual file.


## General Corpus Patterns
When analyzing a corpus, you should look for the following patterns to generate a full synthesis including:

- The top 10-15 major recurring metaphors with characteristic adjectives, feelings, and exact quotes for each
- The overall emotional texture
- Lineages drawn upon
- Recurring themes
- Key concepts
- Important terms
- Relationships between concepts
- Evolution of ideas over time
- Connections to other fields or traditions
- Unique insights or perspectives
- Any patterns that seem particularly interesting or relevant to the task at hand

## The Lineage Researcher Perspective (Graph-Manifold)

When analyzing a corpus, adopt the **@[skills/LINEAGE_RESEARCH.MD]** persona to map the topological boundaries of the author's "Self".

### 1. Citation Graph Mapping
Look for silent co-authors and anchor traditions.
- **k-Hop Clique Identification**: Determine the distance between the author and their sources. Are they at $k=1$ (direct student) or $k=3$ (interpreting an interpretation)?
- **Anchor Traditions**: Identify the "Root Nodes" (e.g., Tantra, Graph Theory, Hermeticism) that the author resonates with.

### 2. The Discrete-Smooth Flip
Identify where the author moves between rigid logic and smooth experience.
- **Vietoris-Rips Invocation**: How does the author use language (graphs) to trigger a state-flip in the reader?
- **Catharsis Release**: Note the specific concepts or metaphors that seem to release the most "energy" or emotional clarity—this is where the "Flip" is occurring.
- **Nyam Reification**: How does the author "package" their mystical experiences into usable metaphors or instructions?

## Dream Bridge Analysis Method (DIM)

The Dream Interview Method (DIM) is a specific technique for comparing metaphors across parallel corpora. It accepts the **structured JSON analysis** of two target corpora as input and synthesizes them. It treats text segments as "dream images" to reveal unique, culturally specific meanings.

### Phase 1: The Setup (Antigravity Perspective)
Adopt the persona of a **Antigravity** who knows nothing about Earth customs or symbols. Prevent projecting your own definitions onto the text. Elicit meaning entirely from the text's own descriptions.

### Phase 2: The Interview Process
For each target metaphor in each corpus:

1.  **Description (The "Alien" Inquiry):**
    - Ask: "What is [Metaphor] like?"
    - Elicit 3-4 specific adjectives and feelings distinct to this text (e.g., is the "Forest" *dark/suffocating* or *green/resource-rich*?).

2.  **Recapitulation (Mirroring):**
    - Summarize the description back using **only the text's exact words**.
    - Confirm the specific tone.

3.  **Reflective Bridge (Contextualization):**
    - Ask: "Is there any situation, argument, or theme in this text that is **like** [Recapitulation]?"
    - Connect the image to the broader reality or argument of the text (the "waking life" of the corpus).

### Phase 3: Crossing the Dream Bridge
Compare the findings from Corpus A and Corpus B:
-   **Compare Adjectives/Feelings:** How do the specific textures differ?
-   **Compare Bridges:** How do the functional metaphors differ? (e.g., Internal state vs. External event).

## Structural Comparison Dimensions

In addition to metaphor analysis, compare the corpora along these structural dimensions:

1.  **Rhetorical Mode:** Style, tone, genre, typical references.
2.  **Emotional Register:** Dominant mood, feeling-tone, emotional signature.
3.  **Direction of Attention:** Inward/Outward, Up/Down, Micro/Macro.
4.  **Relationship to the Reader:** Teacher, friend, oracle, diarist, etc.
5.  **Core Verb:** One word that captures the central activity of the corpus.

## Output Standards

All analysis artifacts must be saved in the dedicated analysis directory:
`reports/mystic_corpus/<corpus_name>/analysis/`
(e.g., `reports/mystic_corpus/eigenhector/analysis/`)

To ensure the analysis is both human-readable and machine-processable for downstream tasks (like the Dream Bridge), you must generate **two** output files for every analysis within this directory.

### 1. Human-Readable Output (HTML)
**Purpose:** For human review and simplified reading.
**Location:** `reports/mystic_corpus/<corpus_name>/analysis/<corpus_name>_analysis_<YYYYMMDD>.html`
**Format:**
-   **Structure:** Standard HTML5.
-   **Style:** Clean, minimal CSS (e.g., sans-serif fonts, clear headers, distinct sections for metaphors).
-   **Content:**
    -   **Metadata Header:** Corpus name, author, date.
    -   **Executive Summary:** High-level synthesis.
    -   **Metaphors Section:** Each metaphor clearly displayed with its description, recapitulation, and bridge.
    -   **Structural Dimensions:** Formatted as a readable list or table.
    -   **Key Concepts:** Definitions list.
    -   **Evolution of Ideas:** Narrative text.

### 2. Machine-Readable Output (JSON)
**Purpose:** To serve as input for `skills/DREAM_BRIDGE_TEMPLATE.MD` and other agentic tasks.
**Location:** `reports/mystic_corpus/<corpus_name>/analysis/<corpus_name>_analysis_<YYYYMMDD>.json`
**Format:**
-   **Strict Schema:** Must strictly follow the structure defined in `skills/ANALYSIS_JSON_TEMPLATE.json`.
-   **Fields Required:**
    -   `corpus_metadata` (including `local_corpus_path`)
    -   `major_recurring_metaphors` (Array of objects, must include `occurrences` list with quotes and `source_document` paths)
    -   `structural_dimensions`
    -   `key_concepts` (Array of objects, must include `occurrences` list with `source_document` paths)
    -   `evolution_of_ideas`
