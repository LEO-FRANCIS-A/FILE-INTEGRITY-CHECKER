import hashlib
import os
import json
import sys

Hash_Storage = 'hashes.json'  


def get_file_hash(file_path):
    #Calculate and return the SHA256 hash of a file
    hasher = hashlib.sha256()

    try:
        with open(file_path, 'rb') as file:
            while data_chunk := file.read(4096):
                hasher.update(data_chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def save_all_file_hashes(path_to_scan):
    #Save the hashes of all files in a directory
    file_hashes = {}

    if os.path.isfile(path_to_scan):
        file_hash = get_file_hash(path_to_scan)
        if file_hash:
            file_hashes[path_to_scan] = file_hash
    else:
        for folder_path, _, file_names in os.walk(path_to_scan):
            for file_name in file_names:
                full_path = os.path.join(folder_path, file_name)
                file_hash = get_file_hash(full_path)
                if file_hash:
                    file_hashes[full_path] = file_hash

    with open(Hash_Storage, 'w') as storage:
        json.dump(file_hashes, storage, indent=2)

    print(f"Hashes saved in '{Hash_Storage}'.")


def verify_file_integrity(path_to_check):
    #Check if files have changed by comparing with saved hashes
    if not os.path.exists(Hash_Storage):
        print("No saved hash file found. Please run with 'store' mode first.")
        return

    with open(Hash_Storage, 'r') as storage:
        saved_hashes = json.load(storage)

    current_files = []

    if os.path.isfile(path_to_check):
        current_files.append(path_to_check)
    else:
        for folder_path, _, file_names in os.walk(path_to_check):
            for file_name in file_names:
                current_files.append(os.path.join(folder_path, file_name))

    for current_file in current_files:
        current_hash = get_file_hash(current_file)
        original_hash = saved_hashes.get(current_file)

        if original_hash is None:
            print(f"NEW FILE: {current_file} was not in the saved list.")
        elif current_hash != original_hash:
            print(f"CHANGED: {current_file} has been modified.")
        else:
            print(f"OK: {current_file} has not changed.")

    for recorded_file in saved_hashes:
        if recorded_file not in current_files and not os.path.exists(recorded_file):
            print(f"MISSING: {recorded_file} has been deleted or moved.")


def main():
    if len(sys.argv) != 3:
        print("Try: python checker.py [store | check] [path_to_file_or_folder]")
        return

    user_action = sys.argv[1].lower()
    user_path = sys.argv[2]

    if user_action == 'store':
        save_all_file_hashes(user_path)
    elif user_action == 'check':
        verify_file_integrity(user_path)
    else:
        print("Invalid action. Use 'store' to save hashes or 'check' to verify files.")


if __name__ == '__main__':
    main()
