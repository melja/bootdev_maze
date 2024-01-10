from graphics import Window, Line, Point

class Cell():
    def __init__(self, win=None): 
        self.has_left_wall = True 
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_bottom_wall = True 
        self._x1 = None 
        self._x2 = None 
        self._y1 = None 
        self._y2 = None 
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left = Point(self._x1, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        top_right = Point(self._x2, self._y1)

        if self._win:
            if self.has_left_wall:
                self._win.draw_line(Line(top_left, bottom_left))
            else:
                self._win.draw_line(Line(top_left, bottom_left), fill_color="white")
                
            if self.has_bottom_wall:
                self._win.draw_line(Line(bottom_left, bottom_right))
            else:
                self._win.draw_line(Line(bottom_left, bottom_right), fill_color="white")
                
            if self.has_right_wall:
                self._win.draw_line(Line(bottom_right, top_right))
            else:
                self._win.draw_line(Line(bottom_right, top_right), fill_color="white")
                
            if self.has_top_wall:
                self._win.draw_line(Line(top_left, top_right))
            else:
                self._win.draw_line(Line(top_left, top_right), fill_color="white")
                                
    def draw_move(self, to_cell, undo=False):
        center = self._center()
        start = center
        end = to_cell._center()
        color = "red" if undo else "gray"
        if self._win:
            self._win.draw_line(Line(start, end), color)

    def _center(self):
        return Point(self._x1 + ((self._x2-self._x1)/2),self._y1 + ((self._y2-self._y1)/2))
