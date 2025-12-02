from day_base import Day

class Day2(Day):

    def __init__(self):
        super().__init__(2025, 2, 'Gift Shop', debug=False, expected_a=1227775554, expected_b=4174379265)

    def part_a(self) -> int:
        ranges: list[list[str]] = [r.split('-') for r in self.input[0].split(",") if len(r.split('-')) > 0]

        faulty_number_sum = 0
        for [start, stop] in ranges:
            r = range(int(start), int(stop) + 1)
            for number in r:
                string = str(number)
                if len(string) % 2 == 0 and len(string) > 1:
                    first = string[:(len(string) // 2)]
                    second = string[(len(string) // 2):]
                    if first == second:
                        faulty_number_sum += number
        
        return faulty_number_sum
    
    def part_b(self) -> int:
        ranges: list[list[str]] = [r.split('-') for r in self.input[0].split(",") if len(r.split('-')) > 0]

        faulty_number_sum = 0
        for [start, stop] in ranges:
            for number in range(max(10, int(start)), int(stop) + 1):
                string = str(number)
                for i in range(1, len(string) // 2 + 1):
                    
                    if len(string) % i != 0:
                        continue

                    # Split the string into parts of i length
                    parts = [string[j:j+i] for j in range(0, len(string), i)]

                    # If we found at least one part and they're all identical we did a good job.
                    if len(parts) > 1 and len(set(parts)) == 1:
                        faulty_number_sum += number

                        # Go find the next number
                        break
        
        return faulty_number_sum

if __name__ == '__main__':
    (Day2()).run()
