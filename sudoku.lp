% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

row(1..9).
col(1..9).
num(1..9).

% subgrid uses the formula in the Hints, can change n in original formula to actual grid size
subgrid(X,Y,G) :- row(X), col(Y), G = 1 + (((X-1)/3)*3) + (Y-1)/3.

% for every combination of row x and col y, choose exactly 1 sudoku, where N is a valid number
1 { sudoku(X,Y,N) : num(N) } 1 :- row(X), col(Y).

% constraints: don't allow the same number in the same row or column or subgrid
:- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 != Y2.
:- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 != X2.

:- subgrid(X1,Y1,G), sudoku(X1,Y1,N), subgrid(X2,Y2,G), sudoku(X2,Y2,N), X1 != X2.

% ensures initial solutions exist
sudoku(X,Y,N) :- initial(X,Y,N).


#show sudoku/3.
