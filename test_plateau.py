from plateau import Plateau 
import pytest

def test_checkPlateau_size_isnotNull():

    with pytest.raises(ValueError):
        Plateau(0,0).isPlateauValid()
    assert Plateau(1,5).isPlateauValid() == True


    