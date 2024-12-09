import sys
import yaml

SQL_FILE = "eazyskills_update.sql"

def escape_sql_string(value):
    """Escape single quotes in SQL strings."""
    if isinstance(value, str):
        return value.replace("'", "''")  # Double apostrophes to escape
    return value

def generate_sql_for_course(course, file_path):
    """Generate SQL for a course."""
    return f"""
    INSERT INTO courses (file_path, name, url, duration_hours, level, objectives, description, prerequisites, technologies, language, deprecated)
    VALUES ('{file_path}', '{escape_sql_string(course["name"])}', '{escape_sql_string(course["url"])}', {course["duration_hours"]}, '{escape_sql_string(course["level"])}', '{escape_sql_string(course["objectives"])}', '{escape_sql_string(course["description"])}', '{escape_sql_string(course.get("prerequisites", ""))}', ARRAY{course["technologies"]}, '{escape_sql_string(course["language"])}', {str(course["deprecated"]).upper()})
    ON CONFLICT (file_path) DO UPDATE SET
        name = EXCLUDED.name,
        url = EXCLUDED.url,
        duration_hours = EXCLUDED.duration_hours,
        level = EXCLUDED.level,
        objectives = EXCLUDED.objectives,
        description = EXCLUDED.description,
        prerequisites = EXCLUDED.prerequisites,
        technologies = EXCLUDED.technologies,
        language = EXCLUDED.language,
        deprecated = EXCLUDED.deprecated;
    """

def generate_sql_for_path(path, file_path):
    """Generate SQL for a path."""
    return f"""
    INSERT INTO paths (file_path, name, target_role, course_ids, prerequisites, url, language, deprecated)
    VALUES ('{file_path}', '{escape_sql_string(path["name"])}', '{escape_sql_string(path["target_role"])}', ARRAY{path["course_ids"]}, '{escape_sql_string(path.get("prerequisites", ""))}', '{escape_sql_string(path.get("url", ""))}', '{escape_sql_string(path["language"])}', {str(path["deprecated"]).upper()})
    ON CONFLICT (file_path) DO UPDATE SET
        name = EXCLUDED.name,
        target_role = EXCLUDED.target_role,
        course_ids = EXCLUDED.course_ids,
        prerequisites = EXCLUDED.prerequisites,
        url = EXCLUDED.url,
        language = EXCLUDED.language,
        deprecated = EXCLUDED.deprecated;
    """

def generate_sql_for_bootcamp(bootcamp, file_path):
    """Generate SQL for a bootcamp."""
    return f"""
    INSERT INTO bootcamps (file_path, name, target_role, modules, duration_weeks, prerequisites, url, language, deprecated)
    VALUES ('{file_path}', '{escape_sql_string(bootcamp["name"])}', '{escape_sql_string(bootcamp["target_role"])}', ARRAY{bootcamp["modules"]}, {bootcamp["duration_weeks"]}, '{escape_sql_string(bootcamp.get("prerequisites", ""))}', '{escape_sql_string(bootcamp.get("url", ""))}', '{escape_sql_string(bootcamp["language"])}', {str(bootcamp["deprecated"]).upper()})
    ON CONFLICT (file_path) DO UPDATE SET
        name = EXCLUDED.name,
        target_role = EXCLUDED.target_role,
        modules = EXCLUDED.modules,
        duration_weeks = EXCLUDED.duration_weeks,
        prerequisites = EXCLUDED.prerequisites,
        url = EXCLUDED.url,
        language = EXCLUDED.language,
        deprecated = EXCLUDED.deprecated;
    """

def process_file(file_path):
    """Process a single YAML file and generate SQL."""
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

        # Ensure file_path is included in the SQL
        data["file_path"] = file_path  # Dynamically add the file_path field

        # Determine entity type based on directory
        if "courses/" in file_path:
            return generate_sql_for_course(data, file_path)
        elif "paths/" in file_path:
            return generate_sql_for_path(data, file_path)
        elif "bootcamps/" in file_path:
            return generate_sql_for_bootcamp(data, file_path)
        else:
            raise ValueError(f"Unknown directory for file: {file_path}")

if __name__ == "__main__":
    files = sys.argv[1:]  # Get list of modified files passed as arguments

    if not files:
        print("No files to process.")
        sys.exit(0)

    sql_statements = []

    for file in files:
        try:
            sql_statements.append(process_file(file))
        except Exception as e:
            print(f"Error processing file {file}: {e}")
            sys.exit(1)

    # Write all SQL statements to the file
    with open(SQL_FILE, "w") as sql_file:
        sql_file.write("\n".join(sql_statements))

    print(f"SQL script generated: {SQL_FILE}")
