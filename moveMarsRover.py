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