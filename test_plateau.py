from plateau import Plateau 

def test_checkPlateau_size_isnotNull():
    assert Plateau(0,0).isPlateauValid() == False
    assert Plateau(1,5).isPlateauValid() == True