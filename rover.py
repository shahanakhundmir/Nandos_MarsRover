class Rover:
    def __init__(self, x, y, direction):
        self._x = x
        self._y = y
        self._direction = direction

    def set_x(self, x ):
        self._x = x

    def set_y(self, y ):
        self._y = y

    def set_direction(self, direction ):
        self._direction = direction

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_direction(self):
        return self._direction

    def __eq__(self, other):
        if self._x == other.get_x() and self._y == other.get_y() and self._direction == other.get_direction():
            return True
        else:
            return False    


