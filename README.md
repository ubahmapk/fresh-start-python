# fresh-start-python

Template repository for a python project

## Usage

```
Usage: freshstartpy [OPTIONS]

 Example code base for a new python project.

╭─ Options ───────────────────────────────────────────────────────────╮
│ --verbose  -v      INTEGER  Repeat for extra verbosity [default: 0] │
│ --version  -V               Show the version and exit.              │
│ --help     -h               Show this message and exit.             │
╰─────────────────────────────────────────────────────────────────────╯
```

## Git (Phase 1)

Remove the `.git` directory, so you can use version control in your new project and not try and push stuff back to this one!

```shell
rm -rf .git
```

## Metadata Installation

1. Update the `pyproject.toml` file with the new:
 - project name
 - description
 - author name and email (if it's not me 😄️)
 - license (if changed)
 - classifiers
 - `project.scripts` section (to match the name)

2. Update the `freshstartpy` directory with the name of the script/module

3. Update the `__main__.py` file inside the newly-renamed project directory to use the updated project name in the import statement and the updated `prog_name` variable

`prog_name` is used used in the `--help` option to report the correct script name

4. Update the `__version__.py` file in the project directory (if necessary)

## Python Installation

I strongly recommend the use of [uv](https://docs.astral.sh/uv/) to manage your python environments.

Set up the virtual environment for the project.

1. Create the virtual environment in the root of the project folder

```shell
uv venv -p 3.13
```
(Or whatever Python version expected for this project)

2. Activate the new venv

```shell
source .venv/bin/activate
```

You can also configured your editor (like VSCode) to now use this environment when you launch a terminal for this project.

3. Install the project dependencies

```shell
uv sync -U
```

## Git (Phase 2)

Create the new repository and add the project.

1. Initialize git VCS

```shell
git init .
```

2. Create the repository

This assumes the repo will be hosted on github.com and that you have the `gh` client installed.

```shell
gh repo create [REPO_NAME] --private -d "[PROJECT DESCRIPTION]" --source=.
```

The above command also assumes you wish the repository to be private. Substitute options to your liking. 😄

Otherwise, please follow the instructions provided at the git provider you're using
