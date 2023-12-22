import math

from day_base import Day


class Node:

    def __init__(self, ranges: dict, workflow: str):
        self.children = []
        self.ranges = ranges
        self.workflow = workflow
        self.accepted = None

    def evaluate_workflow(self, workflows: dict):
        while self.accepted is None:
            if self.workflow == 'A':
                self.accepted = True
            elif self.workflow == 'R':
                self.accepted = False
            else:
                for condition, next_workflow in workflows[self.workflow]:
                    if type(condition) == str:
                        check_value = int((condition.split('>') if '>' in condition else condition.split('<'))[1])
                        category = condition[0]

                        if '<' in condition:
                            if self.ranges[category][1] < check_value:
                                # Accepted this check, so jump to the next workflow
                                self.workflow = next_workflow
                                break
                            elif self.ranges[category][0] >= check_value:
                                # This workflow is not accepted. So continue to the next rule
                                continue
                            else:
                                # Partially matched, split in a true and false case.
                                matching_ranges = self.ranges.copy()
                                matching_ranges[category] = (self.ranges[category][0], check_value - 1)
                                matching_node = Node(matching_ranges, next_workflow)

                                failing_ranges = self.ranges.copy()
                                failing_ranges[category] = (check_value, self.ranges[category][1])
                                failing_node = Node(failing_ranges, self.workflow)
                                self.children.append(matching_node)
                                self.children.append(failing_node)
                                matching_node.evaluate_workflow(workflows)
                                failing_node.evaluate_workflow(workflows)
                                self.accepted = False
                                break
                        else:
                            if self.ranges[category][0] > check_value:
                                # Accepted this check, so jump to the next workflow
                                self.workflow = next_workflow
                                break
                            elif self.ranges[category][1] <= check_value:
                                # This workflow is not accepted. So continue to the next rule
                                continue
                            else:
                                # Partially matched, split in a true and false case.
                                matching_ranges = self.ranges.copy()
                                matching_ranges[category] = (check_value + 1, self.ranges[category][1])
                                matching_node = Node(matching_ranges, next_workflow)

                                failing_ranges = self.ranges.copy()
                                failing_ranges[category] = (self.ranges[category][0], check_value)
                                failing_node = Node(failing_ranges, self.workflow)

                                self.children.append(matching_node)
                                self.children.append(failing_node)
                                matching_node.evaluate_workflow(workflows)
                                failing_node.evaluate_workflow(workflows)
                                self.accepted = False
                                break
                    else:
                        self.workflow = next_workflow

    def calculate_passing_combinations(self) -> int:
        if len(self.children) > 0:
            # A node with children is never accepted by itself, since it had to split in the first case.
            return sum(child.calculate_passing_combinations() for child in self.children)
        elif self.accepted:
            # The number of possibilities for a set of ranges is the product of their options.
            return math.prod(e - s + 1 for s, e in self.ranges.values())
        else:
            return 0


class Day19(Day):

    def __init__(self):
        super().__init__(2023, 19, 'Aplenty', expected_a=19114, expected_b=167409079868000, debug=False)

    def part_a(self):
        workflows = dict()
        parts = []

        parsing_workflows = True
        for line in self.input:
            if line.strip() == '':
                parsing_workflows = False
                continue

            if parsing_workflows:
                name, rules = line.split('{')
                rules = rules[:-1]  # Remove the last `}`
                r = []
                for rule in rules.split(','):
                    rule_condition = rule.split(':')
                    if len(rule_condition) == 2:
                        r.append((rule_condition[0], rule_condition[1]))
                    else:
                        r.append((True, rule_condition[0]))
                workflows[name] = r

            else:
                part = line[1:-1]
                part_dict = dict()
                for val in part.split(','):
                    category, score = val.split('=')
                    part_dict[category] = int(score)
                parts.append(part_dict)

        accepted_parts = []
        for part in parts:
            current_workflow = 'in'

            completed = False
            while not completed:
                for condition, next in workflows[current_workflow]:
                    if condition == True or eval(condition, None, part):

                        if next == 'A':
                            accepted_parts.append(part)
                            completed = True
                        elif next != 'R':
                            current_workflow = next
                        else:
                            completed = True
                        break

        return sum(sum(v for v in part.values()) for part in accepted_parts)

    def part_b(self) -> int:
        workflows = dict()
        for line in self.input:
            # No need to read the parts, so skip these
            if line.strip() == '':
                break

            name, rules = line.split('{')
            rules = rules[:-1]  # Remove the last `}`
            r = []
            for rule in rules.split(','):
                rule_condition = rule.split(':')
                if len(rule_condition) == 2:
                    r.append((rule_condition[0], rule_condition[1]))
                else:
                    r.append((True, rule_condition[0]))
            workflows[name] = r

        root = Node({
            'x': (1, 4000),
            'm': (1, 4000),
            'a': (1, 4000),
            's': (1, 4000),
        }, 'in')
        root.evaluate_workflow(workflows)
        return root.calculate_passing_combinations()


if __name__ == '__main__':
    (Day19()).run()
