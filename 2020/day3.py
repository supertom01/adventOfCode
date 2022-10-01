from functools import reduce
from day_base import Day


class Day3(Day):
    """
    With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy,
    it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which
    angles will take you near the fewest trees.

    Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your
    puzzle input) of the open squares (.) and trees (#) you can see.
    """
    
    def __init__(self):
        super(Day3, self).__init__(2020, 3, "Toboggan Trajectory")

    def part_a(self):
        """
        The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational
        numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
        :return: The amount of trees encountered on the map
        """
        i_max = len(self.input[0])
        i = 3
        tree_count = 0
        for line in self.input[1:]:
            if line[i] == '#':
                tree_count += 1
            i = (i + 3) % i_max
        return tree_count

    def part_b(self):
        """
        Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-
        left corner and traverse the map all the way to the bottom:

            Right 1, down 1.
            Right 3, down 1. (This is the slope you already checked.)
            Right 5, down 1.
            Right 7, down 1.
            Right 1, down 2.

        :return: The amount of trees found for each option, multiplied with each other
        """
        i_max = len(self.input[0])
        step_sizes = [1, 3, 5, 7, 1]
        tree_count = [0, 0, 0, 0, 0]
        curr_pos = [1, 3, 5, 7, 1]
        count = False
        for line in self.input[1:]:
            for i in range(len(curr_pos) - 1):
                if line[curr_pos[i]] == '#':
                    tree_count[i] += 1
                curr_pos[i] = (curr_pos[i] + step_sizes[i]) % i_max

            # Hacky stuff for skipping each other line...
            if not count:
                count = True
            else:
                count = False
                if line[curr_pos[4]] == '#':
                    tree_count[4] += 1
                curr_pos[4] = (curr_pos[4] + 1) % i_max

        return reduce(lambda x, y: x * y, tree_count)


if __name__ == '__main__':
    (Day3()).run()
