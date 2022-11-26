from day_base import Day


class Bag:
    """
    A bag that may contain other bags.

    A bag always has a name.
    Additionally, it may have bags inside it, called children.
    """

    def __init__(self, value):
        self.value = value
        self.children = []

    def get_name(self):
        return self.value

    def add_child(self, amount: int, value):
        self.children.append((amount, value))

    def contains_bag(self, bag_name):
        if self.value == bag_name:
            return True
        for _, bag in self.children:
            if bag.contains_bag(bag_name):
                return True
        return False

    def get_content_count(self):
        total = 1
        for amount, bag in self.children:
            total += amount * bag.get_content_count()
        return total

    def __str__(self):
        str_representation = self.value
        for amount, bag in self.children:
            str_representation += f" {amount}X {bag.get_name()}"
        return str_representation


class Day7(Day):

    def __init__(self):
        super(Day7, self).__init__(2020, 7, "Handy Haversacks", expected_a=4, expected_b=32)
        self.bags = {}
        self.nodes = {}

    def parse_input(self):
        """
        Generates a dictionary where each key is a unique key and the values are the bags inside it.
        """
        for line in self.input:
            bag_name, contents = line.split(" bags contain ")
            self.bags[bag_name] = []

            if "no other" in contents:
                continue
            contents = contents.replace(".", "").replace(" bags", "").replace(" bag", "")
            for bag in contents.split(", "):
                amount, pattern, color = bag.split(" ")
                self.bags[bag_name].append((int(amount), f"{pattern} {color}"))
        return self.bags

    def construct_tree(self):
        """
        Creates a tree where the nodes are dynamically being connected.

        First each bag gets its own empty node. Then they are being linked together, forming a tree.
        """
        self.parse_input()

        # Create empty nodes
        for bag_name in self.bags.keys():
            self.nodes[bag_name] = Bag(bag_name)

        # Connect the nodes together, but also storing the amount of bags at the same time
        for bag_name, contents in self.bags.items():
            for (amount, bag) in contents:
                self.nodes[bag_name].add_child(amount, self.nodes[bag])

    def part_a(self):
        """
        Determines the amount of bags that may contain a shiny gold bag.
        :return:
        """
        self.construct_tree()

        # Subtract one, since this method will include the shiny bag itself...
        return sum(1 for bag in self.bags if self.nodes[bag].contains_bag("shiny gold")) - 1

    def part_b(self):
        """
        Determines the amount of bags that would be located within a shiny gold bag.
        :return:
        """
        self.construct_tree()

        # Subtract one, since this method will include the shiny bag itself...
        return self.nodes["shiny gold"].get_content_count() - 1


if __name__ == '__main__':
    (Day7()).run()
