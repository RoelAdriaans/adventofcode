# Advent of Code 2016, 2019, 2020, 2021 and 2022

Advent of Code for some years with tests and utils etc.
Code is in src/adventofcode<years>, tests are in tests/

## Todo

✅ Create a global adventofcode tool
✅ Add --year to adventofcode function
✅ Use adventofcodeutils package instead of utils per year
- Update coockiecutter templates
- Update documentation, currently copied from the latest version (2016)
- Complete all puzzles (Doh)

## Create a new day

You can use the adventofcode script to create the scaffolding and download the
input file for that day. If no year is given, the current year is set as a default.
A default year can also be stored in `.env`.

An example:

    adventofcode --year 2023 --create 20

### Env variables

Create a file `.env` with the content:

```ini
# Store the session key here
AOC_SESSION = ""
# Select the year. If None, the current year is used.
AOC_YEAR = None
```

The variable `AOC_SESSION` is the cookie from <https://adventofcode.com/>. This is available
in your browser after you've logged in.

## Cookiecutter

To create a new day with the CookieCutter version run the command from the
`advent2016` directory.

```shell script
cookiecutter template -f
```

Answer the questions:
* `advendofcode2016` : Accept default answer. This installs the result in the current directory
* `day` : Answer with day you're working on, with leading zero. Eg: 07, 10, 31.
* `directory_name`, `file_name`, `class_name` : Accept default answer

This will create the correct files in the `src` and `tests` directories.
The `-f` option is required to make the files in the current subdirectory.
When the project supports modules this is probably no longer needed.

The new solution still have to be added to the `main.py` file.

### Cookiecutter Todo

* Nothing at the moment

## Install

Install the application with:

```
poetry install
```

### Run

Use `tox` to run the tests, run `adventofcode` to run the main application.

### Update dependencies

For dependencies we use [Poetry Plugin: up](https://github.com/MousaZeidBaker/poetry-plugin-up).

#### Installation

```shell
poetry self add poetry-plugin-up
```

#### Usage

The plugin provides an `up` command to update dependencies

```shell
poetry up --help
```

Update dependencies

```shell
poetry up
```

Update dependencies to latest available compatible versions

```shell
poetry up --latest
```

## Pre-commit

This project uses [pre-commit]. Pre-commit runs all the required tools before committing.
This useful tool will be installed with:

```shell
pip install pre-commit
```

After installation run:

```shell
pre-commit install
```

Now every time before running `git commit` the hooks defined in the
`.pre-commit-config.yaml` file will be run before actually committing.
To run this manually, run:

```shell
pre-commit run --all-files
```

#### Update pre-commit

Update the `.pre-commit-config.yaml` with the command:

```shell
pre-commit autoupdate
```

This command will go online and find the latest versions.

[pre-commit]: https://pre-commit.com/
