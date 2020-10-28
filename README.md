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

## Usage
```bash
eric@eric-pc:~/Documents/python-project-bootstrap$ python3 -m pybootstrap
Project name (example: my_awesome_app): my_awesome_app
Short description: Parse eml files into plain text     
Project location (example: /home/john/Documents): /home/eric/Documents
App name (optional): 
Do you want to create a virtual environment? (y/n)y
Activate the environemnt by entering 'source ./env/bin/activate'
You can upgrade pip by executing 'python -m pip install --upgrade pip'
Recommended updates: 'pip install --upgrade setuptools wheel'
Recommended package: 'sudo apt install python3-dev'
Do you want to initialize a local git repository? (y/n)y
Initialized empty Git repository in /home/eric/Documents/my_awesome_app/.git/
Don't forget to update git config!
```

## Todo

- [x] get user data
- [x] fill file content template
- [x] create dir
- [x] create files
- [x] modify files
- [x] setup a python virtual environment and place it under the root project_folder (suggest user to do `apt install python3-dev`)
- [x] initialize a git repo, and place a `.gitignore`
