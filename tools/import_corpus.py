import os
import sys
import argparse
import json
import shutil
import datetime
from pathlib import Path

# Add the tools directory to the path so we can import corpus_config
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus_config import get_base_dir

def setup_argparse():
    parser = argparse.ArgumentParser(description="Import a local directory of documents into the mystic corpus.")
    parser.add_argument("--source", required=True, help="Absolute path to the source directory containing documents.")
    parser.add_argument("--alias", required=True, help="Alias for the new corpus (e.g., 'the_shattering_chronicles').")
    return parser.parse_args()

def main():
    args = setup_argparse()
    source_dir = Path(args.source)
    alias = args.alias

    if not source_dir.is_dir():
        print(f"Error: Source directory {source_dir} does not exist or is not a directory.")
        sys.exit(1)
        
    base_dir = Path(get_base_dir())
    corpus_dir = base_dir / alias
    docs_dir = corpus_dir / "docs"
    
    # Create directories if they don't exist
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    index_path = corpus_dir / "index.json"
    index_data = []
    
    if index_path.exists():
        with open(index_path, "r", encoding="utf-8") as f:
            try:
                index_data = json.load(f)
                if not isinstance(index_data, list):
                    # Fallback if somehow it's a dict
                    index_data = list(index_data.values()) if isinstance(index_data, dict) else []
            except json.JSONDecodeError:
                pass

    current_id = 1
    if index_data:
        try:
            current_id = max(int(entry.get("id", 0)) for entry in index_data) + 1
        except ValueError:
            current_id = len(index_data) + 1
            
    # Inventory
    files = list(source_dir.glob("*"))
    print(f"Found {len(files)} files in {source_dir}")
    
    for file_path in files:
        if not file_path.is_file():
            continue
            
        if file_path.suffix.lower() not in [".md", ".txt"]:
            print(f"Skipping {file_path.name} (unsupported extension).")
            continue
            
        print(f"Processing {file_path.name}...")
        
        # Read content
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, "r", encoding="latin-1") as f:
                    content = f.read()
            except Exception as e:
                print(f"Failed to read {file_path.name} encoding: {e}")
                continue

        # Get file date
        stat = file_path.stat()
        file_date = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d")
        
        doc_id_str = f"{current_id:05d}"
        dest_filename = f"{doc_id_str}.md"
        dest_path = docs_dir / dest_filename
        
        title = file_path.stem
        # Ensure it's treated as a local path
        local_url = f"local://{file_path.absolute().as_posix()}"
        
        # Frontmatter synthesis
        frontmatter = f"---\nid: {current_id}\ntitle: {title}\ndate: {file_date}\nurl: {local_url}\n---\n\n"
        
        final_content = frontmatter + content
        
        with open(dest_path, "w", encoding="utf-8", errors="replace") as f:
            f.write(final_content)
            
        # Update index mapping
        index_data.append({
            "id": current_id,
            "title": title,
            "url": local_url,
            "date": file_date,
            "filepath": dest_path.as_posix()
        })
        
        current_id += 1

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=4)
        
    print(f"Successfully imported corpus '{alias}' to {corpus_dir.as_posix()}")
    print(f"Run 'python tools/verify_corpus.py --name {alias}' to verify.")

if __name__ == '__main__':
    main()
