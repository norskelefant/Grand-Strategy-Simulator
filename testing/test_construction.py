import hoi_simulator as hoi

import pytest

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line

@pytest.fixture
def germany(): 
    #Creates a new Germany instance before each test
    return create_germany()

def test_can_start_building_civ_at_default_start(germany): 
    #Given default Germany start

    #When a civ starts construction in Oberbayern
    construction_line_1 = germany.construction.start_construction(construction_types.Constructions.CIV, germany.states["oberbayern"], germany)

    #Then it should be part of the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert (germany.construction.get_construction_line_list()[0]).get_state_name().get_name() == "Oberbayern"
    assert construction_line_1.get_amount_of_constructions() == 1
    assert construction_line_1.get_construction_type() == construction_types.Constructions.CIV.name

def test_can_start_building_mil_at_default_start(germany): 
    #Given default Germany start

    #When a mil starts construction in Westfalen
    construction_line_1 = germany.construction.start_construction(construction_types.Constructions.MIL, germany.states["westfalen"], germany)

    #Then it should be part of the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert (germany.construction.get_construction_line_list()[0]).get_state_name().get_name() == "Westfalen"
    assert construction_line_1.get_amount_of_constructions() == 1
    assert construction_line_1.get_construction_type() == construction_types.Constructions.MIL.name

def test_can_start_building_dockyard_in_coastal_state_at_default_start(germany): 
    #Given default Germany start

    holstein_state = germany.states["holstein"]

    #When a dockyard starts construction in Holstein
    construction_line_1 = germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then it should be part of the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert (germany.construction.get_construction_line_list()[0]).get_state_name().get_name() == "Holstein"
    assert holstein_state.get_is_coastal() == True
    assert construction_line_1.get_amount_of_constructions() == 1
    assert construction_line_1.get_construction_type() == construction_types.Constructions.DOCKYARD.name

def test_can_not_start_building_dockyard_in_coastal_state_at_default_start(germany): 
    #Given default Germany start

    baden_state = germany.states["baden"]

    #When a dockyard starts construction in Baden
    #Then it should NOT be part of the construction line
    construction_line_1 = germany.construction.start_construction(construction_types.Constructions.DOCKYARD, baden_state, germany)
    assert construction_line_1 is None
    assert len(germany.construction.get_construction_line_list()) == 0

def test_cannot_start_building_civ_in_state_with_no_free_building_slots(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When brandenburg state gets 3 building slots removed, such that it has 0 free building slots
    remove_building_slots(brandenburg_state)

    #Then it should not be able to construct anything in brandenburg
    assert brandenburg_state.get_total_construction_slots() == 9
    assert brandenburg_state.get_free_construction_slots() == 0
    construction_line_1 = germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    assert construction_line_1 is None
    assert len(germany.construction.get_construction_line_list()) == 0

def create_germany(): 
    return setup_countries.create_germany()

def remove_building_slots(state): 
    state.total_construction_slots -= 3









