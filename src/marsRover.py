import sys
sys.path.append('./src')

from validateMarsRover import is_rover_on_plateau, collision_has_occured 
from formatMissionData import output_as_string
from rover import Rover

def mars_rover_challenge(plateau, roverMissions ):
    completedMissions = []
    
    for roverMission in roverMissions:
        error = 0
        rover = roverMission[0]
        rover.change_invalid_coordinate()
        movements = roverMission[1]
        if plateau.is_plateau_valid() and is_rover_on_plateau(plateau, rover) and rover.is_direction_valid():
            for move in movements:
                if move == "R" or move == "L":
                    change_rover_direction(rover, move)
                elif move == "M":
                    move_rover_forward(rover)
                    if is_rover_on_plateau(plateau, rover):
                        pass
                    if not collision_has_occured(completedMissions, rover):
                        pass
                else:
                    completedMissions.append("Mission Aborted - Invalid move")
                    error = 1
                    break
        if error == 0:     
            completedMissions.append(rover)
    output_as_string(completedMissions)
    return completedMissions

def change_rover_direction(rover, newDirection):
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

def move_rover_forward(rover):
    if rover.get_direction() == 'N':
        rover.set_y(rover.get_y() + 1)
    elif rover.get_direction() == 'S': 
        rover.set_y(rover.get_y() - 1)
    elif rover.get_direction() == 'E': 
        rover.set_x(rover.get_x() + 1)
    elif rover.get_direction() == 'W': 
        rover.set_x(rover.get_x() -1)
    return rover

