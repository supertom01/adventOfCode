from day_base import Day


def find_gap(memory: list[int], block_length: int) -> int | None:
    """
    Find the first index of a gap in the given memory that is of the minimal length.
    """
    i = 0
    while i < len(memory):
        if memory[i] != -1:
            i += 1
        else:
            gap_size = 0
            gap_location = i

            # Determine the gap size
            while i < len(memory) and memory[i] == -1:
                i += 1
                gap_size += 1

            if gap_size >= block_length:
                return gap_location


class Day9(Day):

    def __init__(self):
        super().__init__(2024, 9, 'Disk Fragmenter', debug=False, expected_a=1928, expected_b=2858)

    def expand_disk(self):
        disk_map = [int(x) for x in self.input[0]]

        expanded_disk = []
        current_block_nr = 0
        block_lengths = dict()
        for i, v in enumerate(disk_map):
            if i % 2 == 0:
                # Register the location of this block
                block_lengths[current_block_nr] = v

                expanded_disk.extend([current_block_nr for _ in range(v)])
                current_block_nr += 1
            else:
                expanded_disk.extend([-1 for _ in range(v)])
        return expanded_disk, block_lengths
        
    def part_a(self):
        expanded_disk, _ = self.expand_disk()

        compacted_files = []
        ri = len(expanded_disk) - 1
        for li in range(len(expanded_disk)):
            if (char := expanded_disk[li]) != -1:
                compacted_files.append(char)
            else:
                # Move through the empty blocks on the right-hand side
                while (rv := expanded_disk[ri]) == -1:
                    ri -= 1

                # Make sure that we still haven't passed li:
                if li >= ri:
                    break

                compacted_files.append(rv)
                ri -= 1

            if li >= ri:
                break

        return sum(i * v for (i, v) in enumerate(compacted_files))

    def part_b(self) -> int:
        expanded_disk, block_lengths = self.expand_disk()

        ri = len(expanded_disk) - 1
        while ri >= 0:

            # Find the first block on the right of the expanded disk
            while (file_id := expanded_disk[ri]) == -1:
                ri -= 1

            block_length = block_lengths[file_id]

            # Only consider the memory that we have not seen yet
            location = find_gap(expanded_disk[:ri], block_length)

            # If no free block is available anymore, skip
            if location is None:
                ri -= block_length
                continue

            # Copy the block over
            for i in range(block_length):
                expanded_disk[location + i] = file_id

                # Remove the block from its old location
                expanded_disk[ri - i] = -1

            ri -= block_length

        return sum(i * v for (i, v) in enumerate(expanded_disk) if v != -1)

if __name__ == '__main__':
    (Day9()).run()

