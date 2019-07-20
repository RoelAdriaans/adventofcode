from collections import namedtuple
from utils.abstract import FileReaderSolution
import re


class Day3PartA(FileReaderSolution):
    square_size = 1_000
    map = None
    Claim = namedtuple("Claim", "id, left, top, width, heigth")

    def split_claim_into_sections(
        self, input_data: str
    ) -> Claim:  # NOQA: F821  Flake 8 does not find Clame
        """
        Split the input data `#1 @ 1,3: 4x4` into the parts:
        - ID 1
        - 1 from left edge
        - 3 from top egde
        - 4 width
        - 4 heigh

        return named tuple with the fields.

        :param input_data:
        :return:
        """
        pattern = (
            r"^#(?P<id>\d*) @ (?P<left>\d*),(?P<top>\d*): "
            r"(?P<width>\d*)x(?P<height>\d*)"
        )

        result = re.match(pattern, input_data)
        if result:
            claim = self.Claim(
                id=int(result["id"]),
                left=int(result["left"]),
                top=int(result["top"]),
                width=int(result["width"]),
                heigth=int(result["height"]),
            )
            return claim
        raise ValueError(f"String {input_data} could not be processed as a valid Claim")

    def make_map(self):
        self.map = dict()
        for i in range(0, self.square_size):
            self.map[i] = dict()
            for j in range(0, self.square_size):
                self.map[i][j] = []

    def _parse_claim(self, claim: Claim) -> bool:
        x = claim.left
        y = claim.top
        for i in range(x, x + claim.width):
            for j in range(y, y + claim.heigth):
                self.map[j][i].append(claim.id)
        return True

    def parse_claims(self, claims: [Claim]) -> bool:
        for claim in claims:
            self._parse_claim(claim)
        return True

    def print_map(self):
        for i in range(0, self.square_size):
            for j in range(0, self.square_size):
                claims_on_position = len(self.map[i][j])
                if claims_on_position == 0:
                    print(".", end="")
                elif claims_on_position == 1:
                    print(self.map[i][j][0], end="")
                else:
                    print("x", end="")
            print()

    def compute_multiple_claims(self) -> int:
        counter = 0
        for i in range(0, self.square_size):
            for j in range(0, self.square_size):
                if len(self.map[i][j]) > 1:
                    counter += 1
        return counter

    def solve(self, input_data: str) -> int:
        lines = input_data.split("\n")

        claims = [self.split_claim_into_sections(line) for line in lines if line]
        print(f"We have {len(claims)} claims")

        self.make_map()
        self.parse_claims(claims)
        # self.print_map()
        res = self.compute_multiple_claims()
        return res


class Day3PartB(FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return 0
