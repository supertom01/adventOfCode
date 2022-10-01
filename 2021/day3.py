from day_base import Day


class Day3(Day):

    def __init__(self):
        super().__init__(3, "Binary Diagnostic", input_type="str")

    def part_a(self):
        """
        The input is a list of binary numbers.
        The gamma value is determined by the most common bit along each bit index.
        The epsilon value is determined by the least common bit along each bit index.
        :return: gamma * epsilon
        """
        # Split all binary numbers of a list, where each list consists out of separate digits: [[1,0,1], [0,0,1]]
        numbers = [[int(x) for x in number] for number in self.input]

        # Sum all digits up on the same indices. If the sum is bigger than half of the total number of inputs, the digit
        # 1 is dominant, otherwise 0 is dominant.
        gamma = [int(val > (len(numbers) / 2)) for val in [sum(x[i] for x in numbers) for i in range(len(numbers[0]))]]

        # The value for epsilon is flipped, so flip the digits.
        epsilon = [int(not bool(x)) for x in gamma]

        # Convert the lists of digits to decimal values and multiply them.
        return int("".join(map(str, gamma)), 2) * int("".join(map(str, epsilon)), 2)

    def part_b(self):
        """
        The oxygen rating is determined by getting the most common value in a bit position and removing each number that
        does not adhere to this bit. Then we shift one position to the right and repeat this step, till there's one left
        If the number is equal, choose all the values with 1.
        The co2 rating is flipped, we want the least common value, if the number is equal, we choose all values with 0.
        :return:
        """
        oxygen_rating_list = [[int(c) for c in nr] for nr in self.input]
        co2_rating_list = [[int(c) for c in nr] for nr in self.input]

        result = []

        i = 0
        for rating in [oxygen_rating_list, co2_rating_list]:
            j = 0
            while len(rating) > 1:
                test = sum(x[j] for x in rating)
                if test >= len(rating) / 2:
                    # 1 is the dominant bit.
                    decision = (i + 1) % 2
                else:
                    # 0 is the dominant bit.
                    decision = i
                rating = list(filter(lambda x: x[j] == decision, rating))
                j += 1
            result.append(rating[0])
            i += 1

        oxygen_rating = int("".join(map(str, result[0])), 2)
        co2_rating = int("".join(map(str, result[1])), 2)

        return oxygen_rating * co2_rating


if __name__ == '__main__':
    Day3().run()