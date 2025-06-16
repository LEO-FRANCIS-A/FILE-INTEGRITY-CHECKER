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

HASHES STORED
--> This shows the output after running the script in store mode. It indicates that all file hashes have been saved into hashes.json
    
![Image](https://github.com/user-attachments/assets/7f40e159-ab67-4940-b873-406eac0f0854)

UNCHANGED FILE
--> This shows an example of a file that has not changed since the last scan. The current hash matches the stored hash
    
![Image](https://github.com/user-attachments/assets/0c6ce6cb-5cdb-474c-994e-1903ff35b0d5)

FILE MODIFIED
--> Indicates that the contents of a file have been altered. The hash no longer matches the one stored in hashes.json
    
![Image](https://github.com/user-attachments/assets/c2d396fc-ed8e-4fce-91a1-1204ea2ef24e)

--> FILE MISSING
    This file was present during the initial hash storage but is now missing or has been moved.
    https://github.com/LEO-FRANCIS-A/FILE-INTEGRITY-CHECKER/issues/1#issuecomment-2976488604

NEW FILE DETECTED
--> A new file that wasn't present during the original store operation is now detected during the check phase
    
![Image](https://github.com/user-attachments/assets/f6c77690-96c1-442e-9283-aee3fcfc0dc4)
