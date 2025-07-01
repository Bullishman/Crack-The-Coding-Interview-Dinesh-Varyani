import pandas as pd
import os
import shutil

# --- Configuration ---
EXCEL_FILE = 'Crack The Coding Interview.xlsx'
TEMPLATE_FOLDER = '0-sample'
# --- End of Configuration ---

def create_problem_folder(problem_data):
    """Creates a directory and files for a single problem."""
    try:
        # 1. Set up variables from the problem data
        num = int(problem_data['Number'])
        topic = problem_data['Topic']
        url = problem_data['Question']
        difficulty = problem_data['Difficulty']

        # Extract the problem name from the URL (e.g., "two-sum")
        problem_name = url.strip('/').split('/')[-1]
        
        # Create a title-cased problem title (e.g., "Two Sum")
        problem_title = ' '.join(word.capitalize() for word in problem_name.split('-'))
        
        # Define the new folder and file names
        new_folder_name = f"{num}-{problem_name}"
        python_file_name = f"{problem_name}.py"

        print(f"--- Processing: {new_folder_name} ---")

        # 2. Check if the folder already exists
        if os.path.exists(new_folder_name):
            print(f"[SKIP] Directory '{new_folder_name}' already exists.")
            return

        # 3. Copy the template folder
        shutil.copytree(TEMPLATE_FOLDER, new_folder_name)
        print(f"[OK] Copied template to '{new_folder_name}'.")

        # 4. Clean up the template files inside the new folder
        os.remove(os.path.join(new_folder_name, 'sample.py'))
        os.remove(os.path.join(new_folder_name, 'README.md'))

        # 5. Create the new problem-specific files
        # Create an empty python file
        open(os.path.join(new_folder_name, python_file_name), 'w').close()
        
        # Create the README.md file with the problem details
        readme_content = f"""# {num}. {problem_title}

**Difficulty**: {difficulty}

**Topics**: {topic}

**Link**: {url}
"""
        with open(os.path.join(new_folder_name, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"[OK] Created '{python_file_name}' and 'README.md'.")

    except (KeyError, TypeError) as e:
        print(f"[ERROR] Skipping row due to missing or invalid data: {e}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while processing '{new_folder_name}': {e}")


def main():
    """Main execution function to read the Excel file and process all problems."""
    # 1. Check if the template folder exists before starting
    if not os.path.isdir(TEMPLATE_FOLDER):
        print(f"[FATAL] Template folder '{TEMPLATE_FOLDER}' not found. Aborting.")
        return
        
    # 2. Read the Excel file
    try:
        df = pd.read_excel(EXCEL_FILE)
        # Verify that required columns exist
        required_columns = ['Number', 'Topic', 'Question', 'Difficulty']
        if not all(col in df.columns for col in required_columns):
            print(f"[FATAL] Excel file '{EXCEL_FILE}' is missing one of the required columns: {required_columns}")
            return
    except FileNotFoundError:
        print(f"[FATAL] Excel file '{EXCEL_FILE}' not found. Aborting.")
        return
    except Exception as e:
        print(f"[FATAL] Failed to read the Excel file: {e}")
        return

    print("==================================================")
    print("Starting the problem setup process...")
    print(f"Found {len(df)} problems in '{EXCEL_FILE}'.")
    print("==================================================")

    # 3. Iterate over each row in the DataFrame and create a folder
    for index, row in df.iterrows():
        create_problem_folder(row)

    print("\n==================================================")
    print("All tasks completed.")
    print("==================================================")

if __name__ == "__main__":
    main()
