# Pacman

**Pacman** is my Python project to streamlines the process of starting new Python projects by automating structure creation, virtual environment setup, and inclusion of best-practice files. Pacman is built for individual developers, teams, and organizations looking to standardize and accelerate project bootstrapping. However I mainly built it so I could play games without wifi.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Reference Architecture](#reference-architecture)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Extending Pacman](#extending-Pacman)
8. [Testing](#testing)
9. [Contribution Guidelines](#contribution-guidelines)
10. [License](#license)

---

## Project Overview

This project solves the tedious, error-prone process of setting up a new Python project. By providing a suite of customizable templates and automation options, it ensures consistency, speeds up development, and enforces best practices across all Python projects in your workflow.

---

## Features

- **CLI Tool**: Simple, intuitive command-line interface.
- **Multiple Templates**: Script, package, CLI app, web app, and custom templates.
- **Best-Practice Files**: Auto-generates README, LICENSE, `.gitignore`, and basic test structure.
- **Virtual Environment**: Optionally set up a virtual environment.
- **Git Integration**: Optionally initialize a Git repository.
- **Extensible**: Support for user-defined and organizational templates.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Unit Tested**: Thorough test suite for reliability.

---

## Reference Architecture

### 1. CLI Layer

- **Purpose**: Handles all user interaction and input validation.
- **Technology**: [Click](https://click.palletsprojects.com/) (or `argparse` for minimal dependencies).
- **Location**: `Pacman/cli.py`

### 2. Core Logic Layer

- **Purpose**: Implements business logic for project generation, template management, and project customization.
- **Key Components**:
    - Template engine (Jinja2)
    - File operations (copy, render, variable substitution)
- **Location**: `Pacman/generator.py`

### 3. Template Layer

- **Purpose**: Houses all built-in and user-contributed templates.
- **Structure**:
    - Each template is a directory with a defined structure and meta-information.
    - Template variables (e.g., project name, author) are filled at runtime.
- **Location**: `Pacman/templates/`

### 4. Utilities

- **Purpose**: Supporting modules for OS-level tasks, logging, validation, etc.
- **Location**: `Pacman/utils/`

### 5. Testing

- **Purpose**: All logic is covered by unit and integration tests.
- **Technology**: pytest, unittest
- **Location**: `tests/`

---

## Installation

```bash
pip install Pacman
# or from source:
git clone https://github.com/yourorg/Pacman.git
cd Pacman
pip install .
```

---

## Usage

**Basic Example:**

```bash
Pacman new my_project --template package --git --venv
```

**Help:**

```bash
Pacman --help
```

**Available Templates:**

```bash
Pacman list-templates
```

---

## Project Structure

```plaintext
Pacman/
│
├── Pacman/
│   ├── __init__.py
│   ├── cli.py              # CLI Interface
│   ├── generator.py        # Core logic for generation
│   ├── templates/          # Built-in templates
│   │   ├── script/
│   │   ├── package/
│   │   ├── cli_app/
│   │   └── web_app/
│   └── utils.py            # Helper functions
│
├── tests/
│   ├── test_generator.py
│   └── test_cli.py
│
├── setup.py
├── pyproject.toml
├── README.md
├── .gitignore
└── LICENSE
```

---

## Example Built-in Template Structure

**Package Template:**

```plaintext
package/
├── {{project_slug}}/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_basic.py
├── README.md
├── pyproject.toml
├── .gitignore
└── LICENSE
```

Variables like `{{project_slug}}` are replaced with user input.

---

## Extending Pacman

You can add your own templates to `~/.Pacman/templates/` or a shared templates directory.
- Templates are simple directory trees with Jinja2-style variables.

---

## Testing

Run all tests:

```bash
pytest tests/
```

---

## Contribution Guidelines

1. Fork and clone the repo.
2. Create a new branch for your feature or bugfix.
3. Write tests for your changes.
4. Submit a pull request.

## No License
