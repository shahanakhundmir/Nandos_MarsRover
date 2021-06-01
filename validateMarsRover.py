def isPlateauValid(plateau):
    return plateau.x > 0 and plateau.y > 0 

def isRoverOnPlateau(plateau, rover):
    return plateau.x >= rover.x and rover.x >= 0 and plateau.y >= rover.y and rover.y >= 0

def isDirectionValid(rover):
    return rover.direction == 'N' or rover.direction == 'E' or rover.direction == 'S' or rover.direction == 'W'

def changeInvalidCoordinate(rover):
    if type(rover.x) == str:
        rover.setX(int(rover.x))
    if type(rover.y) == str:
        rover.setY(int(rover.y))
    return rover

def collisionHasOccured(completedMissions, rover):
    for completedMission in completedMissions:
        if completedMission.x == rover.x and completedMission.y == rover.y:
            return True