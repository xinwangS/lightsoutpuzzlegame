# lightsoutpuzzlegame
 We will consider the Lights Out puzzle.
In this puzzle, there is an n × m board of cells, each of which is On or Off.
The puzzle starts out with some cells On and some Off. In each move, the
player chooses one cell; that cell and all adjacent cells are toggled (i.e. On
turns to Off, and Off turns to On). Cells count as adjacent horizontally or
vertically, but not diagonally. In other words, targeting a cell in the center of
the board toggles a total of five cells; a move on the side toggles four; and a
move in the corner toggles three. The goal of the game is to change all cells
to the Off position in as few moves as possible.
You can try playing Lights Out yourself at:
http://www.neok12.com/games/lights-out/lights-out.htm

Implement two functions to solve the Lights Out puzzle, using
each of the following algorithms respectively: Depth-First, Breadth-First,
Each function shouldtake a puzzle as input and return a list of moves that solves the puzzle. In
addition, each function should output the number of steps it took to find
the solution, measured by the number of times the search algorithm used
perform move() to find the next board state
