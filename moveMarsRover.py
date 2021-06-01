def changeRoverDirection(rover, newDirection):
    if newDirection == 'R':
        if rover.direction == 'N': 
            rover.setDirection('E')
        elif rover.direction == 'E': 
            rover.setDirection('S')
        elif rover.direction == 'S': 
            rover.setDirection('W')
        elif rover.direction == 'W': 
            rover.setDirection('N')

    elif newDirection == 'L':
        if rover.direction == 'N': 
            rover.setDirection('W')
        elif rover.direction == 'E': 
            rover.setDirection('N')
        elif rover.direction == 'S': 
            rover.setDirection('E')
        elif rover.direction == 'W': 
            rover.setDirection('S')
    return rover

def moveRoverForward(rover):
    if rover.direction == 'N':
        rover.setY(rover.y + 1)
    elif rover.direction == 'S': 
        rover.setY(rover.y - 1)
    elif rover.direction == 'E': 
        rover.setX(rover.x + 1)
    elif rover.direction == 'W': 
        rover.setX(rover.x -1)
    return rover