import os
import shutil

def copy_template(template_name, dest, context=None):
    template_path = os.path.join(os.path.dirname(__file__), "templates", template_name)
    shutil.copytree(template_path, dest)
    # Optionally fill in template variables using context

def create_venv(project_path):
    import venv
    venv.create(os.path.join(project_path, 'venv'), with_pip=True)
