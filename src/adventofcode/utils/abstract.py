import re
from abc import ABC, abstractmethod
from pathlib import Path


class AbstractSolution(ABC):
    @abstractmethod
    def solve(self, input_data: str) -> str | int:
        raise NotImplementedError


class SimpleSolution(AbstractSolution, ABC):
    """
    This solution implements a simple input_text that is used by the solve method.
    """

    def __call__(self, input_text: str) -> str | int:
        """
        Give the input_text as parameter, process this and return the result
        """
        res = self.solve(input_text)
        return res


class FileReaderSolution(AbstractSolution, ABC):
    """
    Implement filereader
    """

    def __call__(self, input_file: str) -> str | int:
        """
        Give the input_text as parameter, process this and return the result
        """
        # Find the year from the class. Convert self to string, and extract the year
        # after <adventofcode1234>
        year = re.findall("adventofcode([\d]{4})", str(self))
        if not year:
            raise ValueError("Path not found")
        else:
            year = int(year[0])
        root_dir = Path(__file__).parent.parent.parent
        with open(
            root_dir / f"adventofcode{year}" / "solutions" / "data" / input_file
        ) as f:
            input_data = f.read()
            res = self.solve(input_data=input_data)
            return res
