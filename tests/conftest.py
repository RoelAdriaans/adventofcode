import pathlib
import re

import pytest


def read_file(year: int, day: int, filename: str) -> str:
    """Load data from a file in data directory."""
    test_path = (
        pathlib.Path(__file__).parent.parent
        / "src"
        / f"adventofcode{year}"
        / "solutions"
        / "data"
        / f"day_{day:02}"
        / filename
    )
    with open(test_path) as f:
        test_data = f.read()
    return test_data


def parse_classname(request) -> tuple[int, int]:
    # Parse the class name
    day = int("".join(x for x in request.keywords.parent.name if x.isdigit()))
    year = re.findall(r"adventofcode(\d{4})", repr(request.keywords.parent.cls))
    if not year:
        raise ValueError("Path not found")
    else:
        year = int(year[0])

    return year, day


@pytest.fixture
def testdata(request) -> str:
    """Load data from a testfile."""
    year, day = parse_classname(request)
    return read_file(year, day, f"day{day:02}_test.txt")


@pytest.fixture
def testdata_by_postfix(postfix, request) -> str:
    """Run with `testdata_by_postfix("test2")` to load `day03_test2.txt`"""
    """Load data from a testfile."""
    year, day = parse_classname(request)
    filename = f"day{day:02}_{postfix}.txt"
    return read_file(year, day, filename)


@pytest.fixture
def solutiondata(request) -> str:
    """Load data from a solution file."""
    year, day = parse_classname(request)
    return read_file(year, day, f"day{day:02}.txt")
