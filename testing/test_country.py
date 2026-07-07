import hoi_simulator as hoi

from hoi_simulator import country, state, setup_countries



def test_germany(): 
    #Given Germany
    germany = setup_countries.create_germany()

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
    germany = setup_countries.create_germany()

    #When brandenburg is selected
    brandenburg = germany.states["brandenburg"]

    #Then the following should hold for brandenburg
    assert brandenburg.get_name() == "Brandenburg"
    assert brandenburg.get_total_construction_slots() == 12
    assert brandenburg.get_civs() == 4
    assert brandenburg.get_mils() == 5
    assert brandenburg.get_dockyards() == 0
    assert brandenburg.get_infrastructure_level() == 4
    assert brandenburg.get_is_coastal() == False
    assert brandenburg.get_free_construction_slots() == 3




