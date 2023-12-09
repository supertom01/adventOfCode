import functools

from day_base import Day


class Day9(Day):

    def __init__(self):
        super().__init__(2023, 9, 'Mirage Maintenance', expected_a=114, expected_b=2, debug=False)

    def predict(self, predict_future: bool):
        """
        Either predicts the future or history of the measurements that have been taken.

        :param predict_future If true, we predict future values, otherwise we predict historic values.
        """
        prediction_sum = 0
        for history in self.input:
            # Map the line into individual measurements and reverse them.
            measurements = list(reversed(list(map(int, history.split(" ")))))

            # Fill the stack with simplified measurements, till all of them are 0.
            stack = [measurements]
            while any(v != 0 for v in stack[-1]):
                stack.append([stack[-1][i] - stack[-1][i + 1] for i in range(len(stack[-1]) - 1)])

            # Determine the prediction (different formula needed for future or historical predictions)
            prediction_sum += sum([s[0] for s in stack]) if predict_future else functools.reduce(lambda s0, s1: s1[-1] - s0, reversed(stack), 0)
        return prediction_sum

    def part_a(self) -> int:
        return self.predict(predict_future=True)

    def part_b(self) -> int:
        return self.predict(predict_future=False)


if __name__ == '__main__':
    (Day9()).run()
