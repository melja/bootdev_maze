import time 
from graphics import Window #, Line, Point
from maze import Maze

def main():
    res_x = 800
    res_y = 600
    border = 20
    num_rows = 16
    num_cols = 20
    cell_size_x = int((res_x - (border * 2)) / num_cols)
    cell_size_y = int((res_y - (border * 2)) / num_rows)

    win = Window(res_x, res_y)
    maze = Maze(border, border, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=time.monotonic_ns())

    win.wait_for_close()

if __name__ == "__main__":
    main()