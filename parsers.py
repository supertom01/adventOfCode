def parse_input_str(week_nr: int) -> list[str]:
    file_name = f"inputs/input_{week_nr}.txt"
    file = open(file_name, 'r')

    try:
        values = []
        for line in file.readlines():
            values.append(line)
    finally:
        file.close()

    return values


def parse_input_int(week_nr: int) -> list[int]:
    return list(map(int, parse_input_str(week_nr)))


def parse_input_float(week_nr: int) -> list[float]:
    return list(map(float, parse_input_str(week_nr)))