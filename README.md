# Template repository
## Introduction 
A template repository for Digital Health (DH) projects.

## Version control
Version control is required for all projects. At DH we work with git and Azure DevOps. The following are suggested for git usage
  * Use a feature branch or 
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow
  * The master branch is protected through a pull request [policy](https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops).
  * Commit messages are written in English and adhere to the following rules:
    1. The title-line starts with a capital letter, is 50 characters (or less), 
       and has no punctuation at the end.
    2. It should be in the imperative voice. i.e. 
       'Add new About Us page' or 'Refactor tests for the order model'
    3. It should correctly complete the sentence: "If accepted, this commit will <your commit message goes here>."

## Directory structure
Here you can add the directory structure of the project.
Run `tree .` in the terminal to get your project tree.
In order to get a clean tree with only files tracked by git you can either
* Make a new clone
* Remove all untracked and ignoref files with `git clean dfX`
    * Recommended to first do a test run with `git clean nX`

before running `tree`.
```
.
├── README.md
├── data
│   ├── interim
│   ├── processed
│   └── raw
├── docs
│   ├── Makefile
│   └── source
│       ├── conf.py
│       ├── index.rst
│       └── readme_link.rst
├── logs
├── requirements.txt
└── src
    ├── __init__.py
    ├── config.py
    ├── data
    │   ├── __init__.py
    │   └── download_data.py
    └── utils
        └── utils.py
```

## Virtual environment
### Using conda
```
conda env create -f environment.yml
conda activate
```

### Using venv
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

To add you local packages to you pythonpath run 
`export PYTHONPATH="${PYTHONPATH}:."`

## Documentation and styleguide
Styleguids can be checked with linters, for instance, `flake8`.
By default, we adhere to the PEP-8 conventions
The line-length is automatically formatted by `black`
and has a maximum of 88. Line lengths of upto 119 characters are permissible.
The `.flake8` files contains guidelines we choose to ignore.

Code can be formatted (`black`) and checked (e.g. `flake8`)
```
black src/
flake8 --max-line-length 119 src/
```

### Docstrings
We adhere to PEP-8 and PEP-257 with respect to docstrings. 
This implies a line length of at most 72 characters.
The following missing docstrings are currently ignored (see `.flake8`)
* D100 Missing docstring in public module
* D104 Missing docstring in public package

### pre-commit hooks
[pre-commit](https://pre-commit.com) hooks can be configured to automatically 
run formatting and linting steps. An example `.pre-commit-config.yaml`
is present in the root folder. After installation `pre-commit` will
be run upon every commit.

```
# Run pre-commit locally
pre-commit run --all 

# Setup to run pre-commit after every commit
pre-commit install  # instals pre-commit at .git/hooks/pre-commit
```

### Sphinx
With `Sphinx` documentation can be automatically generated as html or pdf
from the docstrings. The example in this repository includes
the `src` package and the `README` file.
For a tutorial see [here](https://github.com/finsberg/sphinx-tutorial).

Generate the documentation as follows

```
cd docs
sphinx-apidoc -o source/ ../src/

# for html
make html
python -m http.server  # launches at http://localhost:8000/build/html/

# for pdf (requires e.g. macTeX)
make latexpdf
```

