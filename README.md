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

- [x] get user data
- [x] fill file content template
- [x] create dir
- [x] create files
- [x] modify files
- [x] setup a python virtual environment and place it under the root project_folder (suggest user to do `apt install python3-dev`)


## Later improvements:
- initialize a git repo, and place a `.gitignore`
