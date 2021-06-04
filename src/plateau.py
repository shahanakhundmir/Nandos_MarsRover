class Plateau:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def is_plateau_valid(self):
        if self._x <= 0 and self._y <= 0:
            raise ValueError('Invalid Plateau coordinates')
        else:
            return True