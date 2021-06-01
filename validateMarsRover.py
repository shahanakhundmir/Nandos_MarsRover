def isPlateauValid(plateau):
    return plateau.x > 0 and plateau.y > 0 

def isRoverOnPlateau(plateau, rover):
    return plateau.x >= rover.x and rover.x >= 0 and plateau.y >= rover.y and rover.y >= 0

