from adventofcodeutils.stack import Stack

from adventofcode2021.utils.abstract import FileReaderSolution


class Day10:
    CHARATERS = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    COMPLETE_CHARACTERS = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    @staticmethod
    def parse_chunk(chunk) -> bool | str:
        """Parse a chunk and return the first invalid character. If the chunk is valid,
        return True"""
        stack: Stack[str] = Stack()
        # Start adding and popping from the stack
        for char in chunk:
            if char in ("(", "[", "{", "<"):
                stack.push(char)
            else:
                popped = stack.pop()
                if char == "]" and popped == "[":
                    continue
                elif char == ")" and popped == "(":
                    continue
                elif char == "}" and popped == "{":
                    continue
                elif char == ">" and popped == "<":
                    continue
                else:
                    return char
        return True

    @staticmethod
    def complete_chunk(chunk) -> str:
        """Complete a chunk. Chunk must be valid, just missing data"""
        stack: Stack[str] = Stack()
        # Start adding and popping from the stack
        for char in chunk:
            if char in ("(", "[", "{", "<"):
                stack.push(char)
            else:
                stack.pop()
        # Resulting characters in the stack must be completed
        missing = []
        while not stack.empty:
            char = stack.pop()
            match char:
                case "<":
                    missing.append(">")
                case "(":
                    missing.append(")")
                case "[":
                    missing.append("]")
                case "{":
                    missing.append("}")
        return "".join(missing)

    def compute_score(self, char) -> int:
        return self.CHARATERS[char]


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        chunks = input_data.splitlines()
        invalid_characters = [self.parse_chunk(chunk) for chunk in chunks]
        score = sum(
            self.compute_score(char) for char in invalid_characters if char is not True
        )
        return score


class Day10PartB(Day10, FileReaderSolution):
    def compute_complete_score(self, input_string) -> int:
        score = 0
        for char in input_string:
            score *= 5
            score += self.COMPLETE_CHARACTERS[char]

        return score

    def solve(self, input_data: str) -> int:
        # First compute all the valid strings
        valid = [
            chunk
            for chunk in input_data.splitlines()
            if self.parse_chunk(chunk) is True
        ]

        scores = [
            self.compute_complete_score(self.complete_chunk(chunk)) for chunk in valid
        ]
        sorted_scores = sorted(scores)

        # Compute middle and return the score
        middle = len(sorted_scores) // 2
        return sorted_scores[middle]
