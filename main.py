from graphics import Window #, Line, Point
#from cell import Cell
from maze import Maze

def main():
    res_x = 800
    res_y = 600
    border = 20
    num_rows = 6
    num_cols = 8
    cell_size_x = int((res_x - (border * 2)) / num_cols)
    cell_size_y = int((res_y - (border * 2)) / num_rows)

    win = Window(res_x, res_y)
    maze = Maze(border, border, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()