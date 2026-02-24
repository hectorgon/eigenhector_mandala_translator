---
name: Corpus Structure
description: Defines the directory hierarchy and file formats for the mystic_corpus.
---

# Corpus Structure

This document defines the standard file structure and data formats for the `mystic_corpus` managed by the `fetch_corpus.py` tool.

## Directory Hierarchy

The corpus storage is organized by **Corpus Name**.

```text
reports/mystic_corpus/
├── corpus_registry.json        # Global registry of user aliases
└── [corpus_name]/              # Directory for a specific corpus (e.g., 'eigenhector')
    ├── index.json              # Metadata index for all fetched documents
    └── docs/                   # Directory containing the actual content files
        ├── 00001.md
        ├── 00002.md
        └── ...
```

*   **`reports/mystic_corpus/`**: The root directory, located in the project's `reports/` folder.
    - > [!IMPORTANT]
    - > The `reports/` folder should always be added to `.gitignore`.
*   **`[corpus_name]/`**: A dedicated folder for each corpus. The name usually matches the user alias or the `--name` argument used during fetching.
*   **`docs/`**: Contains the Markdown files. Files are named sequentially using a 5-digit zero-padded ID (e.g., `00001.md`).

## Index Format (`index.json`)

The `index.json` file contains an array of metadata objects, one for each fetched document. It serves as a fast lookup database without needing to parse every Markdown file.

### Schema within `index.json`

```json
[
  {
    "id": 1,
    "title": "Article Title",
    "url": "https://example.com/article",
    "date": "2023-10-27",
    "filepath": "reports/mystic_corpus/corpus_name/docs/00001.md"
  }
]
```

*   **`id`**: Integer. Unique identifier for the document within this corpus. Matches the filename.
*   **`title`**: String. The title of the article or post.
*   **`url`**: String. The source URL.
*   **`date`**: String. Date of the article (format: `YYYY-MM-DD`).
*   **`filepath`**: String. Absolute path to the file on the local disk.

## Document Format (`docs/*.md`)

Each document is a Markdown file containing Frontmatter and the Body content.

### File Naming
*   Format: `00001.md`, `00002.md`, etc.
*   The filename corresponds directly to the `id` in `index.json`.

### Content Structure

```markdown
---
id: 1
title: Article Title
date: 2023-10-27
url: https://example.com/article
---

# Article Title

## Linking Strategy

To ensure repositories can be easily cloned and remain functional across different environments (or "realms"), all internal links must use **relative paths** instead of absolute `file://` URIs.

### Guidelines
- **Always use relative paths**: Links should be relative to the current file or the repository root.
- **Avoid `file:///`**: These paths are specific to your local machine and will fail for others.

### Examples
| Type | Path Format | Example |
| :--- | :--- | :--- |
| **Absolute (Avoid)** | `file:///C:/Users/.../skills/DIM.MD` | `[DIM](file:///C:/Users/...)` |
| **Relative (Preferred)** | `../DreamBridge/DIM.MD` | `[DIM](../DreamBridge/DIM.MD)` |
| **Root-Relative** | `/skills/DreamBridge/DIM.MD` | `[DIM](/skills/DreamBridge/DIM.MD)` |

> [!TIP]
> When creating new lore or skill documents, verify that all back-links to other documents in the repository are relative.

*   **Frontmatter**: YAML block between `---` separators. Contains metadata redundant with `index.json` for self-containment.
*   **Body**: The converted Markdown content of the web page or source file.
