import re
from collections import namedtuple

from adventofcode.utils.abstract import FileReaderSolution


class Day3:
    square_size = 1_000
    Claim = namedtuple("Claim", "id, left, top, width, height")

    def split_claim_into_sections(self, input_data: str) -> "Claim":
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
                height=int(result["height"]),
            )
            return claim
        raise ValueError(f"String {input_data} could not be processed as a valid Claim")

    def make_map(self):
        self.map: dict[int, dict] = dict()
        for i in range(0, self.square_size):
            self.map[i] = dict()
            for j in range(0, self.square_size):
                self.map[i][j] = []

    def _parse_claim(self, claim: Claim) -> bool:
        x = claim.left
        y = claim.top
        for i in range(x, x + claim.width):
            for j in range(y, y + claim.height):
                self.map[j][i].append(claim.id)
        return True

    def parse_claims(self, claims: list[Claim]) -> bool:
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
        """Compute how many claims are overlapping"""
        counter = 0
        for i in range(0, self.square_size):
            for j in range(0, self.square_size):
                if len(self.map[i][j]) > 1:
                    counter += 1
        return counter

    def compute_unclaimed_id(self) -> int:
        """
        Compute the ID of the Claim that is not overlapping with other claims
        :return: False if there is no overlapping claim
        """
        valid_claims: list = []
        invalid_claims: list = []
        for i in range(0, self.square_size):
            for j in range(0, self.square_size):
                claims_on_position = len(self.map[i][j])
                if claims_on_position == 1:
                    claim_id = self.map[i][j][0]
                    if claim_id not in invalid_claims and claim_id not in valid_claims:
                        # We have a valid claim that has no overlapping claims
                        valid_claims.append(claim_id)
                elif claims_on_position > 1:
                    # We have two claims that are overlapping each other.
                    # Adding them to the invalid_claims, removing them from the valid
                    for claim in self.map[i][j]:
                        if claim not in invalid_claims:
                            invalid_claims.append(claim)
                        if claim in valid_claims:
                            valid_claims.remove(claim)
        return valid_claims[0]

    def build_map(self, input_data):
        """
        Use the Claims input_data to create a map of claims

        :param input_data:
        :return: Nothing
        """
        lines = input_data.split("\n")

        claims = [self.split_claim_into_sections(line) for line in lines if line]
        self.make_map()
        self.parse_claims(claims)


class Day3PartA(Day3, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.build_map(input_data)
        # self.print_map()
        res = self.compute_multiple_claims()
        return res


class Day3PartB(Day3, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.build_map(input_data)
        # self.print_map()
        res = self.compute_unclaimed_id()
        return res
