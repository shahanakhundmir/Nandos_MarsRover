from src.rover import Rover
import pytest

def test_checkRover_direction_isValid():
    assert Rover(6,2,'N').is_direction_valid() == True
    assert Rover(6,2,'E').is_direction_valid() == True
    with pytest.raises(ValueError):
        Rover(6,2,'P').is_direction_valid()

def test_rover_coordinates_areNotString():
    assert Rover('6', 2,'N').change_invalid_coordinate().__eq__(Rover(6, 2,'N'))
    assert Rover(6 ,'2','N').change_invalid_coordinate().__eq__(Rover(6, 2,'N'))

