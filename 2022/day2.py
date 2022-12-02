import enum

from day_base import Day


class Day2(Day):

    def __init__(self):
        super().__init__(2022, 2, 'Rock Paper Scissors', expected_a=15, expected_b=12, debug=False)

    def parse(self):
        available_moves = {
            'A': 0,  # Rock
            'B': 1,  # Paper
            'C': 2,  # Scissors
            'X': 0,  # Lose
            'Y': 1,  # Draw
            'Z': 2   # Win
        }
        matches = []
        for line in self.input:
            match = []
            for val in line.split(' '):
                match.append(available_moves[val])
            matches.append(match)
        return matches

    def part_a(self) -> int:
        """
        Determines the outcome of each game (lose, draw or win) and calculates the total score
        """
        matches = self.parse()
        point_total = 0
        for match in matches:
            outcome = match[1] - match[0]
            if outcome == 1 or outcome == -2:
                # We won!
                point_total += 6 + (match[1] + 1)
            elif outcome == 0:
                # Draw
                point_total += 3 + (match[1] + 1)
            else:
                # We've lost
                point_total += match[1] + 1
        return point_total

    def part_b(self) -> int:
        """
        Determines the move in order to adhere to the expected outcome (lose, draw or win) and calculates the total score
        """
        matches = self.parse()
        point_total = 0
        for match in matches:
            if match[1] == 0:
                # We need to lose
                point_total += (match[0] - 1) % 3 + 1
            elif match[1] == 1:
                # We make a draw
                point_total += 3 + (match[0] + 1)
            else:
                # We have to win
                point_total += 6 + (match[0] + 1) % 3 + 1
        return point_total


if __name__ == '__main__':
    (Day2()).run()
