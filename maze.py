from time import sleep
from cell import Cell
from random import Random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._random = Random()
        if seed is not None:
            self._random.seed(seed)
        else:
            self._random.seed(0)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()
        self.solve()
        self._reset_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)

        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        if self._win:
            self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # check if left visited already
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))
            # check if right visited already
            if i < self._num_cols-1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            # check if above visited already
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            # check if below visited already
            if j < self._num_rows-1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))
            if not to_visit:
                self._draw_cell(i, j)
                break
            next_i, next_j = to_visit[self._random.randrange(len(to_visit))]
            if next_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            if next_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            if next_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            if next_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            self._draw_cell(i, j)
            self._break_walls_r(next_i, next_j)

    def _reset_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        else:
            to_visit = []
            # try down
            if j < self._num_rows-1 and not current.has_bottom_wall and not self._cells[i][j+1].visited: 
                to_visit.append((i, j+1))
            # try right
            if i < self._num_cols-1 and not current.has_right_wall and not self._cells[i+1][j].visited: 
                to_visit.append((i+1, j))
            # try up
            if j > 0 and not current.has_top_wall and not self._cells[i][j-1].visited: 
                to_visit.append((i, j-1))
            # try left
            if i > 0 and not current.has_left_wall and not self._cells[i-1][j].visited: 
                to_visit.append((i-1, j))
            while to_visit:
                next_i, next_j = to_visit.pop(0)
                path = self._solve_r(next_i, next_j)
                current.draw_move(self._cells[next_i][next_j], not path)
                if path:
                    return True
    
            return False
