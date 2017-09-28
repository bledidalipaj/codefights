



import copy

possible_moves = set([m for m in '123456789'])

class Sudoku(object):
    def __init__(self, puzzle_str):
        self.rows = [set() for r in range(9)]
        self.cols = [set() for c in range(9)]
        self.boxes = [[set() for bc in range(3)] for br in range(3)]
        self.grid = [[c for c in line.strip()] for line in puzzle_str.strip().split('\n')]
        for r, row in enumerate(self.grid):
            for c, m in enumerate(row):
                self.move(r, c, m)

    def move(self, r, c, m):
        self.rows[r].add(m)
        self.cols[c].add(m)
        self.boxes[int(r/3)][int(c/3)].add(m)
        self.grid[r][c] = m

    def moves(self, r, c):
        return possible_moves - self.rows[r] - self.cols[c] - self.boxes[int(r/3)][int(c/3)]

    def __str__(self):
        return '\n'.join(['.'.join([c for c in line]) for line in self.grid])

worst_best_move = ((10),(),())

def solve_sudoku(puzzle):
    best_move = worst_best_move
    found_move = True
    finished = True

    while found_move:
        finished = True
        found_move = False
        best_move = worst_best_move
        for r in range(0,9):
            for c in range(0,9):
                if puzzle.grid[r][c]=='0':
                    possible_moves = puzzle.moves(r,c)
                    num_moves = len(possible_moves)
                    if num_moves==0:
                        return None
                    if num_moves==1:
                        found_move=True
                        puzzle.move(r, c, possible_moves.pop())
                    else:
                        finished = False
                        if num_moves < best_move[0]:
                            best_move =(num_moves,(r,c), possible_moves)
    if finished:
        return puzzle

    target = best_move[1]
    for move in best_move[2]:
        guess_puzzle = copy.deepcopy(puzzle)
        guess_puzzle.move(target[0], target[1], move)
        result = solve_sudoku(guess_puzzle)
        if result is not None:
            return result
    return None

def print_s(sudoku):
    for s in sudoku:
        print s

def sudokuSolver(sudoku):
    s = ""
    for x in sudoku:
        for y in x:
            s+=`y`
        s+="\n"

    puzzle = Sudoku(s)
    result = solve_sudoku(puzzle)
    x =  str(result)
    d = []
    for i in  x.split("\n"):
        d.append([int(j) for j in i.split(".")])

    return d


## Second Solution

def sudokuSolver(sudoku):
    
    def bt(empty_cell_index):
        if empty_cell_index >= len(empty_cells):
            return True
        
        i, j = empty_cells[empty_cell_index]
        for d in range(1, 10):
            if rows[i][d-1] or cols[j][d-1] or subgrids[i/3][j/3][d-1]:
                continue
            rows[i][d-1] = cols[j][d-1] = subgrids[i/3][j/3][d-1] = True
            sudoku[i][j] = d
            if bt(empty_cell_index + 1):
                return True
            rows[i][d-1] = cols[j][d-1] = subgrids[i/3][j/3][d-1] = False
            
        return False
            
        
    empty_cells = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                empty_cells.append( (i, j) )
                
    rows = []
    for i in range(len(sudoku)):
        cur_row = [False] * 9
        for j in range(len(sudoku[0])):
            if sudoku[i][j] != 0:
                cur_row[ sudoku[i][j] - 1 ] = True
        rows.append( cur_row )
        
    cols = []
    for j in range(len(sudoku[0])):
        cur_col = [False] * 9
        for i in range(len(sudoku)):
            if sudoku[i][j] != 0:
                cur_col[ sudoku[i][j] - 1 ] = True
        cols.append( cur_col )
        
    subgrids = []
    for i in range(0, len(sudoku), 3):
        subgrids.append( [] )
        for j in range(0, len(sudoku[0]), 3):
            cur_subgrid = [False] * 9
            for di in range(3):
                for dj in range(3):
                    cur_val = sudoku[i + di][j + dj]
                    if cur_val == 0:
                        continue
                    cur_subgrid[ cur_val - 1 ] = True
            subgrids[-1].append( cur_subgrid )
            
    bt(0)
    return sudoku        