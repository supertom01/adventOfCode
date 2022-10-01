import re

from day_base import Day


class Day4(Day):
    """
    FIXME: Part B is one higher than it should...
    """
    
    def __init__(self):
        super(Day4, self).__init__(2020, 4, "Passport Processing")

    def get_passports(self):
        passports = []
        prev_line = self.input[0]
        for line in self.input[1:]:
            if line == "":
                passports.append(prev_line)
                prev_line = ""
            else:
                prev_line += " " + line

        if prev_line != "":
            passports.append(prev_line)

        return passports


    def is_valid_passport(self, fields):
        for field in fields:
            key, value = field.split(":")
            if key == "byr" and (int(value) < 1920 or int(value) > 2002):
                return False
            elif key == "iyr" and (int(value) < 2010 or int(value) > 2020):
                return False
            elif key == "eyr" and (int(value) < 2020 or int(value) > 2030):
                return False
            elif key == "hgt":
                if "cm" in value:
                    size = int(value.replace("cm", ""))
                    if size < 150 or size > 193:
                        return False
                elif "in" in value:
                    size = int(value.replace("in", ""))
                    if size < 59 or size > 76:
                        return False
                else:
                    return False
            elif key == "hcl" and re.match('#[0-9a-f]{6}', value) is None:
                return False
            elif key == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
            elif key == "pid" and re.match('[0-9]{9}', value) is None:
                return False
        return True

    def part_a(self):
        valid_passwords = 0
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        for passport in self.get_passports():
            fields = list(filter(lambda x: x != "", passport.split(" ")))
            keys = {k for (k, _) in (field.split(":") for field in fields)}
            if len(required_fields - keys) == 0:
                valid_passwords += 1
        return valid_passwords

    def part_b(self):
        valid_passwords = 0
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        for passport in self.get_passports():
            fields = list(filter(lambda x: x != "", passport.split(" ")))
            keys = {k for (k, _) in (field.split(":") for field in fields)}
            if len(required_fields - keys) == 0:
                if self.is_valid_passport(fields):
                    valid_passwords += 1
        return valid_passwords


if __name__ == '__main__':
    (Day4()).run()
