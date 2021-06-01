from rover import Rover
from plateau import Plateau 
import validateMarsRover

def test_checkPlateau_size_isnotNull():
    plateau = Plateau(0,0)
    assert validateMarsRover.isPlateauValid(plateau) == False
    plateau = Plateau(1,5)
    assert validateMarsRover.isPlateauValid(plateau) == True


'''
    def test_binary_init_bitstr():
    binary = Binary('110')
    assert int(binary) == 6
    assert validateMarsRover.isPlateauValid((0,0)) == False
    assert validateMarsRover.isPlateauValid((5,5)) == True
    '''