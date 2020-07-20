from pathlib import Path

# Get these from user
project_name = input("Project name: ")
project_desc = input("Short description: ")
target_loc = input("Project location: ")
app_name = input("App name (optional): ")  # name for your source dir
app_name = project_name if not app_name else app_name

# Directories
proj_dir = Path(f"{target_loc}/{project_name}").resolve()
src_dir = proj_dir/app_name
test_dir = proj_dir/"test"

# Files
readme = proj_dir/"README.md"
setup_py = proj_dir/"setup.py"
app_py = src_dir/f"{project_name}.py"
test_py = test_dir/f"test_{project_name}.py"
init_py = "__init__.py"

# Create directories and files
proj_dir.mkdir(exist_ok=False, parents=True)
src_dir.mkdir(exist_ok=False, parents=True)
test_dir.mkdir(exist_ok=False, parents=True)
readme.touch()
setup_py.touch()
app_py.touch()
test_py.touch()
(src_dir/init_py).touch()
(test_dir/init_py).touch()


# Update file content
with readme.open("w") as fh:
    fh.write(f"# {project_name}\n{project_desc}\n")
with setup_py.open() as fh:
    fh.write("")
with test_py.open("w") as fh:
    fh.write("")
