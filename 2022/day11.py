import math

from day_base import Day
import parse


class Day11(Day):

    def __init__(self):
        super().__init__(2022, 11, 'Monkey in the Middle', input_type="raw", expected_a=10605, expected_b=2713310158, debug=False)

    def parse(self):
        monkeys = []
        for monkey in self.input.split("\n\n"):
            m = parse.parse("Monkey {id:n}:\n  Starting items: {items}\n  Operation: new = {formula}\n"
                            "  Test: divisible by {divider:n}\n    If true: throw to monkey {true_monkey:n}\n"
                            "    If false: throw to monkey {false_monkey:n}", monkey)
            monkey_dict = m.named
            monkey_dict["items"] = list(map(int, monkey_dict["items"].split(", ")))
            monkeys.append(monkey_dict)
        return monkeys

    def play_game(self, nr_of_rounds):
        monkeys = self.parse()
        items_inspected = [0 for _ in range(len(monkeys))]
        for _ in range(nr_of_rounds):
            for i in range(len(monkeys)):
                for item in monkeys[i]['items']:
                    items_inspected[i] += 1
                    worry_level = eval(monkeys[i]['formula'].replace("old", str(item)))
                    if nr_of_rounds == 20:
                        worry_level = math.floor(worry_level / 3.0)
                    if worry_level % monkeys[i]['divider'] == 0:
                        monkeys[monkeys[i]['true_monkey']]['items'].append(worry_level)
                    else:
                        monkeys[monkeys[i]['false_monkey']]['items'].append(worry_level)
                monkeys[i]['items'] = []

        sorted_items = sorted(items_inspected, reverse=True)
        return sorted_items[0] * sorted_items[1]

    def part_a(self) -> int:
        return self.play_game(20)

    # def part_b(self) -> int:
    #     return self.play_game(10000)


if __name__ == '__main__':
    (Day11()).run()
