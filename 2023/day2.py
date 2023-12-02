from day_base import Day


class Day2(Day):

    def __init__(self):
        super().__init__(2023, 2, 'Cube Conundrum', expected_a=8, expected_b=2286, debug=False)

    def part_a(self) -> int:
        available_cubes = {"red": 12, "green": 13, "blue": 14}
        return sum(int(line.split(":")[0].split(" ")[1]) if all(all(available_cubes[cube_set[1::].split(" ")[1]] >= int(cube_set[1::].split(" ")[0]) for cube_set in play.split(",")) for play in line.split(":")[1].split(";")) else 0 for line in self.input)

    def part_a_2(self) -> int:
        available_cubes = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        possible_game_count = 0

        for line in self.input:
            game, plays = line.split(":")
            game_id = int(game.split(" ")[1])

            possible_game = True
            for play in plays.split(";"):
                for cube_set in play.split(","):
                    amount, color = cube_set[1::].split(" ")
                    possible_game = possible_game and available_cubes[color] >= int(amount)
            if possible_game:
                possible_game_count += game_id
        return possible_game_count

    def part_b(self) -> int:
        total_powers = 0

        for line in self.input:
            _, plays = line.split(":")
            minimal_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for play in plays.split(";"):
                for cube_set in play.split(","):
                    amount, color = cube_set[1::].split(" ")
                    if minimal_cubes[color] < int(amount):
                        minimal_cubes[color] = int(amount)
            total_powers += minimal_cubes["red"] * minimal_cubes["green"] * minimal_cubes["blue"]
        return total_powers


if __name__ == '__main__':
    (Day2()).run()
