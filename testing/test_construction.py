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







def create_germany(): 
    return setup_countries.create_germany()











