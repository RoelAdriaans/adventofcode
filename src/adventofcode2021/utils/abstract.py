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
        root_dir = Path(__file__).parent.parent
        with open(root_dir / "solutions" / "data" / input_file) as f:
            input_data = f.read()
            res = self.solve(input_data=input_data)
            return res
