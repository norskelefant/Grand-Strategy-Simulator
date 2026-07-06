from hoi_simulator.setup_countries import *
from hoi_simulator.country import *

def test_germany(): 
    #Given Germany
    germany = create_germany()

    #When the game starts

    #Then the following should hold for Germany
    assert germany.name == "Germany"

    assert germany.total_civs == 35
    assert germany.free_civs == 20
    assert germany.total_mils == 28
    assert germany.free_mils == 28

    assert germany.states.count == 23
    #assert germany.tiles = ...
    #assert germany.resources = ...



#def test_state


