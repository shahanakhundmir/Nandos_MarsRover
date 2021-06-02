def isPlateauValid(plateau):
    return plateau.get_x() > 0 and plateau.get_y() > 0 

def isRoverOnPlateau(plateau, rover):
    return plateau.get_x() >= rover.get_x() and rover.get_x() >= 0 and plateau.get_y() >= rover.get_y() and rover.get_y() >= 0

def isDirectionValid(rover):
    return rover.get_direction() == 'N' or rover.get_direction() == 'E' or rover.get_direction() == 'S' or rover.get_direction() == 'W'

def changeInvalidCoordinate(rover):
    if type(rover.get_x()) == str:
        rover.set_x(int(rover.get_x()))
    if type(rover.get_y()) == str:
        rover.set_y(int(rover.get_y()))
    return rover

def collisionHasOccured(completedMissions, rover):
    for completedMission in completedMissions:
        if completedMission.get_x() == rover.get_x() and completedMission.get_y() == rover.get_y():
            return True