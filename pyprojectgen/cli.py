import argparse
from .generator import copy_template, create_venv

def main():
    parser = argparse.ArgumentParser(description="Generate Python project scaffolding.")
    parser.add_argument("name", help="Project name")
    parser.add_argument("--template", default="script", help="Template type")
    parser.add_argument("--venv", action="store_true", help="Create virtual environment")
    args = parser.parse_args()

    project_path = args.name
    copy_template(args.template, project_path)
    if args.venv:
        create_venv(project_path)

if __name__ == "__main__":
    main()
