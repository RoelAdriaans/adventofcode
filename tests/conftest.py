import pathlib
import re

import pytest


def read_file(year: int, day: int, filename: str, testdata: bool = True) -> str:
    """Load data from a file in data directory.

    arguments:
    year -- year of data
    day -- day of data
    filename -- file name
    testdata -- True when data is fetched from the testdata folder,
      false for solution data
    """
    if testdata:
        test_path = (
            pathlib.Path(__file__).parent
            / f"adventofcode{year}"
            / "testdata"
            / f"day_{day:02}"
            / filename
        )
    else:
        test_path = (
            pathlib.Path(__file__).parent.parent
            / "src"
            / "adventofcodedata"
            / f"adventofcode{year}"
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
    return read_file(year, day, f"day{day:02}.txt", testdata=False)
