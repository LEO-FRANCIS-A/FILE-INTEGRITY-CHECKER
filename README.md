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
