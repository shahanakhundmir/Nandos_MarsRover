def isPlateauValid(plateau):
    return plateau.x > 0 and plateau.y > 0 

def isRoverOnPlateau(plateau, rover):
    return plateau.x >= rover.x and rover.x >= 0 and plateau.y >= rover.y and rover.y >= 0

def isDirectionValid(rover):
    return rover.direction == 'N' or rover.direction == 'E' or rover.direction == 'S' or rover.direction == 'W'