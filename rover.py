class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def setX(self, x ):
        self.x = x

    def setY(self, y ):
        self.y = y

    def setDirection(self, direction ):
        self.direction = direction

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.direction == other.direction:
            return True
        else:
            return False    



    