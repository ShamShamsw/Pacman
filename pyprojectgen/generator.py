import os
import shutil
import subprocess
from jinja2 import Environment, FileSystemLoader

class ProjectGenerator:
    def __init__(self, templates_dir=None):
        self.templates_dir = templates_dir or os.path.join(os.path.dirname(__file__), 'templates')

    def create_project(self, name, template, git=False, venv=False):
        dest = os.path.abspath(name)
        template_path = os.path.join(self.templates_dir, template)
        
        # Render template files
        env = Environment(loader=FileSystemLoader(template_path))
        os.makedirs(dest, exist_ok=True)
        for root, dirs, files in os.walk(template_path):
            rel_path = os.path.relpath(root, template_path)
            target_dir = os.path.join(dest, rel_path) if rel_path != '.' else dest
            os.makedirs(target_dir, exist_ok=True)
            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(target_dir, file)
                with open(src_file, 'r') as f:
                    content = env.from_string(f.read()).render(project_slug=name)
                with open(dst_file, 'w') as f:
                    f.write(content)
        
        if venv:
            subprocess.run(['python', '-m', 'venv', os.path.join(dest, 'venv')])
        if git:
            subprocess.run(['git', 'init', dest])
