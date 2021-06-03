from validateMarsRover import *#collisionHasOccured, isPlateauValid, isRoverOnPlateau, isDirectionValid, checkCoordinatedAreValid
from moveMarsRover import moveRoverForward, changeRoverDirection
from formatMissionData import outputAsString


def marsRoverChallenge(plateau, roverMissions ):
    completedMissions = []
    error = 0
    for roverMission in roverMissions:
        rover = roverMission[0]
        rover.changeInvalidCoordinate()
        movements = roverMission[1]
        if plateau.isPlateauValid() and isRoverOnPlateau(plateau, rover) and rover.isDirectionValid():
            for move in movements:
                if move == "R" or move == "L":
                    changeRoverDirection(rover, move)
                elif move == "M":
                    moveRoverForward(rover)
                    if not isRoverOnPlateau(plateau, rover):
                        completedMissions.append("Mission Aborted - Rover is no longer on the plateau")
                        error = 1
                        break
                    if collisionHasOccured(completedMissions, rover):
                        completedMissions.append("Mission Aborted - Collision has occured")
                        error = 1
                        break
                else:
                    completedMissions.append("Mission Aborted - Invalid move")
                    error = 1
                    break
        # only capture the rovers mission if it has been successful
        if error == 0:     
            completedMissions.append(rover)
        outputAsString(completedMissions)
    return completedMissions