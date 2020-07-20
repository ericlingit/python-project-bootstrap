# python-project-bootstrap

Quickly set up a python project folder.

(like rust's `Cargo`; you could type `cargo new project_name` to bootstrap the creation of a new rust project)

It should create this folder structure:
```
project_name/
    project_name/    (for source codes)
        __init__.py
        project_name.py
    test/
        __init__.py
        test_project_name.py
    README.md
    setup.py
```


## Todo

1. get user data
1. fill file content template
1. create dir
1. create files
1. modify files


## Later improvements:
- initialize a git repo, and place a `.gitignore`
- setup a python virtual environment and place it under the root project_folder (suggest user to do `apt install python3-dev python3-venv`)
- run pip updates for you:
    ```
    python -m pip install --upgrade pip
    pip install --upgrade setuptools wheel
    ```
- install flake8 and place a config file
