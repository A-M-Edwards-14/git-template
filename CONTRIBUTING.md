# Contributing to <PROJECT_NAME>

Please take a moment to review these guidelines before you start helping out.

## **Quick links**
- You can find the main repository's README file [here](./README.md) for more details about the project.
- The <b>Getting Started</b> section in the README file outlines how to quickly set up your environment for development.


## **How to Contribute**

### **Creating & Updating uv.lock & pyproject.toml**
To create and update the uv.lock file, follow the following steps below:

1) First initialise the enviroment, this will in essense create the venv and pyproject.toml file.
```
python -m uv init
```

2) To install or add extra packages to the enviroment, enter the command below.
```
python -m uv add <PACKAGE_NAME>
```

3) If the package being installed is via a hyperlink, replace the package name with the link.
```
python -m uv add <HYPERLINK>
```

4) To update the uv.lock file with new packages added, run:
```
python -m uv sync --upgrade
```

5) To execute specific scripts, use this command.
```
python -m uv run python <SCRIPT.py>
```

### **Enabling Relative Imports**

A common problem you may encounter with this repo is the "attempted relative import with no known parent package" error. This occurs when trying to import scripts in different subfolders into one another. The following steps demonstrate how to set your repo up to avoid this error.

The [pyproject.toml](./pyproject.toml) file acts as the "ID card" for the project. It identifies the root directory as a package and specifies how it should be built.

To enable the relative imports, we must install the working directory as an editable install (as shown below):

```
$ python -m pip install -e .
```

This tells tools like pip that the current folder is not just a collection of files, but a structured Python package with a specific name. Thus allowing relative imports to occur.

### **Enabling Pre-Commits**

1) First install pre-commit with pip.
```
$ python -m pip install pre-commit
```

2) With the yaml file now filled with your selection of checks, you need to install all the checks you have made to the pre-commit hooks files. This is done with the command:
```
$ pre-commit install
```

3) The pre-commits are now all set up. If you try and commit code that doesn’t meet any of the checks you have put in place, you commit will be blocked until you make the necessary changes. Alternatively, you can quickly check if your code does meet the pre-commit checks by running:

```
$ pre-commit run --all-files
```

4) Alternatively, you can run the checks on a single file with:
```
$ pre-commit run --files <file_path>
```


### **Submitting/Suggesting Code Changes**
Whether you want to: suggest a fix to a known bug/issue; want to propose an enhancement; or provide a general beneficial suggestion change to the code base, please follow the below steps to acheive this.

1. Clone the repository.
2. Create a new branch for your changes (`git checkout -b feature-name`).
3. Make your changes and commit them with clear, concise messages.
4. Merge your branch with the master once finished developing the feature.

### **Commit Message Style**
We currently use _conventional commits_ in our workflows. Below is a table listing the prefixes you should use when opening a pull request from a forked repository:

| Prefix       | Description                                      | Example Usage               | 
|--------------|--------------------------------------------------|-----------------------------|
| `fix:`       | Indicates a bug fix in the codebase.             | `fix: resolve null pointer` | 
| `feat:`      | Introduces a new feature or functionality.       | `feat: add user login`      | 
| `docs:`      | Updates or improves documentation.               | `docs: update README`       | 
| `test:`      | Adds or modifies tests for existing functionality. | `test: add unit tests`      | 
| `chore:`     | Miscellaneous tasks like build or dependency updates. | `chore: update dependencies` |
| `refactor:`  | Code changes that neither fix a bug nor add a feature. | `refactor: optimize loop`   |
| `style:`     | Changes that do not affect the meaning of the code (e.g., formatting). | `style: fix linting issues` |
| `perf:`      | Code changes that improve performance.           | `perf: improve query speed` |
| `ci:`        | Changes to CI/CD configuration files and scripts. | `ci: update GitHub Actions` |
| `revert:`    | Reverts a previous commit.                       | `revert: undo feature`      |

Ensure your commit starts with one of these prefixes.


### **Code Style**
- Ensure your code is well-documented and includes tests where applicable.
- Follow pep-8 coding standards where possible.

To ensure consistent styling, it is good practice to apply automatic linting tools to your scripts prior to committing. This is done by using the commands shown below:

```
$ python -m black --line-length 78 ./src/
```

```
$ python -m isort --line-length 78 ./src/
```

Also, it is good practice to measure how compliant your code is with PEP 8 standards. This can be done using the Pylint tool. Use the command below to measure compliance and make the suggested changes where appropriate:

```
$ python -m pylint --max-line-length=78 ./src/
```


### **Testing**
Provide unit tests for all functions and features added to this repository.

It is good practice to aim for atleast 70% test coverage (ideally over 80%, but this won't always be possible). To measure the overall test coverage of the repo, use the commands shown below:

```
$ coverage run --source=src -m unittest discover -s test
```

```
$ python -m coverage report
```
---

