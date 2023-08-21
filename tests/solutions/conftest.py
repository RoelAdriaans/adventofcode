import pathlib

import pytest


def read_file(day: int, filename: str) -> str:
    """Load data from a file in data directory."""
    test_path = (
        pathlib.Path(__file__).parent.parent.parent
        / "src"
        / "adventofcode2016"
        / "solutions"
        / "data"
        / f"day_{day:02}"
        / filename
    )
    with open(test_path) as f:
        test_data = f.read()
    return test_data


def parse_classname(request) -> int:
    # Parse the class name
    day = int("".join(x for x in request.keywords.parent.name if x.isdigit()))
    return day


@pytest.fixture
def testdata(request) -> str:
    """Load data from a testfile."""
    postfix = request.node.get_closest_marker("postfix")
    day = parse_classname(request)
    if postfix is None:
        filename = f"day{day:02}_test.txt"
    else:
        filename = f"day{day:02}_{postfix}.txt"

    return read_file(day, filename)


@pytest.fixture
def solutiondata(request) -> str:
    """Load data from a solution file."""
    day = parse_classname(request)
    return read_file(day, f"day{day:02}.txt")
