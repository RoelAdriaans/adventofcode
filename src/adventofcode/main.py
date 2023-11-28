import importlib
import logging
import os
import sys
import timeit
from datetime import datetime
from pathlib import Path

import click
import requests
import tqdm
from bs4 import BeautifulSoup
from cookiecutter.main import cookiecutter
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load env values from .env file, or from environment variables if set
load_dotenv()


@click.command()
@click.argument(
    "day",
    type=click.IntRange(1, 25),
)
@click.option(
    "--year",
    default=lambda: os.environ.get("AOC_YEAR", datetime.now().year),
    type=click.IntRange(2016, 2025),
    help="The year to run. Defaults to current year. Can be overriden in .env "
    "by using value AOC_YEAR",
)
@click.option(
    "--create",
    is_flag=True,
    help="Create the files for a specific day",
)
@click.option(
    "--force",
    is_flag=True,
    help="Overwrite if files already exist",
)
@click.option(
    "--submit",
    is_flag=True,
    help="Submit the results to Advent of Code",
)
@click.option(
    "--download",
    is_flag=True,
    help="Download fresh copy of the input before starting",
)
@click.option("--parta", "part", flag_value="parta")
@click.option("--partb", "part", flag_value="partb")
@click.option(
    "-t",
    "--timeit",
    "timeit_",
    type=click.INT,
    help="Test the solution using timeit with timeit iterations",
)
@click.option("-v", "--verbose", is_flag=True)
def main(day, year, create, force, submit, download, part, timeit_, verbose):
    """
    Simple program that runs a module from the advent of code.
    DAY is an integer representing the day (1 - 25) that runs that day.
    """
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.WARNING

    if create and submit:
        print("Create and submit cannot be used at the same time")
        sys.exit(-65)

    if submit and not part:
        print(
            "Submit can only be used ony part at a time (Eg specify --parta or --partb)"
        )
        sys.exit(-65)

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )

    day = f"{int(day):02}"

    print(
        f"Welcome to Advent of Code - {year=} - {day=} - {part=} - {timeit_=} - "
        f"{verbose=} - {create=}"
    )

    if create:
        # Create a new solution
        ensure_correct_directory()
        create_solution(force=force, year=year, day=day)
        download_input_data(year=year, day=day)
    else:
        # Run a specific day
        if download:
            download_input_data(year=year, day=day)
        run_solution(year=year, day=day, timeit_=timeit_, part=part, submit=submit)


def ensure_correct_directory():
    """Make sure that we are in the correct directory: Main sources root"""
    main_file = Path("src/adventofcode/main.py")
    if main_file.exists():
        return True
    else:
        current_path = Path(__file__).parent.parent.parent.resolve()
        print(f"Not in the correct folder. Please execute: cd {current_path}")
        sys.exit(-65)


def create_solution(force, year, day):
    print(f"Creating solution for {year}-{day} --")

    # Check before we overwrite
    import_path = f"adventofcode{year}.solutions.day{day}"
    logger.debug(f"Importing {import_path}")
    try:
        importlib.import_module(import_path)
    except ModuleNotFoundError:
        pass
        logger.debug(f"{import_path} does not exist, we can continue")
    else:
        if not force:
            print("Module already exists - Not creating")
            sys.exit(-65)

    cookiecutter(
        "template/",
        no_input=True,
        extra_context={"day": day, "year": year},
        overwrite_if_exists=True,
    )


def _get_session():
    session = os.environ.get("AOC_SESSION")
    if not session:
        print("AOC_SESSION key is not set in environment or .env file")
        sys.exit(-65)
    return session


def download_input_data(year: str, day: str):
    """Download the input data"""
    # Download the content, using the session key
    r = requests.get(
        f"https://adventofcode.com/{year}/day/{day.lstrip('0')}/input",
        cookies={"session": _get_session()},
        timeout=30,
    )
    if r.status_code != 200:
        print(f"Unable to download the input data. Response code {r.status_code}")
        if r.status_code == 500:
            print("An internal server error occurred. Is your session valid?")
        elif r.status_code == 404:
            print(
                "Solution not found: You are too early, or this day does not"
                "have an input file."
            )
        else:
            print(r.content)

        sys.exit(-65)

    logger.debug(f"Received data, length {len(r.content)}")

    data_path = f"day_{day}/day{day}.txt"
    root_dir = Path(__file__).parent.parent
    filename = root_dir / f"adventofcode{year}" / "solutions" / "data" / data_path
    with open(filename, "wb") as f:
        f.write(r.content)

    logger.info(f"Input data writen to {filename}")


def run_solution(year, day, timeit_, part, submit):
    # Try to import the solution
    import_path = f"adventofcode{year}.solutions.day{day}"
    data_path = f"day_{day}/day{day}.txt"

    logger.debug(f"Importing {import_path}")

    try:
        day_module = importlib.import_module(import_path)
    except ModuleNotFoundError:
        print(f"Module {day} is not yet available")
        sys.exit(-65)
    if timeit_:
        execution_times = []
        results = ""

        for _ in tqdm.trange(timeit_):
            time_prior = timeit.default_timer()

            results = run_day(data_path, year, day, day_module, part, submit=False)

            time_after = timeit.default_timer()
            execution_times.append(time_after - time_prior)

        average_time = sum(execution_times) / len(execution_times)

        print("Results:")
        print(results)
        print(
            f"Average running time: {average_time:.6f} seconds ({timeit_} iterations)"
        )
    else:
        print("Results:")
        print(run_day(data_path, year, day, day_module, part, submit))


def run_day(data_path, year, day, day_module, part, submit):
    if part == "parta":
        result = run_parta(data_path, day, day_module)
        if submit:
            submit_result(year=year, day=day, part=part, result=result)
        return result

    elif part == "partb":
        result = run_partb(data_path, day, day_module)
        if submit:
            submit_result(year=year, day=day, part=part, result=result)
        return result

    else:
        a = run_parta(data_path, day, day_module)
        b = run_partb(data_path, day, day_module)

        return f"Part A:\n{a}\n\nPart B:\n{b}\n"


def run_parta(data_path, day, day_module):
    result = getattr(day_module, f"Day{day}PartA")()(data_path)
    return result


def run_partb(data_path, day, day_module):
    result = getattr(day_module, f"Day{day}PartB")()(data_path)
    return result


def submit_result(year, day, part, result):
    """Submit a solution to advent of code"""
    day = day.lstrip("0")
    post_url = f"https://adventofcode.com/{year}/day/{day}/answer"
    logger.debug(f"Posting to {post_url}")

    level = 1 if part == "parta" else 2
    data = {"level": level, "answer": result}

    logger.debug(f"Posting data: {data}")

    r = requests.post(
        url=post_url,
        data=data,
        cookies={"session": _get_session()},
        timeout=30,
    )

    result = parse_result(r.text)

    if result:
        print(f"{result}")
    else:
        print(f"Could not parse content. Raw result:\n{str(r.content)}")


def parse_result(html_doc):
    # Parse the result, and print the first main.article
    soup = BeautifulSoup(html_doc, "html.parser")
    result = []
    for m in soup.main:
        # Skip empty sections or java scripts
        if m == "\n" or "<script>" in str(m):
            continue
        else:
            result.append(str(m.get_text()))
    return result


if __name__ == "__main__":
    main()
