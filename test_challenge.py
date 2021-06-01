from rover import Rover
from plateau import Plateau 
import validateMarsRover
import moveMarsRover
import marsRover

def test_checkPlateau_size_isnotNull():
    plateau = Plateau(0,0)
    assert validateMarsRover.isPlateauValid(plateau) == False
    plateau = Plateau(1,5)
    assert validateMarsRover.isPlateauValid(plateau) == True

def test_checkRover_position_isWithinPlateau():
    plateau = Plateau(5,5)
    rover1 = Rover(6, 2,'N')
    rover2 = Rover(1 ,2,'N')
    assert validateMarsRover.isRoverOnPlateau(plateau, rover1) == False
    assert validateMarsRover.isRoverOnPlateau(plateau, rover2) == True

def test_checkRover_direction_isValid():
    rover1 = Rover(6, 2,'N')
    rover2 = Rover(6 ,2,'E')
    rover3 = Rover(6 ,2,'P')
    assert validateMarsRover.isDirectionValid(rover1) == True
    assert validateMarsRover.isDirectionValid(rover2) == True
    assert validateMarsRover.isDirectionValid(rover3) == False

def test_rover_coordinates_areNotString():
    assert validateMarsRover.changeInvalidCoordinate(Rover('6', 2,'N')).__eq__(Rover(6, 2,'N'))
    assert validateMarsRover.changeInvalidCoordinate(Rover(6 ,'2','N')).__eq__(Rover(6, 2,'N'))

def test_rover_direction_changeRight():
    assert moveMarsRover.changeRoverDirection(Rover(6, 2,'N'), 'R').__eq__(Rover(6, 2,'E'))
    assert moveMarsRover.changeRoverDirection(Rover(6, 2,'E'), 'R').__eq__(Rover(6, 2,'S'))

def test_rover_direction_changeLeft():
    assert moveMarsRover.changeRoverDirection( Rover(6, 2,'N'), 'L').__eq__(Rover(6, 2,'W'))
    assert moveMarsRover.changeRoverDirection( Rover(6, 2,'E'), 'L').__eq__(Rover(6, 2,'N'))

def test_rover_moveForward_newPosition():
    assert moveMarsRover.moveRoverForward(Rover(6, 2,'N')).__eq__(Rover(6, 3,'N'))
    assert moveMarsRover.moveRoverForward(Rover(6, 2,'S')).__eq__(Rover(6, 1,'S'))
    assert moveMarsRover.moveRoverForward(Rover(6, 2,'E')).__eq__(Rover(7, 2,'E'))
    assert moveMarsRover.moveRoverForward(Rover(6, 2,'W')).__eq__(Rover(5, 2,'W'))

def test_rover_seriesOfMoves_newPosition():
    plateau = Plateau(5,5)
    assert marsRover.marsRoverChallenge(plateau,[(Rover(4, 3,'W'),"RRMRM"),(Rover(2, 2,'S'),"LMMLM")]) == [Rover(5, 2, 'S'), Rover(4, 3, 'N')]
    assert marsRover.marsRoverChallenge(plateau,[(Rover(1, 2, 'N'),"LMLMLMLMM"),(Rover(3, 3, 'E'),"MMRMMRMRRM")]) == [Rover(1, 3, 'N'),Rover(5, 1, 'E')]