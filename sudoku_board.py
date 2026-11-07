from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        for i in range(1, 10):
            for j in range(1, 10):
                if j % 3 == 1 and j != 1:
                    s+= "  " + str(self.sudoku[(i, j)])
                elif j == 1: 
                    s += str(self.sudoku[(i, j)])
                else:
                    s += " " + str(self.sudoku[(i, j)])
            if i % 3 == 0 and i != 9:
                s += "\n\n"
            else:
                s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        row = 1
        for line in s.splitlines():
            if not line.strip():
                continue
            col = 1
            for number in line.split():
                if number != "-":
                    sudoku[(row,col)] = int(number)
                col += 1
            row += 1

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        symbols = model.symbols(shown=True)
        for symbol in symbols:
            key1  = symbol.arguments[0].number
            key2  = symbol.arguments[1].number
            sudoku[(key1, key2)] = symbol.arguments[2].number
        return cls(sudoku)
