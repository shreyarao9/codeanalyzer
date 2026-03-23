from analyzer import analyze_code
import sys
from pathlib import Path

def analyze_file(filepath):
    """Helper function to read and analyze a single file."""
    try:
        # Added utf-8 encoding to prevent errors on different operating systems
        with open(filepath, 'r', encoding='utf-8') as file:
            code_contents = file.read()
            
        results = analyze_code(code_contents)
        
        print(f"--- Results for {filepath} ---")
        print(results)
        print() # Add a blank line for readability between files

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

def main():
    # Get filename from command line
    # sys.argv[0] is 'main.py', sys.argv[1] is 'test_code.py'
    if len(sys.argv) < 2:
        print("Error: Please provide a file or directory to analyze.")
        print("Usage: python main.py <filename_or_directory>")
        sys.exit(1) # Exit the program with an error code
        
    # Convert the argument into a Path object
    target_path = Path(sys.argv[1])

    # Handle paths that don't exist
    if not target_path.exists():
        print(f"Error: The path '{target_path}' was not found.")
        sys.exit(1)

    # Handle Single Files
    if target_path.is_file():
        if target_path.suffix == '.py':
            analyze_file(target_path)
        else:
            print(f"Error: '{target_path}' is not a Python (.py) file.")
            
    # Handle Directories
    elif target_path.is_dir():
        print(f"Scanning directory: {target_path}\n")
        
        # .rglob('*.py') recursively finds ALL .py files in the folder and subfolders
        python_files = list(target_path.rglob('*.py'))
        
        if not python_files:
            print("No Python files found in this directory.")
            
        for filepath in python_files:
            analyze_file(filepath)

if __name__ == "__main__":
    main()