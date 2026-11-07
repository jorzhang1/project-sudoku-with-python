import clingo, sys
from sudoku_board import Sudoku

class Context:

    def __init__(self, board: Sudoku):
        # YOUR CODE HERE
        self.board = board
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        # YOUR CODE HERE
        symbols = []
        for (row, col), value in self.board.sudoku.items():
            symbols.append(clingo.Function("", [clingo.Number(row), clingo.Number(col), clingo.Number(value)]))
        return symbols

class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.load("sudoku.lp")
        ctl.ground()
        ctl.solve()

    def print_model(self, model, printer) -> None:
        formatted_model = Sudoku.from_model(model)
        print(formatted_model)

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())