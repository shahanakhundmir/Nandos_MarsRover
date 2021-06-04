import pytest
import sys
sys.path.append('./src')
from rover import Rover

def test_checkRover_direction_isValid():
    assert Rover(6,2,'N').is_direction_valid() == True
    assert Rover(6,2,'E').is_direction_valid() == True
    with pytest.raises(ValueError):
        Rover(6,2,'P').is_direction_valid()

def test_rover_coordinates_areNotString():
    rover1  = Rover('6', 2,'N').change_invalid_coordinate()
    assert rover1.get_x() == 6

    rover1  = Rover(6, '2','N').change_invalid_coordinate()
    assert rover1.get_y() == 2
