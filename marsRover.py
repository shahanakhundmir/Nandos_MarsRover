from validateMarsRover import isRoverOnPlateau, collisionHasOccured 
from formatMissionData import outputAsString
from rover import Rover

def marsRoverChallenge(plateau, roverMissions ):
    completedMissions = []
    
    for roverMission in roverMissions:
        error = 0
        rover = roverMission[0]
        rover.changeInvalidCoordinate()
        movements = roverMission[1]
        if plateau.isPlateauValid() and isRoverOnPlateau(plateau, rover) and rover.isDirectionValid():
            for move in movements:
                if move == "R" or move == "L":
                    changeRoverDirection(rover, move)
                elif move == "M":
                    moveRoverForward(rover)
                    if isRoverOnPlateau(plateau, rover):
                        pass
                    if not collisionHasOccured(completedMissions, rover):
                        pass
                else:
                    completedMissions.append("Mission Aborted - Invalid move")
                    error = 1
                    break
        # only capture the rovers mission if it has been successful
        if error == 0:     
            completedMissions.append(rover)
    outputAsString(completedMissions)
    return completedMissions

def changeRoverDirection(rover, newDirection):
    if newDirection == 'R':
        if rover.get_direction() == 'N': 
            rover.set_direction('E')
        elif rover.get_direction() == 'E': 
            rover.set_direction('S')
        elif rover.get_direction() == 'S': 
            rover.set_direction('W')
        elif rover.get_direction() == 'W': 
            rover.set_direction('N')

    elif newDirection == 'L':
        if rover.get_direction() == 'N': 
            rover.set_direction('W')
        elif rover.get_direction() == 'E': 
            rover.set_direction('N')
        elif rover.get_direction() == 'S': 
            rover.set_direction('E')
        elif rover.get_direction() == 'W': 
            rover.set_direction('S')
    return rover

def moveRoverForward(rover):
    if rover.get_direction() == 'N':
        rover.set_y(rover.get_y() + 1)
    elif rover.get_direction() == 'S': 
        rover.set_y(rover.get_y() - 1)
    elif rover.get_direction() == 'E': 
        rover.set_x(rover.get_x() + 1)
    elif rover.get_direction() == 'W': 
        rover.set_x(rover.get_x() -1)
    return rover

