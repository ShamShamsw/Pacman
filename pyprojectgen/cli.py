import click
from .generator import ProjectGenerator

@click.group()
def cli():
    pass

@cli.command()
@click.argument('project_name')
@click.option('--template', default='package', help='Template type')
@click.option('--git/--no-git', default=False, help='Initialize git repo')
@click.option('--venv/--no-venv', default=False, help='Create virtualenv')
def new(project_name, template, git, venv):
    """Create a new Python project."""
    generator = ProjectGenerator()
    generator.create_project(
        name=project_name,
        template=template,
        git=git,
        venv=venv
    )
    click.echo(f"Project {project_name} created with template {template}.")

if __name__ == '__main__':
    cli()
