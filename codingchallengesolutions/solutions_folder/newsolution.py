import os
import json
import shutil
import sys

def create_folder_and_file(file_name, language_flag):
    # Determine the file extension and runtime field name based on the language flag
    extensions = {'c': '.cpp', 'j': '.java', 'p': '.py'}
    runtime_fields = {'c': 'cpp_runtime', 'j': 'java_runtime', 'p': 'python_runtime'}
    file_extension = extensions.get(language_flag, '.txt')  # Default to .txt if flag is unknown
    runtime_field = runtime_fields.get(language_flag, 'runtime')  # Default to generic 'runtime' if flag is unknown
    
    # Create folder with the given name if it doesn't exist
    if not os.path.exists(file_name):
        os.makedirs(file_name)
    else:
        print(f"Folder '{file_name}' already exists. Updating contents.")
    
    # Copy info.json to the new folder, overwrite if exists
    info_json_path = f'{file_name}/info.json'
    if not os.path.exists(info_json_path):
        shutil.copy('info.json', info_json_path)
    else:
        print("info.json already exists in the target folder. It will be updated.")
 
    
    # Prepare the data structure with the specific runtime field
    data = {
        "difficulty": input("Enter difficulty (easy/medium/hard): "),
        runtime_field: float(input("Enter runtime (in seconds): ")),
        "companies": [],
        "title": " ".join(part.capitalize() for part in file_name.split("_")),
        "site": input("Enter site name: "),
        "url": input("Enter problem URL: "),
    }
    
    # Add companies
    while True:
        company = input("Enter company name (or type 'x' to finish): ")
        if company.lower() == 'x':
            break
        data['companies'].append(company)
    
    # Write the updated data to info.json inside the new folder
    with open(info_json_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    # Create an empty solution file with appropriate extension
    solution_file_path = f"{file_name}/{file_name}{file_extension}"
    if not os.path.exists(solution_file_path):
        open(solution_file_path, 'w').close()
        print(f"Empty solution file created: {solution_file_path}")
    else:
        print(f"Solution file already exists: {solution_file_path}")
    
    print(f"Folder '{file_name}' setup completed.")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] not in ['c', 'j', 'p']:
        print("Usage: newsolution <file_name> <language_flag(c/j/p)>")
    else:
        create_folder_and_file(sys.argv[1], sys.argv[2])
