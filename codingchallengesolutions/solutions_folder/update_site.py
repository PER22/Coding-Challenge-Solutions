import os
import json
from json.decoder import JSONDecodeError

def update_info_json_files(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        # Filter out solution files before processing info.json
        solution_files = [f for f in files if f.endswith(('.py', '.cpp', '.java'))]
        for filename in files:
            if filename == "info.json":
                file_path = os.path.join(subdir, filename)
                try:
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                    
                    # Process each solution file
                    for solution_file in solution_files:
                        if solution_file.endswith('.py'):
                            data['python_solution'] = os.path.join(subdir.replace(root_dir, '').lstrip('/'), solution_file)
                        elif solution_file.endswith('.cpp'):
                            data['cpp_solution'] = os.path.join(subdir.replace(root_dir, '').lstrip('/'), solution_file)
                        elif solution_file.endswith('.java'):
                            data['java_solution'] = os.path.join(subdir.replace(root_dir, '').lstrip('/'), solution_file)

                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    print(f"Updated {file_path}")
                except JSONDecodeError as e:
                    print(f"Error updating {file_path}: {e}")

if __name__ == "__main__":
    root_directory = "."  # Adjust this path to your actual solutions_folder directory
    update_info_json_files(root_directory)
