from src.plateau import Plateau 
import pytest

def test_checkPlateau_size_isnotNull():

    with pytest.raises(ValueError):
        Plateau(0,0).is_plateau_valid()
    assert Plateau(1,5).is_plateau_valid() == True


    