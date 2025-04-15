import os
import argparse
from pathlib import Path

def delete_ds_store(ds_dir):
    """Recursively deletes .DS_Store files within a directory."""
    for root, _, files in os.walk(ds_dir):
        for file in files:
            if file == ".DS_Store":
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Delete .DS_Store files from a directory')
    parser.add_argument('directory', nargs='?', type=str, help='Directory to search for .DS_Store files')
    args = parser.parse_args()
    if args.directory is not None:
        directory = args.directory
        print(directory)
    else:
        # Enter your directory below for testing or scripting purposes.
        directory = Path(r'C:\Users\brand\Dev\python\automation\Test')
        print(directory)
    if os.path.exists(directory):
        delete_ds_store(directory)
    else:
        print(f"Directory does not exist: {directory}")
        exit(1)
