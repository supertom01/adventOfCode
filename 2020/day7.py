import re

from day_base import Day


class Bag(object):

    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, bag, amount: int):
        self.children[bag.name] = {'bag': bag, 'amount': amount}

    def contains_bag(self, bag_name):
        if bag_name in self.children.keys():
            return True
        for child in self.children.values():
            if child['bag'].contains_bag(bag_name):
                return True
        return False

def parse_bag(bag):
    bag_name, other = bag.split(" bags contain ")
    other = other.replace(" bags", "").replace("bag.", "")
    bags = {}
    for inner_bag in other.split("bag, "):
        if inner_bag == "no other.":
            continue
        number, inner_bag_name = re.split("([0-9]+) ([a-z ]+)", inner_bag)[1:3]
        inner_bag_name = inner_bag_name[:-1] if inner_bag_name[-1] == " " else inner_bag_name
        bags[inner_bag_name] = int(number)
    return bag_name, bags


class Day7(Day):

    def __init__(self):
        super(Day7, self).__init__(2020, 7, "Handy Haversacks")

    def create_bag_structure(self):
        bags = {}
        for line in self.input:
            bag_name, inner_bags = parse_bag(line)
            if bag_name not in bags.keys():
                bags[bag_name] = Bag(bag_name)

            for bag, number in inner_bags.items():
                if bag not in bags.keys():
                    bags[bag] = Bag(bag)
                bags[bag_name].add_child(bags[bag], number)
        return bags

    def part_a(self):
        bag_name = "shiny gold"
        nr_bags = 0
        for bag, bag_obj in self.create_bag_structure().items():
            if bag_obj.contains_bag(bag_name):
                nr_bags += 1
        return nr_bags

    def part_b(self):
        pass


if __name__ == '__main__':
    (Day7()).run()