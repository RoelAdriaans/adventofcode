import pathlib

import pytest


@pytest.fixture
def testdata(request) -> str:
    """Load data from a testfile.
    If `filename` is given, this file is loaded, otherwise the default `daynn_test.txt`
    file is used.
    """

    # Parse the class name, eg
    day = int("".join(x for x in request.keywords.parent.name if x.isdigit()))

    test_path = (
        pathlib.Path(__file__).parent.parent.parent
        / "src"
        / "adventofcode2016"
        / "solutions"
        / "data"
        / f"day_{day:02}"
        / f"day{day:02}_test.txt"
    )
    with open(test_path) as f:
        test_data = f.read()
    return test_data
