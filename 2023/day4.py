import math
import re
from functools import reduce

from day_base import Day


class Day4(Day):

    def __init__(self):
        super().__init__(2023, 4, 'Scratchcards', expected_a=13, expected_b=30, debug=True)

    def calculate_scores(self):
        return [0] + [
            len(
                reduce(lambda x, y: x & y, (
                    set(int(x) if x != '' else None for x in re.split(r"\s+", nrs))
                    for nrs in line.split(": ")[1].split(" | ")
                )) - {None}
            )
            for line in self.input
        ]

    def part_a(self) -> int:
        return sum(math.pow(2, score - 1) if score > 0 else 0 for score in self.calculate_scores())

    def part_b(self) -> int:
        # First determine for each card the amount of points that we would receive
        scores = self.calculate_scores()
        cards = [0] + [1 for _ in range(len(self.input))]

        for card in range(len(cards)):
            for _ in range(cards[card]):
                for i in range(scores[card]):
                    if card + i + 1 < len(scores):
                        cards[card + i + 1] += 1

        return sum(cards)


if __name__ == '__main__':
    (Day4()).run()
