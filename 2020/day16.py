import numpy as np

from day_base import Day


def is_valid_ticket(valid_ranges, ticket):
    ticket = set(ticket)
    invalid_nrs = ticket - valid_ranges
    return len(invalid_nrs) == 0


class Day16(Day):

    def __init__(self):
        super().__init__(2020, 16, 'Ticket Translations', expected_a=None, debug=False)

    def parse_field_ranges(self):
        fields = dict()
        i = 0

        while self.input[i] != "":
            field, ranges = self.input[i].split(": ")
            valid_range = set()
            for r in ranges.split(" or "):
                start = int(r.split("-")[0])
                end = int(r.split("-")[1])
                valid_range.update(range(start, end + 1))
            fields[field] = valid_range
            i += 1
        return fields

    def part_a(self) -> int:
        # Determine the valid numbers
        field_ranges = self.parse_field_ranges()
        valid_ranges = set().union(*[r for r in field_ranges.values()])

        # Skip my ticket for now
        i = len(field_ranges) + 1
        while self.input[i] != "":
            i += 1

        # Find all the wrong values
        sum_wrong_values = 0
        i += 2  # Skips the text "nearby tickets"
        while i < len(self.input):
            ticket_nrs = set(int(nr) for nr in self.input[i].split(","))
            invalid_nrs = ticket_nrs - valid_ranges
            sum_wrong_values += sum(invalid_nrs)
            i += 1

        return sum_wrong_values

    def part_b(self) -> int:
        # Parse the input for this specific case
        field_ranges = self.parse_field_ranges()
        valid_ranges = set().union(*[r for r in field_ranges.values()])
        my_ticket = [int(x) for x in self.input[len(field_ranges) + 2].split(',')]

        # Filter out the invalid tickets from the nearby tickets
        nearby_tickets = [[int(f) for f in self.input[i].split(",")] for i in range(len(field_ranges) + 5, len(self.input))]
        valid_tickets = list(filter(lambda ticket: is_valid_ticket(valid_ranges, ticket), nearby_tickets))

        # The first step is to remove all locations which are not able to have the field according to the given ranges
        possible_locations = [set(field_ranges.keys()) for _ in range(len(field_ranges))]
        transpose = np.transpose(valid_tickets)
        for i in range(len(transpose)):
            field_values = set(transpose[i])
            for possible_field in field_ranges:
                if len(field_ranges[possible_field].union(field_values)) != len(field_ranges[possible_field]):
                    possible_locations[i].remove(possible_field)

        # Once all the rules have been processed, we need to remove duplicate values which are already determined
        confirmed_values = set()
        while len(confirmed_values) != len(field_ranges):
            for i, field in enumerate(possible_locations):
                if len(field) == 1:
                    confirmed_values.update(field)
                else:
                    possible_locations[i].difference_update(confirmed_values)

        # We now know the locations for each field, get all the values of the departures and calculate their product
        field_location = [x.pop() for x in possible_locations]
        multiplied_departure_fields = 1
        for i, field in enumerate(field_location):
            if 'departure' in field:
                multiplied_departure_fields *= my_ticket[i]
        return multiplied_departure_fields


if __name__ == '__main__':
    (Day16()).run()
