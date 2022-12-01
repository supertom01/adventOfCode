from day_base import Day


class Day14(Day):

    def __init__(self):
        super().__init__(2020, 14, 'Docking Data', expected_a=165, debug=False)

    def part_a(self) -> int:
        mask = [-1 for _ in range(36)]
        memory = {}
        for line in self.input:
            left, right = line.split(" = ")
            if left == "mask":
                mask = [(-1 if x == "X" else int(x)) for x in right]
            else:
                mem_addr = int(left.replace("mem", "")[1:-1])
                value = int(right)

                # Apply the bit mask bit by bit
                for i in range(36):
                    mask_bit = mask[35 - i]
                    if mask_bit == 0:
                        # If the bit is not already zero, subtract 2**i effectively setting only that bit to zero
                        if value & 2**i != 0:
                            value -= 2**i
                    if mask_bit == 1:
                        # If the bit is not already set, add 2**i effectively setting only that bit to one
                        if value & 2**i == 0:
                            value += 2**i
                memory[mem_addr] = value
        return sum(memory.values())


if __name__ == '__main__':
    (Day14()).run()
