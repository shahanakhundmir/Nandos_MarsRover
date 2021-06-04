import pytest
import sys
sys.path.append('./src')
from plateau import Plateau

def test_checkPlateau_size_isnotNull():

    with pytest.raises(ValueError):
        Plateau(0,0).is_plateau_valid()
    assert Plateau(1,5).is_plateau_valid() == True


    