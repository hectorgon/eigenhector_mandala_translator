import os
import argparse
import json
import sys
from datetime import datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corpus_config

class CorpusVerifier:
    def __init__(self, corpus_name, storage_root=None):
        self.corpus_name = corpus_name
        if storage_root:
             self.base_dir = storage_root
        else:
            self.base_dir = corpus_config.get_base_dir()
        
        self.corpus_dir = os.path.join(self.base_dir, self.corpus_name)
        self.docs_dir = os.path.join(self.corpus_dir, 'docs')
        self.index_path = os.path.join(self.corpus_dir, 'index.json')
        self.issues = []

    def verify(self):
        print(f"Verifying corpus: {self.corpus_name}")
        print(f"Path: {self.corpus_dir}")
        
        if not os.path.exists(self.corpus_dir):
            print(f"Error: Corpus directory not found: {self.corpus_dir}")
            return False

        if not os.path.exists(self.index_path):
            self.issues.append("Missing index.json")
            print("Error: index.json not found.")
        
        if not os.path.exists(self.docs_dir):
            self.issues.append("Missing docs directory")
            print("Error: docs directory not found.")
            return False

        index_entries = []
        if os.path.exists(self.index_path):
            try:
                with open(self.index_path, 'r', encoding='utf-8') as f:
                    index_entries = json.load(f)
            except json.JSONDecodeError:
                self.issues.append("Invalid JSON in index.json")
                print("Error: index.json is not valid JSON.")
                return False

        docs_files = set(f for f in os.listdir(self.docs_dir) if f.endswith('.md'))
        index_files = set(os.path.basename(entry.get('filepath', '')) for entry in index_entries)
        
        # Check 1: Files in index but not on disk
        missing_on_disk = index_files - docs_files
        if missing_on_disk:
            count = len(missing_on_disk)
            self.issues.append(f"{count} files listed in index but missing from docs/")
            print(f"Warning: {count} entries in index are missing files on disk.")
            if count < 10:
                for f in missing_on_disk:
                    print(f"  - Missing: {f}")

        # Check 2: Files on disk but not in index (Orphans)
        orphans = docs_files - index_files
        if orphans:
            count = len(orphans)
            self.issues.append(f"{count} orphan files in docs/ (not in index)")
            print(f"Warning: {count} files in docs/ are not in index.json.")
            if count < 10:
                for f in orphans:
                    print(f"  - Orphan: {f}")

        # Check 3: Content validity (basic)
        empty_files = []
        for filename in docs_files:
            filepath = os.path.join(self.docs_dir, filename)
            if os.path.getsize(filepath) == 0:
                empty_files.append(filename)
        
        if empty_files:
            self.issues.append(f"{len(empty_files)} empty files found")
            print(f"Warning: {len(empty_files)} files are empty.")

        # Stats
        print("\n--- Corpus Statistics ---")
        print(f"Total entries in index: {len(index_entries)}")
        print(f"Total files in docs/: {len(docs_files)}")
        
        if not self.issues:
            print("\n✅ Corpus Verification PASSED")
            return True
        else:
            print("\n⚠️ Corpus Verification COMPLETED WITH ISSUES")
            for issue in self.issues:
                print(f"  - {issue}")
            return False

def load_registry(storage_root=None):
    if storage_root:
        base_dir = storage_root
    else:
        base_dir = corpus_config.get_base_dir()
            
    registry_path = corpus_config.get_registry_path(base_dir)
    if os.path.exists(registry_path):
        with open(registry_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def main():
    parser = argparse.ArgumentParser(description="Verify the integrity of a fetched corpus.")
    parser.add_argument('--name', help="Name of the corpus or user alias")
    parser.add_argument('--storage-root', help="Override default storage root")
    
    args = parser.parse_args()
    
    if not args.name:
        parser.error("The --name argument is required.")
        
    # Check if name is an alias in registry
    registry = load_registry(args.storage_root)
    corpus_name = args.name
    
    # If the name exists in registry, use it (it might map to a different folder structure in future, 
    # but for now registry keys are treated as corpus names).
    # So if user passes 'eigenhector', it's key in registry.
    
    verifier = CorpusVerifier(corpus_name, args.storage_root)
    verifier.verify()

if __name__ == "__main__":
    main()
