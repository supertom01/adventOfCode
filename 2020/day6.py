from day_base import Day


class Day6(Day):

    def __init__(self):
        super(Day6, self).__init__(2020, 6, "Custom Customs")

    def get_group_answers(self, anyone: bool):
        """
        Register for each group the answers that were answered with "yes".
        :param anyone: If anyone, then only one person has to answer yes in order to register the question. Otherwise
            everyone should answer yes to the question (union vs intersection)
        :return: A list of sets containing the answers for each group
        """
        groups = []
        current_group = set()
        new_line = True
        for line in self.input:
            if line == "":
                groups.append(current_group)
                new_line = True
            elif new_line:
                current_group = set(x for x in line)
                new_line = False
            elif anyone:
                current_group = current_group.union(set(x for x in line))
            else:
                current_group = current_group.intersection(set(x for x in line))
        groups.append(current_group)
        return groups

    def part_a(self):
        """
        The total sum of questions answered yes to by anyone in each group.
        :return:
        """
        return sum(len(group) for group in self.get_group_answers(anyone=True))

    def part_b(self):
        """
        The total sum of questions answered yes to by everyone in each group
        :return:
        """
        return sum(len(group) for group in self.get_group_answers(anyone=False))


if __name__ == '__main__':
    (Day6()).run()