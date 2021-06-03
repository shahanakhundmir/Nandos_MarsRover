from rover import Rover

def test_checkRover_direction_isValid():
    assert Rover(6,2,'N').isDirectionValid() == True
    assert Rover(6,2,'E').isDirectionValid() == True
    assert Rover(6,2,'P').isDirectionValid() == False

def test_rover_coordinates_areNotString():
    assert Rover('6', 2,'N').changeInvalidCoordinate().__eq__(Rover(6, 2,'N'))
    assert Rover(6 ,'2','N').changeInvalidCoordinate().__eq__(Rover(6, 2,'N'))
