
def isRoverOnPlateau(plateau, rover):
    if plateau.get_x() >= rover.get_x() and rover.get_x() >= 0 and plateau.get_y() >= rover.get_y() and rover.get_y() >= 0:
        return True 
    else:
        raise ValueError('Mission aborted - Rover is not on the Plateau')

def collisionHasOccured(completedMissions, rover):
    for completedMission in completedMissions:
        if type(completedMission) != str:
            if completedMission.get_x() == rover.get_x() and completedMission.get_y() == rover.get_y():
                raise ValueError('Mission aborted - Collision has occured')
            else:
                return False