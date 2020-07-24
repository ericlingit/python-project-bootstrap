import re
import sys
import subprocess
import file_content
from pathlib import Path


def main():
    # Get info from user
    project_name = input("Project name (example: my_awesome_app): ")
    project_desc = input("Short description: ")
    target_loc = Path(input("Project location (example: /home/john/Documents): "))
    app_name = input("App name (optional): ")  # name for your source dir
    app_name = project_name if not app_name else app_name

    if not target_loc.exists():
        sys.exit(f"Target location not found: {target_loc}")

    # Sanitize app name
    delim = re.compile("[ -]")
    app_name = delim.sub("_", app_name)

    # Directories
    proj_dir = Path(f"{target_loc}/{project_name}").resolve()
    src_dir = proj_dir/app_name
    test_dir = proj_dir/"test"

    # Files
    readme = proj_dir/"README.md"
    setup_py = proj_dir/"setup.py"
    app_py = src_dir/f"{app_name}.py"
    test_py = test_dir/f"test_{delim.sub('_', project_name)}.py"
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
        fh.write(f"# {project_name}\n\n{project_desc}\n")
    with setup_py.open("w") as fh:
        fh.write(file_content.setup(app_name, project_desc))
    with test_py.open("w") as fh:
        fh.write(file_content.testpy(app_name))


    # Create virtual environment
    v = input("Do you want to create a virtual environment? (y/n)")
    if v.lower() != "y":
        print("No virtual environment will be created.")
    else:
        try:
            import venv
            venv.create(proj_dir/"env", with_pip=True, clear=True)
            print("Activate the environemnt by entering 'source ./env/bin/activate'")
            print("You can upgrade pip by executing 'python -m pip install --upgrade pip'")
            print("Recommended updates: 'pip install --upgrade setuptools wheel'")
            print("Recommended package: 'sudo apt install python3-dev'")
        except ImportError:
            print("Unable to import venv, do you have python3-venv installed?")
        except Exception as e:
            print(f"Unable to create a virtual environment: {e}")


    # Initialize a git repo
    g = input("Do you want to initialize a local git repository? (y/n)")
    if g.lower() != "y":
        print("No git repo will be created.")
    else:
        try:
            subprocess.run(["git", "init", str(proj_dir)])
        except Exception as e:
            print(f"Unable to initialize a git repository: {e}")

    # Create .gitignore
    ign = proj_dir/".gitignore"
    ign.touch(exist_ok=True)

    with ign.open("w") as fh:
        fh.write(file_content.GITIGNORE)


if __name__ == "__main__":
    main()
