import os
import json
from json.decoder import JSONDecodeError

def update_info_json_files(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename == "info.json":
                file_path = os.path.join(subdir, filename)
                try:
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                    data['url'] = None
                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    print(f"Updated {file_path}")
                except JSONDecodeError as e:
                    print(f"Error updating {file_path}: {e}")

if __name__ == "__main__":
    root_directory = "."  
    update_info_json_files(root_directory)
