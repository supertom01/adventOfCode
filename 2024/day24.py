from day_base import Day


def simulate(gates, wires):
    old_len = 0
    while len(wires) != old_len:
        old_len = len(wires)

        for (w1, w2, operation, out) in gates:
            if w1 in wires and w2 in wires and out not in wires:

                if operation == 'AND':
                    wires[out] = wires[w1] and wires[w2]
                elif operation == 'OR':
                    wires[out] = wires[w1] or wires[w2]
                elif operation == 'XOR':
                    wires[out] = wires[w1] != wires[w2]
                else:
                    raise NotImplementedError(operation)


class Day24(Day):

    def __init__(self):
        super().__init__(2024, 24, 'Crossed Wires', debug=False, expected_a=2024)

    def parse_data(self):
        wires: dict[str, bool] = dict()
        gates: list[tuple[str, str, str, str]] = list()

        collect_wires = True
        for line in self.input:
            if len(line) == 0:
                collect_wires = False
                continue

            if collect_wires:
                wire, value = line.split(': ')
                wires[wire] = value == '1'
            else:
                wire1, operation, wire2, _, wire_out = line.split(' ')
                gates.append((wire1, wire2, operation, wire_out))
        return gates, wires

    def part_a(self):
        gates, wires = self.parse_data()

        simulate(gates, wires)

        zs = sorted([(k, v) for (k, v) in wires.items() if k.startswith('z')], key=lambda k: k[0])
        return sum(2 ** i for i, (_, v) in enumerate(zs) if v)


if __name__ == '__main__':
    (Day24()).run()

