from rover import Rover
from plateau import Plateau 
import validateMarsRover

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

