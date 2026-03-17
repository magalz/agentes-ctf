#!/usr/bin/env python3
"""
List CTFs - CTF Professor
=========================
Lists all challenge folders in CTFs/ and provides a quick summary.
"""

import os
from pathlib import Path

def list_ctfs():
    ctfs_dir = Path("CTFs")
    if not ctfs_dir.exists():
        print("Directory 'CTFs/' not found.")
        return

    folders = [f for f in ctfs_dir.iterdir() if f.is_dir()]
    if not folders:
        print("No challenges found in 'CTFs/'.")
        return

    print(f"\n{'Challenge Name':<25} | {'Artifacts':<10} | {'Status':<15} | {'Flag'}")
    print("-" * 75)

    for folder in folders:
        files = list(folder.iterdir())
        artifact_count = len([f for f in files if f.is_file()])
        
        # Check for flags or notes
        flag_content = "-"
        has_flag = False
        
        for f in files:
            if "flag" in f.name.lower() and f.is_file():
                has_flag = True
                try:
                    content = f.read_text(encoding='utf-8').strip()
                    # Truncate flag if too long
                    flag_content = content[:20] + "..." if len(content) > 20 else content
                except:
                    flag_content = "[Binary/Unreadable]"
                break
                
        has_notes = (folder / "notes.md").exists()
        
        status = "🆕 New"
        if has_notes:
            status = "⏳ In Progress"
        if has_flag:
            status = "🏁 Solved"

        print(f"{folder.name:<25} | {artifact_count:<10} | {status:<15} | {flag_content}")
    print()

if __name__ == "__main__":
    list_ctfs()
