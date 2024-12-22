from day_base import Day


def calculate_next_number(secret_number):
    # Multiply by 64 and mix
    new_number = secret_number << 6
    secret_number = secret_number ^ new_number
    secret_number = secret_number & (16777216 - 1)
    # Divide by 32 and mix, and prune
    new_number = secret_number >> 5
    secret_number = secret_number ^ new_number
    secret_number = secret_number & (16777216 - 1)
    # Multiply by 2048 and mix,
    new_number = secret_number << 11
    secret_number = secret_number ^ new_number
    secret_number = secret_number & (16777216 - 1)
    return secret_number


class Day22(Day):

    def __init__(self):
        super().__init__(2024, 22, 'Monkey Market', debug=False)
        
    def part_a(self):
        total = 0
        for secret_number in self.input:
            secret_number = int(secret_number)
            for _ in range(2000):
                secret_number = calculate_next_number(secret_number)
            total += secret_number

        return total

    def part_b(self) -> int:
        buyers = []
        for secret_number in self.input:
            secret_number = int(secret_number)
            buyer = [secret_number % 10]

            for _ in range(2000):
                secret_number = calculate_next_number(secret_number)
                buyer.append(secret_number % 10)

            buyers.append(buyer)

        # Find the prices for each sequence
        buyer_sequence = dict()
        for buyer_idx, buyer in enumerate(buyers):
            seen_sequences = set()
            for i in range(2000 - 5):
                d1, d2, d3, d4 = buyer[i + 1] - buyer[i], buyer[i + 2] - buyer[i + 1], buyer[i + 3] - buyer[i + 2], buyer[i + 4] - buyer[i + 3]
                sequence = (d1, d2, d3, d4)
                price = buyer[i + 4]

                if sequence in seen_sequences:
                    continue
                seen_sequences.add(sequence)

                if sequence not in buyer_sequence.keys():
                    buyer_sequence[sequence] = 0
                buyer_sequence[sequence] += price

        max_sequence = max(buyer_sequence.keys(), key=lambda k: buyer_sequence[k])

        return buyer_sequence[max_sequence]



if __name__ == '__main__':
    (Day22()).run()

