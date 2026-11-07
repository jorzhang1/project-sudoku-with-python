import clingo, sys
import sudoku_board

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
        formatted_model = sudoku_board.Sudoku.from_model(model)
        print(formatted_model)

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())