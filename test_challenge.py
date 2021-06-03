from rover import Rover
from plateau import Plateau 
import validateMarsRover
import marsRover
import pytest

def test_rover_direction_changeRight():
    assert marsRover.changeRoverDirection(Rover(6, 2,'N'), 'R').__eq__(Rover(6, 2,'E'))
    assert marsRover.changeRoverDirection(Rover(6, 2,'E'), 'R').__eq__(Rover(6, 2,'S'))

def test_rover_direction_changeLeft():
    assert marsRover.changeRoverDirection( Rover(6, 2,'N'), 'L').__eq__(Rover(6, 2,'W'))
    assert marsRover.changeRoverDirection( Rover(6, 2,'E'), 'L').__eq__(Rover(6, 2,'N'))

def test_rover_moveForward_newPosition():
    assert marsRover.moveRoverForward(Rover(6, 2,'N')).__eq__(Rover(6, 3,'N'))
    assert marsRover.moveRoverForward(Rover(6, 2,'S')).__eq__(Rover(6, 1,'S'))
    assert marsRover.moveRoverForward(Rover(6, 2,'E')).__eq__(Rover(7, 2,'E'))
    assert marsRover.moveRoverForward(Rover(6, 2,'W')).__eq__(Rover(5, 2,'W'))

def test_rover_seriesOfMoves_newPosition():
    plateau = Plateau(5,5)
    assert marsRover.marsRoverChallenge(plateau,[(Rover(4, 3,'W'),"RRMRM"),(Rover(2, 2,'S'),"LMMLM")]) == [Rover(5, 2, 'S'), Rover(4, 3, 'N')]
    assert marsRover.marsRoverChallenge(plateau,[(Rover(1, 2, 'N'),"LMLMLMLMM"),(Rover(3, 3, 'E'),"MMRMMRMRRM")]) == [Rover(1, 3, 'N'),Rover(5, 1, 'E')]

def test_rover_invalidMove_errorMessage():
    plateau = Plateau(5,5)
    assert marsRover.marsRoverChallenge(plateau,[(Rover(4,3,'W'),"RRWRM")]) == ['Mission Aborted - Invalid move']

def test_rover_collision_raiseValueError():
    with pytest.raises(ValueError):
        marsRover.marsRoverChallenge(Plateau(5,5),[(Rover(4,3,'W'),"RRMRM"),(Rover(5,1,'E'),"LMM")]) 
     
def test_rover_notOnPlateau_raiseValueError():
    with pytest.raises(ValueError):
        marsRover.marsRoverChallenge(Plateau(5,5),[(Rover(4, 3,'W'),"RRMRM"),(Rover(4, 4, 'E'),"MMLM")])

def test_checkRover_position_isWithinPlateau_raiseValueError():
    plateau = Plateau(5,5)
    with pytest.raises(ValueError):
        assert validateMarsRover.isRoverOnPlateau(plateau, Rover(6, 2,'N'))
    assert validateMarsRover.isRoverOnPlateau(plateau, Rover(1 ,2,'N')) == True
