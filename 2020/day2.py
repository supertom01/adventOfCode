from day_base import Day


class Day2(Day):
    
    def __init__(self):
        super(Day2, self).__init__(2020, 2, "Password Philosophy")

    def part_a(self):
        """
        Each line gives the policy for a password.

        The policy indicates the lowest and highest number of times a given letter must appear for the password to be
        valid.
        :return: The amount of passwords that are valid according to the policy
        """
        valid_passwords = 0
        for line in self.input:
            min_max, char, password = line.split(" ")
            min = int(min_max.split("-")[0])
            max = int(min_max.split("-")[1])
            char = char[0]

            char_count = sum(1 for c in password if c == char)
            if char_count <= max and char_count >= min:
                valid_passwords += 1

        return valid_passwords

    def part_b(self):
        """
        Each policy describes two positions in the password. Where the 1 indicates the first char. Exactly one of these
        two positions should contain the given letter.
        :return:
        """
        valid_passwords = 0
        for line in self.input:
            positions, char, password = line.split(" ")
            pos_1 = int(positions.split("-")[0]) - 1
            pos_2 = int(positions.split("-")[1]) - 1
            char = char[0]

            if (password[pos_1] == char and password[pos_2] != char) or (password[pos_2] == char and password[pos_1] != char):
                valid_passwords += 1

        return valid_passwords


if __name__ == '__main__':
    (Day2()).run()