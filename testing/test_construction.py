import hoi_simulator as hoi

import pytest

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game

@pytest.fixture
def germany(): 
    #Creates a new Germany instance before each test
    return create_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

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
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
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

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    #And the priority order is moved
    move_priority_level(construction_line_baden_civ, 0, germany)

    #Then the order should be the following
    assert construction_line_baden_civ.get_priority() == 0
    assert construction_line_brandenburg_civ.get_priority() == 1
    assert construction_line_brandenburg_mil.get_priority() == 2

    assert construction_line_baden_civ.get_construction_type() == construction_types.Constructions.CIV.name
    assert construction_line_brandenburg_civ.get_construction_type() == construction_types.Constructions.CIV.name
    assert construction_line_brandenburg_mil.get_construction_type() == construction_types.Constructions.MIL.name

def test_cannot_change_priority_level_to_non_existent_priority_level(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    #Then it should not be possible to change priority level to something that doesn't exist
    move_priority_level(construction_line_brandenburg_civ, 3, germany)

    assert construction_line_brandenburg_civ.get_priority() == 0
    assert construction_line_brandenburg_mil.get_priority() == 1
    assert construction_line_baden_civ.get_priority() == 2

def test_moving_priority_levels_multiple_times(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    #Then it should not be possible to change priority level to something that doesn't exist
    move_priority_level(find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany), 2, germany)

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_mil.get_priority() == 0
    assert construction_line_baden_civ.get_priority() == 1

    move_priority_level(construction_line_brandenburg_mil, 1, germany)

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_mil.get_priority() == 1
    assert construction_line_baden_civ.get_priority() == 0

    move_priority_level(construction_line_brandenburg_civ, 0, germany)

    assert construction_line_brandenburg_civ.get_priority() == 0
    assert construction_line_brandenburg_mil.get_priority() == 2
    assert construction_line_baden_civ.get_priority() == 1

def test_can_move_construction_lines_with_multiple_factories(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    assert germany.construction.get_construction_line_size() == 3

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 2
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 1
    assert construction_line_baden_civ.get_amount_of_constructions() == 3

    #Then the priority order should be correct after each moving of priority level
    move_priority_level(find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany), 2, germany)

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_mil.get_priority() == 0
    assert construction_line_baden_civ.get_priority() == 1

    move_priority_level(find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany), 1, germany)

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_mil.get_priority() == 1
    assert construction_line_baden_civ.get_priority() == 0

    move_priority_level(find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany), 0, germany)

    assert construction_line_brandenburg_civ.get_priority() == 0
    assert construction_line_brandenburg_mil.get_priority() == 2
    assert construction_line_baden_civ.get_priority() == 1

def test_can_switch_production_lines_and_factories_will_be_reassigned_based_on_priority_order(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_mil.get_assigned_civs() == 5
    assert construction_line_baden_civ.get_assigned_civs() == 0

    #Then when the order is switched, then the number of assigned factories should be switched
    move_priority_level(find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany), 2, germany)

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_mil.get_priority() == 0
    assert construction_line_baden_civ.get_priority() == 1

    assert construction_line_brandenburg_civ.get_assigned_civs() == 0
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_baden_civ.get_assigned_civs() == 5

    move_priority_level(construction_line_baden_civ, 0, germany)

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_mil.get_priority() == 1
    assert construction_line_baden_civ.get_priority() == 0

    assert construction_line_brandenburg_civ.get_assigned_civs() == 0
    assert construction_line_brandenburg_mil.get_assigned_civs() == 5
    assert construction_line_baden_civ.get_assigned_civs() == 15

    for construction_line in germany.construction.get_construction_line_list(): 
        print(construction_line)

def test_remove_civ_from_construction_line(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states and a factory is removed from one of them
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert germany.construction.get_construction_line_size() == 1
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 2

    remove_building_from_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should remove it from the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1

def test_delete_construction_line(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states and the construction line is removed
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert germany.construction.get_construction_line_size() == 1
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 2

    remove_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then there should be no more construction lines
    assert germany.construction.get_construction_line_size() == 0

def test_delete_construction_line_priority_levels_and_assigned_factories(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    assert germany.construction.get_construction_line_size() == 3

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 2
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 1
    assert construction_line_baden_civ.get_amount_of_constructions() == 3

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_mil.get_assigned_civs() == 5
    assert construction_line_baden_civ.get_assigned_civs() == 0

    assert germany.construction.get_construction_line_size() == 3

    #Then when a construction line is removed, it should change priority levels and assigned factories
    remove_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert germany.construction.get_construction_line_size() == 2

    assert construction_line_brandenburg_mil.get_priority() == 0
    assert construction_line_baden_civ.get_priority() == 1

    print(construction_line_brandenburg_civ.get_assigned_civs())

    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_baden_civ.get_assigned_civs() == 5

    remove_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)

    assert germany.construction.get_construction_line_size() == 1

    assert construction_line_baden_civ.get_priority() == 0
    
    assert construction_line_baden_civ.get_assigned_civs() == 15

    assert germany.get_free_civs() == 5

def test_free_civs(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    #Then the amount of free civs should be correct
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    assert germany.get_free_civs() == 0

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_baden_civ.get_assigned_civs() == 5

    remove_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert construction_line_baden_civ.get_assigned_civs() == 15

    assert germany.get_free_civs() == 5

    remove_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    assert germany.get_free_civs() == 20

def test_construction_cost_left_on_civ_and_mil_default_start(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then the construction cost should be the default costs
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 7200


def test_construction_cost_left_on_civ_and_mil_after_a_day_with_default_construction_speed(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then then the construction cost should be the default costs
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 7200

    #When a day passes
    new_game.pass_day()

    #Then the construction costs should be the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 10740
    assert construction_line_baden_mil.get_construction_cost() == 7180

    real_date = new_game.get_date()
    correct_date = date.Date(2, 1, 1936)
    same_dates = check_date(real_date, correct_date)

    assert same_dates == True



def test_construction_cost_left_on_civ_and_mil_after_a_month_with_default_construction_speed(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then then the construction cost should be the default costs
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 7200

    #When days pass until next month begins
    new_game.pass_month()

    #Then the construction costs should be the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 8940
    assert construction_line_baden_mil.get_construction_cost() == 6580

def test_construction_cost_left_on_civ_and_mil_after_52_with_default_construction_speed(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then then the construction cost should be the default costs
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 7200

    #When 52 days pass
    for i in range(52): 
        new_game.pass_day()

    #Then the construction costs should be the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 7680
    assert construction_line_baden_mil.get_construction_cost() == 6160

def test_construction_cost_left_on_civ_should_be_0_after_180_days(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then then the construction cost should be the default costs
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 7200

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the construction costs should be the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 0
    assert construction_line_baden_mil.get_construction_cost() == 3600

def test_construction_cost_doesnt_change_if_no_factories_are_assigned(germany, new_game): 
        #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)


    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)


    #Then then the construction cost should be the default costs
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 7200
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the construction costs should be the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 0
    assert construction_line_baden_mil.get_construction_cost() == 3600
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400

def test_civ_count_updates_if_civ_finishes_building(germany, new_game): 
    return None














def test_amount_of_time_left_on_civ_construction_with_default_construction_speed(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then the amount of time left should be correct

    return None
    #assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    #assert construction_line_baden_mil.get_assigned_civs() == 5







def create_germany(): 
    return setup_countries.create_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def remove_building_slots(state): 
    state.total_construction_slots -= 3

def get_construction_line(country, number): 
    return country.construction.get_construction_line_list()[number]

def find_construction_line(construction_type, state, country): 
    return country.construction.find_construction_line(construction_type, state)

def move_priority_level(construction_type, state, country): 
    country.construction.move_priority_level(construction_type, state, country)

def remove_building_from_construction_line(construction_type, state, country): 
    country.construction.remove_building_from_construction_line(find_construction_line(construction_type, state, country))

def remove_construction_line(construction_type, state, country): 
    country.construction.delete_construction_line(find_construction_line(construction_type, state, country), country)

def get_construction_line_list(country): 
    return country.construction.get_construction_line_list()

def check_date(date_one, date_two): 
    return date_one.get_day() == date_two.get_day() and date_one.get_month() == date_two.get_month() and date_one.get_year() == date_two.get_year()