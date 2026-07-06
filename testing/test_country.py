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

    assert len(germany.states) == 24
    #assert germany.tiles = ...
    #assert germany.resources = ...

def test_brandenburg(): 
    #Given Germany
    germany = create_germany()

    #When brandenburg is selected
    brandenburg = germany.states["brandenburg"]

    #Then the following should hold for brandenburg
    assert brandenburg.name == "Brandenburg"
    assert brandenburg.construction_slots == 12
    assert brandenburg.civs == 4
    assert brandenburg.mils == 5
    assert brandenburg.infrastructure_level == 4


#def test_state


