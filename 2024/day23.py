from day_base import Day

class Day23(Day):

    def __init__(self):
        super().__init__(2024, 23, 'LAN Party', debug=False, expected_a=7)

    def part_a(self):
        # Find to which computer each other computer is connected
        graph = dict()
        for line in self.input:
            c1, c2 = line.split('-')

            if c1 not in graph:
                graph[c1] = []
            graph[c1].append(c2)

            if c2 not in graph:
                graph[c2] = []
            graph[c2].append(c1)

        # Find all inter-connected computers
        inter_connected_computers = set()
        for c1, computers in graph.items():
            for c2 in computers:
                for c3 in graph[c2]:
                    if c3 in computers and any(c.startswith('t') for c in [c1, c2, c3]):
                        inter_connected_computers.add(frozenset([c1, c2, c3]))

        return len(inter_connected_computers)

if __name__ == '__main__':
    (Day23()).run()

