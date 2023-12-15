import numpy as np

from day_base import Day


def find_mirrors(matrices):
    found_mirrors = set()

    # Iterate both over the columns and rows
    for transpose in [True, False]:
        for matrix_index, matrix in enumerate(matrices):
            if matrix_index in [m[0] for m in found_mirrors]:
                continue

            matrix = np.transpose(matrix) if transpose else matrix
            for i in range(1, len(matrix)):
                min_length = min(i, len(matrix) - i)
                top = matrix[(i - min_length):i]
                bottom = matrix[i:(i + min_length)]
                if np.all(top == np.flip(bottom, axis=0)):
                    found_mirrors.add((matrix_index, transpose, i))
    return found_mirrors


class Day13(Day):

    def __init__(self):
        super().__init__(2023, 13, 'Point of Incidence', expected_a=405, expected_b=400, debug=False)

    def parse(self):
        # Parse the matrices
        matrices = []
        current_matrix = []
        for line in self.input:
            if line.strip() == '':
                matrices.append(np.array(current_matrix))
                current_matrix = []
            else:
                current_matrix.append([x == '#' for x in line])
        matrices.append(np.array(current_matrix))
        return matrices

    def part_a(self):
        matrices = self.parse()
        found_mirrors = find_mirrors(matrices)
        return sum(i if transposed else i * 100 for (matrix_index, transposed, i) in found_mirrors)

    def part_b(self) -> int:
        matrices = self.parse()
        original_mirrors = find_mirrors(matrices)

        total = 0
        unsmudged_mirrors = set()
        for transpose in [True, False]:
            for matrix_index, orig_matrix in enumerate(matrices):

                # Simply iterate over all the possible coordinates and fix a potential smudge.
                # This could be more optimized, by only including coordinates that were in the original mirror,
                # but for the input this was not that relevant.
                for (x, y) in [(x, y) for (x, row) in enumerate(orig_matrix) for (y, _) in enumerate(row)]:
                    # If this matrix was already resolved, then we do not have to check for mirrors again.
                    if matrix_index in unsmudged_mirrors:
                        break

                    # Fix possible smudge
                    matrix = orig_matrix.copy()
                    matrix[x][y] = not matrix[x][y]

                    # Check whether a new mirror can be found on either a column or a row.
                    matrix = np.transpose(matrix) if transpose else matrix
                    for i in range(1, len(matrix)):
                        min_length = min(i, len(matrix) - i)
                        top = matrix[(i - min_length):i]
                        bottom = matrix[i:(i + min_length)]
                        if np.all(top == np.flip(bottom, axis=0)):

                            # If this line was originally present, that it is not valid
                            if (matrix_index, transpose, i) in original_mirrors:
                                continue

                            if transpose:
                                total += i
                            else:
                                total += (i * 100)

                            # We found the mirror's location, there's no need to keep searching
                            unsmudged_mirrors.add(matrix_index)
                            break
        return total


if __name__ == '__main__':
    (Day13()).run()

