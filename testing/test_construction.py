import hoi_simulator as hoi

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line


def test_can_start_building_civ_at_default_start(): 
    #Given default Germany start
    germany = setup_countries.create_germany()

    #When a civ starts construction in oberbayern
    construction_line_1 = construction.start_construction(construction_types.Constructions.CIV, germany.states["oberbayern"], germany)

    #Then it should be part of the construction line
    assert construction.get_construction_line_size() == 1
    assert (construction.get_construction_line_list()[0]).get_state_name().get_name() == "Oberbayern"
    assert construction_line_1.get_amount_of_constructions() == 1














