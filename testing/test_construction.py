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
    germany.construction.start_construction(construction_types.Constructions.CIV, germany.states["oberbayern"], germany)

    #Then it should be part of the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert (germany.construction.get_construction_line_list()[0]).get_state_name().get_name() == "Oberbayern"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name

def test_can_start_building_mil_at_default_start(germany): 
    #Given default Germany start

    #When a mil starts construction in Westfalen
    germany.construction.start_construction(construction_types.Constructions.MIL, germany.states["westfalen"], germany)

    #Then it should be part of the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert (germany.construction.get_construction_line_list()[0]).get_state_name().get_name() == "Westfalen"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.MIL.name

def test_can_start_building_dockyard_in_coastal_state_at_default_start(germany): 
    #Given default Germany start

    holstein_state = germany.states["holstein"]

    #When a dockyard starts construction in Holstein
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then it should be part of the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert (germany.construction.get_construction_line_list()[0]).get_state_name().get_name() == "Holstein"
    assert holstein_state.get_is_coastal() == True
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.DOCKYARD.name

def test_can_not_start_building_dockyard_in_coastal_state_at_default_start(germany): 
    #Given default Germany start

    baden_state = germany.states["baden"]

    #When a dockyard starts construction in Baden
    #Then it should NOT be part of the construction line
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, baden_state, germany)
    assert len(germany.construction.get_construction_line_list()) == 0

def test_cannot_start_building_civ_in_state_with_no_free_building_slots(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When brandenburg state gets 3 building slots removed, such that it has 0 free building slots
    remove_building_slots(brandenburg_state)

    #Then it should not be able to construct anything in brandenburg
    assert brandenburg_state.get_total_construction_slots() == 9
    assert brandenburg_state.get_free_construction_slots(germany) == 0
    
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    assert len(germany.construction.get_construction_line_list()) == 0

def test_can_start_construction_of_two_civs_in_same_state(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When brandenburg state gets two constructed buildings
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should be able to start the construction of both
    assert germany.construction.get_construction_line_size() == 1
    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 2
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name

def test_can_start_construction_of_a_civ_in_two_different_states(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When two states get constructed a civ each
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    #Then it should be able to start the construction of both
    assert germany.construction.get_construction_line_size() == 2
    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"
    assert (get_construction_line(germany, 1)).get_state_name().get_name() == "Baden"

    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 1).get_amount_of_constructions() == 1

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV.name

def test_can_start_construction_of_civ_and_mil_in_same_state(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When brandenburg state gets two constructed buildings
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should be able to start the construction of both
    assert germany.construction.get_construction_line_size() == 2
    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"

    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 1).get_amount_of_constructions() == 1

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.MIL.name
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV.name

def test_different_constructions(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When different states get different buildings constructed
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    print(germany.construction.get_construction_line_size())
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    print(germany.construction.get_construction_line_size())
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    print(germany.construction.get_construction_line_size())
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    print(germany.construction.get_construction_line_size())
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then it should be able to start the construction of them all
    assert germany.construction.get_construction_line_size() == 4

    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"
    assert (get_construction_line(germany, 1)).get_state_name().get_name() == "Brandenburg"
    assert (get_construction_line(germany, 2)).get_state_name().get_name() == "Baden"
    assert (get_construction_line(germany, 3)).get_state_name().get_name() == "Holstein"

    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 1).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 2).get_amount_of_constructions() == 2
    assert get_construction_line(germany, 3).get_amount_of_constructions() == 1

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.MIL.name
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.MIL.name
    assert get_construction_line(germany, 3).get_construction_type() == construction_types.Constructions.DOCKYARD.name

def test_cannot_add_more_buidlings_to_construction_line_when_there_are_no_free_building_slots(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    print(brandenburg_state.get_free_construction_slots(germany))

    #When brandenburg state gets 3 civ constructions
    for i in range(3): 
        germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should be able to start the construction of them all
    assert germany.construction.get_construction_line_size() == 1
    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 3
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name

    print(brandenburg_state.get_free_construction_slots(germany))

    #When another civ starts construction
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should not start the construction of it(because Brandenburg only has 3 free slots in the beginning)
    assert germany.construction.get_construction_line_size() == 1
    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 3
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name

def test_construction_gets_fifteen_factories(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When brandenburg state gets a civ constructed
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should assign 15 factories to it
    assert germany.construction.get_construction_line_size() == 1
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name

    assert get_construction_line(germany, 0).get_assigned_civs() == 15
    assert germany.get_free_civs() == 5

def test_multiple_constructions_assigned_factories(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When three states gets a civ constructed
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, holstein_state, germany)


    #Then it should correctly assign factories to all three depending on the order
    assert germany.construction.get_construction_line_size() == 3
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 1).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 2).get_amount_of_constructions() == 1

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.CIV.name

    assert get_construction_line(germany, 0).get_assigned_civs() == 15
    assert get_construction_line(germany, 1).get_assigned_civs() == 5
    assert get_construction_line(germany, 2).get_assigned_civs() == 0
    assert germany.get_free_civs() == 0

def test_multiple_constructions_in_same_states_assigned_factories(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    rhineland_state = germany.states["rhineland"]


    #When three states gets a civ constructed
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, rhineland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, rhineland_state, germany)

    #Then it should correctly assign factories to all three depending on the order
    assert germany.construction.get_construction_line_size() == 3
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 2
    assert get_construction_line(germany, 1).get_amount_of_constructions() == 2

    assert get_construction_line(germany, 2).get_amount_of_constructions() == 2

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.CIV.name

    assert get_construction_line(germany, 0).get_assigned_civs() == 15
    assert get_construction_line(germany, 1).get_assigned_civs() == 5
    assert get_construction_line(germany, 2).get_assigned_civs() == 0
    assert germany.get_free_civs() == 0

def test_priority_level_correct_when_construction_starts(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    #Then it should correctly find the priority order
    assert germany.construction.get_construction_line_size() == 3

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.MIL.name
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.CIV.name

    assert get_construction_line(germany, 0).get_assigned_civs() == 15
    assert get_construction_line(germany, 1).get_assigned_civs() == 5
    assert get_construction_line(germany, 2).get_assigned_civs() == 0

    assert get_construction_line(germany, 0).get_priority() == 0
    assert get_construction_line(germany, 1).get_priority() == 1
    assert get_construction_line(germany, 2).get_priority() == 2

def test_moving_priority_order(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    print(find_construction_line(construction_types.Constructions.CIV, baden_state, germany).get_priority())


    #And the priority order is moved
    move_priority_level(get_construction_line(germany, 2), 0, germany)

    #Then the order should be the following

    print(get_construction_line(germany, 0))
    print(get_construction_line(germany, 1))
    print(get_construction_line(germany, 2))

    print(find_construction_line(construction_types.Constructions.CIV, baden_state, germany).get_priority())

    assert find_construction_line(construction_types.Constructions.CIV, baden_state, germany).get_priority() == 0
    assert find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany).get_priority() == 1
    assert find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany).get_priority() == 2

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV.name
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.MIL.name

def test_cannot_change_priority_level_to_non_existent_priority_level(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    #Then it should not be possible to change priority level to something that doesn't exist
    move_priority_level(get_construction_line(germany, 1), 3, germany)

    assert find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany).get_priority() == 0
    assert find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany).get_priority() == 1
    assert find_construction_line(construction_types.Constructions.CIV, baden_state, germany).get_priority() == 2







def create_germany(): 
    return setup_countries.create_germany()

def remove_building_slots(state): 
    state.total_construction_slots -= 3

def get_construction_line(country, number): 
    return country.construction.get_construction_line_list()[number]

def find_construction_line(construction_type, state, country): 
    return country.construction.find_construction_line(construction_type, state)

def move_priority_level(construction_type, state, country): 
    return country.construction.move_priority_level(construction_type, state)



