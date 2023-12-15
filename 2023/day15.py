import math

from day_base import Day


def hash(value) -> int:
    curr = 0
    for c in value:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr


class Day15(Day):

    def __init__(self):
        super().__init__(2023, 15, 'Lens Library', expected_a=1320, expected_b=145, debug=True)

    def part_a(self):
        return sum(hash(value) for value in self.input[0].split(','))

    def part_b(self) -> int:
        boxes = dict()

        for value in self.input[0].split(','):
            if '=' in value:
                box, focal_length = value.split('=')
            else:
                box = value[:-1]

            # Determines the box nr
            box_nr = hash(box)

            # Create the box if needed
            if box_nr not in boxes.keys():
                boxes[box_nr] = []

            # Add a lens with a given label and focal length
            if '=' in value:

                # Check if we have to replace a value.
                replaced = False
                for i, (label, _) in enumerate(boxes[box_nr]):
                    if label == box:
                        lenses = boxes[box_nr]
                        lenses[i] = (box, int(focal_length))
                        boxes[box_nr] = lenses
                        replaced = True
                        break

                # If it was not replaced, then simply append the lens
                if not replaced:
                    boxes[box_nr].append((box, int(focal_length)))

            # If we need to remove the lens, just filter the list on that lens label
            else:
                boxes[box_nr] = list(filter(lambda x: x[0] != box, boxes[box_nr]))

        return sum(
            sum(math.prod([box_nr + 1, slot + 1, focal_length])
                for slot, (_, focal_length) in enumerate(lenses)
            ) for box_nr, lenses in boxes.items()
        )


if __name__ == '__main__':
    (Day15()).run()
