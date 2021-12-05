import time

from days.day import Day
import numpy as np


def get_score(board, last_number: int):
    s = sum(sum(item[0] for item in row if not item[1]) for row in board)
    return s * last_number


class Day4(Day):

    def __init__(self):
        super().__init__(4, "Giant Squid", input_type="str")
        self.drawn_numbers = list(map(int, self.input[0].split(",")))
        self.boards = None

    def get_boards(self):
        boards = []
        board = []
        for line in self.input[2:]:
            if line == "":
                boards.append(board)
                board = []
            else:
                board.append([[int(nr), False] for nr in filter(lambda x: x != "", line.split(" "))])
        boards.append(board)
        return boards

    def mark_boards(self, nr: int):
        self.boards = [[[[n, b or n == nr] for [n, b] in row] for row in board] for board in self.boards]

    def get_bingo(self):
        for board in self.boards:
            b = np.array(board)
            for row, col in zip(b, b.transpose((1, 0, 2))):
                if all([x[1] for x in row]) or all([x[1] for x in col]):
                    return board
        return None

    def get_all_bingos(self):
        bingos = []
        for board in self.boards:
            b = np.array(board)
            for row, col in zip(b, b.transpose((1, 0, 2))):
                if all([x[1] for x in row]) or all([x[1] for x in col]):
                    bingos.append(board)
                    break
        return bingos

    def part_a(self):
        self.boards = self.get_boards()

        i = 0
        bingo_board = None
        while bingo_board is None:
            self.mark_boards(self.drawn_numbers[i])
            bingo_board = self.get_bingo()
            i += 1
        i -= 1
        return get_score(bingo_board, self.drawn_numbers[i])

    def part_b(self):
        self.boards = self.get_boards()
        i = 0
        while len(self.boards) > 1:
            self.mark_boards(self.drawn_numbers[i])
            self.boards = [x for x in self.boards if x not in self.get_all_bingos()]
            i += 1
        while self.get_bingo() is None:
            self.mark_boards(self.drawn_numbers[i])
            i += 1
        i -= 1
        return get_score(self.boards[0], self.drawn_numbers[i])


if __name__ == '__main__':
    Day4().run()
