# FILE-INTEGRITY-CHECKER

 *COMPANY*: CODTECH IT SOLUTIONS

 *NAME*: LEO FRANCIS A

 *INTERN ID*: CT04DM1437 

 *DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

 *DURATION*: 4 WEEKS

 *MENTOR*: NEELA SANTOSH


File Integrity Checker

A simple Python-based tool to monitor and verify the integrity of files by generating and comparing SHA-256 hashes. This script helps detect if any file in a specified directory has been modified, deleted, or newly added. It’s lightweight, beginner-friendly, and works right from your terminal.
--> Tools & Technologies

    Language: Python 3

    Libraries Used: hashlib, os, json, sys

    Platform: Ubuntu Terminal

    Editor: Sublime Text

    Version Control: Git & GitHub

--> How It Works

    Store Mode
    --> Save the current state (hashes) of all files in a folder
         
         python3 checker.py store /path/to/folder

    Check Mode
    --> Compare current file hashes with previously stored values:

         python3 checker.py check /path/to/folder

    Based on the comparison, you’ll see output like:

    --> OK: File unchanged

    --> CHANGED: File has been modified

    --> MISSING: File was deleted or moved

    --> NEW FILE: File wasn't present during original scan

--> Hashes.json
    This file is created automatically in store mode. It acts as a snapshot of your files at a specific point in time, storing each file’s SHA-256 hash.

    Example:

    {
       "test/leo.txt": "0d35eff369a74254d4f09daab428a3f1d3425d06c2e6206050882ee54ad618f1"
    }

    Key: Path to the file
    Value: SHA-256 hash of the file’s contents

    In check mode, the script loads this file and compares the saved hashes against the current ones to detect any changes.

OUTPUT SCREENSHOTS:
--> HASHES STORED
    This shows the output after running the script in store mode. It indicates that all file hashes have been saved into hashes.json
    https://github.com/LEO-FRANCIS-A/FILE-INTEGRITY-CHECKER/issues/1#issue-3149832648

--> UNCHANGED FILE
    
