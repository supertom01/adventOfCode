import enum
from copy import deepcopy

from day_base import Day


# Cached coordinates for seats in a line of sight (since calculating this is quite some work...)
seats_in_view_coordinate_cache = []


class Seat(enum.Enum):
    """
    The status of a single seat.
    Either there is not even a seat (floor), or there is; in which case it is either empty or occupied
    """
    FLOOR = 0
    EMPTY = 1
    OCCUPIED = 2


def get_adjacent_seats(floor_plan, i, j):
    """
    Get the status of all the adjacent seats for the given floor plan

    :param floor_plan: The floor plan containing the current status of all the seats
    :param i: The row of the seat
    :param j: The column of the seat
    :return: The status of each adjacent seat
    """
    adjacent_seats = []

    # Seats are between 0, max_x and max_y
    for k in range(max(i - 1, 0), min(i + 2, len(floor_plan))):
        for l in range(max(j - 1, 0), min(j + 2, len(floor_plan[i]))):
            if k == i and l == j:
                continue
            adjacent_seats.append(floor_plan[k][l])
    return adjacent_seats


def get_seats_in_view(floor_plan, i, j):
    """
    Get the status of all the seats in the line of sight for the given floor plan and seat.

    This function makes use of caching for the coordinates of the seats that are in the line of sight,
    since constantly re-calculating these takes a lot of time.

    :param floor_plan: The floor plan containing the current status of all the seats
    :param i: The row of the seat
    :param j: The column of the seat
    :return: The status of each seat within the line of sight of the given seat.
    """

    # Check if cache is available
    global seats_in_view_coordinate_cache
    if len(seats_in_view_coordinate_cache) == 0:
        seats_in_view_coordinate_cache = [[[] for _ in row] for row in floor_plan]
    elif len(seats_in_view_coordinate_cache[i][j]) != 0:
        return [floor_plan[k][l] for (k, l) in seats_in_view_coordinate_cache[i][j]]

    # Cache is not yet available, start discovering coordinates
    seats_in_view = []

    # North-West direction
    for k in range(1, min(i, j) + 1):
        if floor_plan[i - k][j - k] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i - k][j - k])
            seats_in_view_coordinate_cache[i][j].append((i - k, j - k))
            break

    # North direction
    for k in range(1, i + 1):
        if floor_plan[i - k][j] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i - k][j])
            seats_in_view_coordinate_cache[i][j].append((i - k, j))
            break

    # North-East direction
    for k in range(1, min(i + 1, len(floor_plan[i]) - j)):
        if floor_plan[i - k][j + k] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i - k][j + k])
            seats_in_view_coordinate_cache[i][j].append((i - k, j + k))
            break

    # West direction
    for k in range(1, j + 1):
        if floor_plan[i][j - k] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i][j - k])
            seats_in_view_coordinate_cache[i][j].append((i, j - k))
            break

    # East direction
    for k in range(1, len(floor_plan[i]) - j):
        if floor_plan[i][j + k] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i][j + k])
            seats_in_view_coordinate_cache[i][j].append((i, j + k))
            break

    # South-West direction
    for k in range(1, min(len(floor_plan) - i, j + 1)):
        if floor_plan[i + k][j - k] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i + k][j - k])
            seats_in_view_coordinate_cache[i][j].append((i + k, j - k))
            break

    # South direction
    for k in range(1, len(floor_plan) - i):
        if floor_plan[i + k][j] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i + k][j])
            seats_in_view_coordinate_cache[i][j].append((i + k, j))
            break

    # South-East direction
    for k in range(1, min(len(floor_plan) - i, len(floor_plan[i]) - j)):
        if floor_plan[i + k][j + k] != Seat.FLOOR:
            seats_in_view.append(floor_plan[i + k][j + k])
            seats_in_view_coordinate_cache[i][j].append((i + k, j + k))
            break

    return seats_in_view


def print_floor_plan(floor_plan: list[list[Seat]]):
    """
    Prints the floor plan in a human-readable form.

    Only used for debugging purposes
    :param floor_plan:
    :return:
    """
    for row in floor_plan:
        string = ""
        for seat in row:
            if seat == Seat.OCCUPIED:
                string += "#"
            elif seat == Seat.EMPTY:
                string += "L"
            elif seat == Seat.FLOOR:
                string += "."
        print(string)
    print()


class Day11(Day):

    def __init__(self):
        super().__init__(2020, 11, 'Seating System', expected_a=37, expected_b=26, debug=False)

        # Parse the input
        self.floor_plan = []
        for line in self.input:
            row = []
            for spot in line:
                if spot == "L":
                    row.append(Seat.EMPTY)
                elif spot == "#":
                    row.append(Seat.OCCUPIED)
                elif spot == ".":
                    row.append(Seat.FLOOR)
                else:
                    raise RuntimeError(f"Invalid seating found: {spot}")
            self.floor_plan.append(row)

    def part_a(self):
        """
        Determine if a seat is being switched from occupied to empty. Based on adjacent seats
        :return:
        """
        prev_floor_plan = deepcopy(self.floor_plan)
        this_floor_plan = deepcopy(self.floor_plan)

        while True:
            # Update the floor plan model
            for i in range(len(self.floor_plan)):
                for j in range(len(self.floor_plan[i])):
                    current_seat = prev_floor_plan[i][j]

                    # No need to look at the floor
                    if current_seat == Seat.FLOOR:
                        continue

                    adjacent_seats = get_adjacent_seats(prev_floor_plan, i, j)
                    if current_seat == Seat.EMPTY and Seat.OCCUPIED not in adjacent_seats:
                        this_floor_plan[i][j] = Seat.OCCUPIED
                    elif current_seat == Seat.OCCUPIED and len(
                            [seat for seat in adjacent_seats if seat == Seat.OCCUPIED]) >= 4:
                        this_floor_plan[i][j] = Seat.EMPTY

            # Once the floor plan does no longer update, we're done
            if prev_floor_plan == this_floor_plan:
                break
            prev_floor_plan = deepcopy(this_floor_plan)

        return sum(sum(1 for location in row if location == Seat.OCCUPIED) for row in this_floor_plan)

    def part_b(self):
        """
        Determine if a seat is being switched from occupied to empty. Based on the line of sight
        :return:
        """
        prev_floor_plan = deepcopy(self.floor_plan)
        this_floor_plan = deepcopy(self.floor_plan)

        while True:
            # Update the floor plan model
            for i in range(len(self.floor_plan)):
                for j in range(len(self.floor_plan[i])):
                    current_seat = prev_floor_plan[i][j]

                    # No need to look at the floor
                    if current_seat == Seat.FLOOR:
                        continue

                    seats_in_view = get_seats_in_view(prev_floor_plan, i, j)
                    if current_seat == Seat.EMPTY and Seat.OCCUPIED not in seats_in_view:
                        this_floor_plan[i][j] = Seat.OCCUPIED
                    elif current_seat == Seat.OCCUPIED and len(
                            [seat for seat in seats_in_view if seat == Seat.OCCUPIED]) >= 5:
                        this_floor_plan[i][j] = Seat.EMPTY

            # Once the floor plan does no longer update, we're done
            if prev_floor_plan == this_floor_plan:
                break
            prev_floor_plan = deepcopy(this_floor_plan)

        return sum(sum(1 for location in row if location == Seat.OCCUPIED) for row in this_floor_plan)


if __name__ == '__main__':
    (Day11()).run()
