import os
import re
import sys
from glob import glob

# Define regex patterns for naming conventions
PATTERN_COURSES = r"^[a-z_]+_(beginner|intermediate|advanced)_(en|fr|es)(_([a-z_]+))?\.yaml$"
PATTERN_PATHS = r"^[a-z_]+(_[a-z_]+)?_(en|fr|es)\.yaml$"
PATTERN_BOOTCAMPS = r"^[a-z_]+_[a-z_]+_(en|fr|es)\.yaml$"

def validate_naming(directory, pattern):
    """Validate filenames in a directory against a given regex pattern."""
    files = glob(f"{directory}/*.yaml")
    invalid_files = []

    for file in files:
        filename = os.path.basename(file)
        if not re.match(pattern, filename):
            invalid_files.append(filename)
    
    return invalid_files

if __name__ == "__main__":
    errors = []
    
    # Validate naming conventions for each category
    errors += validate_naming("courses", PATTERN_COURSES)
    errors += validate_naming("paths", PATTERN_PATHS)
    errors += validate_naming("bootcamps", PATTERN_BOOTCAMPS)
    
    if errors:
        print("Invalid filenames detected:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("All filenames are valid.")
