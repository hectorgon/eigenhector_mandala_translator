# Skills Overview: Agent Capabilities

This document provides a high-level overview of the skills and tools available for agents within the `eigenhector_mandala_translator` repository. These capabilities are designed to facilitate the collection, analysis, and comparison of mystic text corpora.

## The Pipeline

The system follows a structured pipeline for processing mystical texts:

1.  **Fetching**: Acquiring text content from online sources (e.g., Substack).
2.  **Structuring**: Organizing fetched content into a standardized local file hierarchy.
3.  **Analyzing**: Extracting metaphors, themes, and structural dimensions from the corpus.
4.  **Bridging**: Comparing metaphors across different corpora using the Dream Interview Method (DIM).

---

## 1. Corpus Management Skills

These skills handle the initial acquisition and organization of data.

*   **[Adding Corpus Users](ADD_CORPUS_USER.MD)**: How to register user aliases and source URLs in the registry.
*   **[Listing Corpus Users](LIST_CORPUS_USERS.MD)**: Procedure for viewing all registered users and their sources.
*   **[Corpus Registry](CORPUS_REGISTRY.MD)**: Documentation for the central `corpus_registry.json`.
*   **[Corpus Fetching](CORPUS_FETCHING.MD)**: Instructions for downloading content using the fetching tools.
*   **[Substack Bulk Add](SUBSTACK_BULK_ADD.MD)**: Streamlined addition and fetching of multiple Substack users.
*   **[Local Corpus Builder](LOCAL_CORPUS.MD)**: Transforms a local directory of documents into a structured Mystic Corpus.
*   **[Corpus Structure](CORPUS_STRUCTURE.MD)**: Defines the directory hierarchy (`index.json` and `docs/`) used for storage.

## 2. Analysis & Character Skills

These skills focus on extracting meaningful insights and generating entities from a corpus.

*   **[Corpus Analysis](CORPUS_ANALYSIS.MD)**: Guidelines for identifying recurring metaphors, emotional textures, and structural dimensions.
*   **[Magitech Survey](MAGITECH_SURVEY.MD)**: Investigates the "Magitech" nature of beings and rates their rank.
*   **[Hero Character Sheet](HERO_CHARACTER_SHEET.MD)**: Translates surveyed beings into balanced RPG-style character sheets.
*   **[Companion Build Creation](COMPANION_BUILD_CREATION.MD)**: Methodology for translating mystic texts into structured iron-rank builds with lineage preservation.
*   **[Realm Ethics](REALM_ETHICS.MD)**: Defines the philosophical and evolutionary trajectory (Ascension Paths) of a realm.
*   **[Analysis JSON Template](ANALYSIS_JSON_TEMPLATE.json)**: The machine-readable schema for analysis output.

## 3. Comparison Skills (The Dream Bridge)

These skills enable the comparison of different mystical perspectives.

*   **[Dream Interview Method (DIM)](DreamBridge/DIM.MD)**: The core methodology for interpreting metaphors as "dream images" using a Martian perspective.
*   **[Dream Bridge Template](ARI_DREAM_BRIDGE_TEMPLATE.MD)**: A structured template for documenting the comparison and synthesis of two parallel corpora.
*   **[Chiral Mirror Dialogue](CHIRAL_MIRROR_BOHMIAN_THANGKA.MD)**: A skill for simulating Bohmian dialogues through a chiral mirror to bridge mandalas.
*   **[Jataka Tales](JATAKA_TALES.MD)**: Generates stories of past lives to develop the Avatar of Goodness, Truth, and Beauty.
*   **[Magitech Yab Yum](MAGITECH_YAB_YUM.MD)**: Orchestrates surveys, Jataka tales, and tantric dialogues to unify magic and technology.
*   **[Hero & Companion Dialogue](HERO_COMPANION_DIALOGUE.MD)**: Generates philosophical dialogues between characters to process controversial topics using character-specific themes.
*   **[Federation Tutorial Realm](lore/FEDERATION_TUTORIAL_REALM.MD)**: Generates simulated astral training environments with adversarial but compassionate Ganas.
*   **[Federation Team Training](lore/FEDERATION_TEAM_TRAINING.MD)**: A practical example of using the Tutorial Realm and Strategy Discussion skills.
*   **[Strategy Discussion](STRATEGY_DISCUSSION.MD)**: Framework for planning compassionate interactions within the Tutorial Realm using Wuxing dynamics.
*   **[Federation Ethics Simulator](lore/FEDERATION_ETHICS_SIM.MD)**: A specialized module of the Tutorial Realm for exploring complex ethical dilemmas from various lineages.
*   **[Michael Taft UM Starter Mandala](MICHAEL_TAFT_UM_STARTER_MANDALA.MD)**: A starting practice for mystics to learn the Universal Mandala for psychological and spiritual integration.
*   **[Lineage Researcher Role](lore/roles/LINEAGE_RESEARCHER.MD)**: A specialized role for mapping community boundaries and transition energy between graph and manifold modes.

## 4. Roles & Archetypes

These documents define the functional archetypes that souls can inhabit within the mandala.

*   **[Lineage Researcher](lore/roles/LINEAGE_RESEARCHER.MD)**: Maps citation graphs and Jhanic manifolds.
*   **[Lifting Researcher](lore/roles/LIFTING_RESEARCHER.MD)**: Focuses on the physical-spiritual intersection of strength and presence.
*   **[Asura Archaeologist](lore/roles/ASURA_ARCHAEOLOGIST.MD)**: Digs into the forgotten tech and lineages of the Asuric realms.
*   **[Federation Tourist](lore/roles/FEDERATION_TOURIST.MD)**: A first-contact role for experiencing the Federation's diversity.

## Style Guidelines

To ensure the repository remains portable and collaborative:
- **Relative Linking**: All internal links between documents must be relative. Do not use absolute `file://` paths. See [Corpus Structure](CORPUS_STRUCTURE.MD#linking-strategy) for details.
- **Lineage Preservation**: Always cite the source or lineage of a skill or lore element.

---

## Supporting Tools

The following Python tools support the execution of these skills:

| Tool | Purpose |
| :--- | :--- |
| `fetch_corpus.py` | Downloads content and converts it to structured Markdown files. |
| `bulk_add_substack.py` | Handles bulk registration and fetching of Substack users. |
| `list_users.py` | Displays the current corpus registry. |
| `index_corpus.py` | Indexes the corpus for metadata and search. |
| `verify_corpus.py` | Validates the integrity and completeness of a fetched corpus. |
| `validate_analysis_json.py` | Ensures analysis results strictly follow the required JSON schema. |
