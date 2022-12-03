from day_base import Day


ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_priorities():
    """
    Creates a map from character to priority
    """
    priorities = {}
    for index, letter in zip(range(len(ALPHABET)), ALPHABET):
        priorities[letter] = index + 1
        priorities[letter.upper()] = index + 27
    return priorities


class Day3(Day):

    def __init__(self):
        super().__init__(2022, 3, 'Rucksack Reorganization', expected_a=157, expected_b=70, debug=False)

    def part_a(self) -> int:
        """
        Determines for each bag which item is shared between two compartments.
        The priorities are for each shared item are calculated and the sum is returned.
        :return: The total sum of the priorities for the items that occur in both compartments
        """
        common_items = []
        for line in self.input:
            center = int(len(line) / 2)
            compartment_1 = set(line[:center])
            compartment_2 = set(line[center:])
            shared_items = compartment_1.intersection(compartment_2)
            common_items.append(shared_items.pop())
        priorities = get_priorities()
        return sum(priorities[item] for item in common_items)

    def part_b(self) -> int:
        """
        Determines the badge that each group of three elves is wearing with them.
        The priority for each badge is calculated and the total sum of all priorities for the badges is returned.
        :return: The total sum of the priorities for the badges in each three groups of elves
        """
        badges = []
        for i in range(0, len(self.input), 3):
            rucksacks = self.input[i:i+3]
            badge = set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2]))
            badges.append(badge.pop())
        priorities = get_priorities()
        return sum(priorities[badge] for badge in badges)


if __name__ == '__main__':
    (Day3()).run()
