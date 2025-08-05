import os
import shutil
import pytest
from pyprojectgen.generator import ProjectGenerator

def test_create_project(tmp_path):
    gen = ProjectGenerator()
    proj_name = "testproj"
    gen.create_project(proj_name, "package")
    assert (tmp_path / proj_name / "README.md").exists()
