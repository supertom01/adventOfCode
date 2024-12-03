import os


def generate_day(day_nr: int, year: int, description=None):
    text = f'''from day_base import Day


class Day{day_nr}(Day):

    def __init__(self):
        super().__init__({year}, {day_nr}, '{description if description is not None else 'description'}')
        
    def part_a(self):
        pass


if __name__ == '__main__':
    (Day{day_nr}()).run()

'''

    # Create the directory for this year, if it doesn't exist yet.
    os.makedirs(f"{year}/", exist_ok=True)
    os.makedirs(f"test/{year}/", exist_ok=True)

    with open(f"{year}/day{day_nr}.py", "x") as python_file:
        python_file.write(text)
    with open(f"test/{year}/{day_nr}.txt", "x") as _:
        pass

    print("Successfully created day.py and test input files.")


if __name__ == '__main__':
    generate_day(3, 2024)
