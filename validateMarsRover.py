
def isRoverOnPlateau(plateau, rover):
    return plateau.get_x() >= rover.get_x() and rover.get_x() >= 0 and plateau.get_y() >= rover.get_y() and rover.get_y() >= 0

def collisionHasOccured(completedMissions, rover):
    for completedMission in completedMissions:
        if completedMission.get_x() == rover.get_x() and completedMission.get_y() == rover.get_y():
            return True