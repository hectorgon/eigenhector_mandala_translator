# Adding Users to the Corpus Registry

This skill outlines the process for registering new user aliases in the corpus registry.

## Overview
The **Corpus Registry** is a JSON configuration file that maps short, user-friendly aliases to specific corpus metadata.

## Configuration File Location
*   **Path:** `mystic_corpus/corpus_registry.json`
*   **Exact Location:** Inside the user's `mystic_corpus` directory (e.g., `%USERPROFILE%\Documents\mystic_corpus\` on Windows or `~/Documents/mystic_corpus/` on Linux).

## JSON Structure
The registry is a JSON object where update keys are aliases and values are source definitions.

### Entry Format
Each user entry requires the following fields:
*   `type`: The source type (e.g., `local`).
*   `url`: The original source URL or path.
*   `description`: A brief description of the corpus.

### Example Configuration
```json
{
  "ari": {
    "type": "local",
    "url": "local://path/to/ari/docs",
    "description": "Ari's corpus"
  },
  "hector": {
    "type": "local",
    "url": "local://path/to/hector/docs",
    "description": "Hector's Local Repo"
  }
}
```

## Step-by-Step Instructions

1.  **Locate the File:** Navigate to your `mystic_corpus` directory. If `corpus_registry.json` does not exist, create it.
2.  **Open in Editor:** Open the file in a text editor or IDE.
3.  **Add Entry:** Insert a new key-value pair for the desired user alias. Ensure the JSON syntax is valid (commas between entries).
4.  **Save:** Save and close the file.

## Verification
To verify the new user has been added correctly, check that `index.json` is generated properly for that corpus via `verify_corpus.py`:

```bash
python tools/verify_corpus.py --name <new_alias>
```

If the tool runs correctly and reports on the corpus size, configuration is successful.
