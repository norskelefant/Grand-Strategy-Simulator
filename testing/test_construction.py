import hoi_simulator as hoi

import pytest

import math

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
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV

def test_can_start_building_mil_at_default_start(germany): 
    #Given default Germany start

    #When a mil starts construction in Westfalen
    germany.construction.start_construction(construction_types.Constructions.MIL, germany.states["westfalen"], germany)

    #Then it should be part of the construction line
    assert germany.construction.get_construction_line_size() == 1
    assert (germany.construction.get_construction_line_list()[0]).get_state_name().get_name() == "Westfalen"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.MIL

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
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.DOCKYARD

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
    assert brandenburg_state.get_free_construction_slots() == 0
    
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
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV

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

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV

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

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.MIL
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV

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

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.MIL
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.MIL
    assert get_construction_line(germany, 3).get_construction_type() == construction_types.Constructions.DOCKYARD

def test_cannot_add_more_buidlings_to_construction_line_when_there_are_no_free_building_slots(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When brandenburg state gets 3 civ constructions
    for i in range(3): 
        germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should be able to start the construction of them all
    assert germany.construction.get_construction_line_size() == 1
    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 3
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV

    #When another civ starts construction
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should not start the construction of it(because Brandenburg only has 3 free slots in the beginning)
    assert germany.construction.get_construction_line_size() == 1
    assert (get_construction_line(germany, 0)).get_state_name().get_name() == "Brandenburg"
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 3
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV

def test_construction_gets_fifteen_factories(germany): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When brandenburg state gets a civ constructed
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then it should assign 15 factories to it
    assert germany.construction.get_construction_line_size() == 1
    assert get_construction_line(germany, 0).get_amount_of_constructions() == 1
    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV

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

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.CIV

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

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.CIV
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.CIV

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

    assert get_construction_line(germany, 0).get_construction_type() == construction_types.Constructions.CIV
    assert get_construction_line(germany, 1).get_construction_type() == construction_types.Constructions.MIL
    assert get_construction_line(germany, 2).get_construction_type() == construction_types.Constructions.CIV

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

    assert construction_line_baden_civ.get_construction_type() == construction_types.Constructions.CIV
    assert construction_line_brandenburg_civ.get_construction_type() == construction_types.Constructions.CIV
    assert construction_line_brandenburg_mil.get_construction_type() == construction_types.Constructions.MIL

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

    #for construction_line in germany.construction.get_construction_line_list(): 
    #    print(construction_line)

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

    #When 179 days pass
    for i in range(179): 
        new_game.pass_day()

    #Then the construction costs should be the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 60
    assert construction_line_baden_mil.get_construction_cost() == 3620
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400

def test_civ_count_updates_if_civ_finishes_building(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
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
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 3600

    #and the amount of civs in the construction line should be 1
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert construction_line_baden_mil.get_amount_of_constructions() == 2

def test_civ_count_updates_if_mil_finishes_building(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
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
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 3600

    #When the priority level between the two switches
    move_priority_level(construction_line_baden_mil, 0, germany)

    assert construction_line_brandenburg_civ.get_priority() == 1
    assert construction_line_baden_mil.get_priority() == 0

    #When 60 days pass
    for i in range(60): 
        new_game.pass_day()

    #and the amount of mils in the construction line should be 1
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert construction_line_baden_mil.get_amount_of_constructions() == 1

    assert construction_line_brandenburg_civ.get_assigned_civs() == 6
    assert construction_line_baden_mil.get_assigned_civs() == 15
    
    assert construction_line_brandenburg_civ.get_construction_cost() == 9360
    assert construction_line_baden_mil.get_construction_cost() == 7200

def test_construction_cost_gets_reset(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the construction cost should be reset to 10800
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 3600

def test_construction_line_gets_removed_if_civ_finishes_and_there_is_only_one_civ_in_construction_line(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    assert new_game.get_date().get_day() == 30
    assert new_game.get_date().get_month() == 6
    assert new_game.get_date().get_year() == 1936

    #Then the first civ should finish and the construction line should be removed
    assert construction_line_baden_mil.get_construction_cost() == 3600
    assert germany.get_construction().get_construction_line_size() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert germany.get_free_civs() == 6

def test_construction_line_gets_removed_if_two_civs_finish(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 360 days pass
    for i in range(360): 
        new_game.pass_day()

    #These variables include how much construction was done in the first half with 5 free civs and in the second half with 6 free civs
    first_half_construction_of_civ = (5 * 4) * 180
    second_half_construction_of_mil = (6 * 4) * 180

    #Then the civs should be finished and the construction line should be removed
    assert construction_line_baden_mil.get_construction_cost() == 6480
    assert construction_line_baden_mil.get_amount_of_constructions() == 1
    assert germany.get_construction().get_construction_line_size() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert germany.get_free_civs() == 7
    assert germany.get_free_mils() == 29

def test_check_for_finished_buildings_for_pass_month(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 6 months pass
    for i in range(6): 
        new_game.pass_month()
    
    assert new_game.get_date().get_day() == 1
    assert new_game.get_date().get_month() == 7
    assert new_game.get_date().get_year() == 1936

    #Then the civs should be finished and the construction line should be removed
    assert construction_line_baden_mil.get_construction_cost() == 3540
    assert construction_line_baden_mil.get_amount_of_constructions() == 2
    assert germany.get_construction().get_construction_line_size() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert germany.get_free_civs() == 6
    print(germany.get_total_civs())
    print(germany.get_total_mils())


def test_construction_line_gets_removed_if_mil_finishes_and_there_is_only_one_mil_in_construction_line(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 360 days pass
    for i in range(365): 
        new_game.pass_day()

    #Then the first mil should finish and the construction line should be removed
    assert construction_line_brandenburg_civ.get_construction_cost() == 10500
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert germany.get_construction().get_construction_line_size() == 1
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert germany.get_total_civs() + germany.get_total_mils() == 66
    assert germany.get_free_civs() == 7

def test_construction_line_gets_removed_if_three_mils_finish(germany, new_game): 
    #Given default Germany start

    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 360 days pass
    for i in range(360): 
        new_game.pass_day()

    #Then the mils should be finished and the construction line should be removed
    assert germany.get_construction().get_construction_line_size() == 0
    assert germany.get_free_civs() == 20

def test_everything_continues_even_if_nothing_is_being_constructed(germany, new_game): 
    #Given default Germany start

    baden_state = germany.states["baden"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 360 days pass
    for i in range(360): 
        new_game.pass_day()

    #Then the civs should be finished and the construction line should be removed
    assert germany.get_construction().get_construction_line_size() == 0
    assert germany.get_free_civs() == 20

    #When 50 more days pass
    for i in range(50): 
        new_game.pass_day()

    #Then everything should be as before
    assert germany.get_construction().get_construction_line_size() == 0
    assert germany.get_free_civs() == 20

def test_constructions_can_start_later_and_still_work(germany, new_game): 
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

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the first CIV should finish
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_baden_mil.get_construction_cost() == 3600
    assert construction_line_baden_mil.get_assigned_civs() == 6
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert construction_line_baden_mil.get_amount_of_constructions() == 2
    assert germany.get_construction().get_construction_line_size() == 2

    #When 30 more days pass
    for i in range(30): 
        new_game.pass_day()
    
    #Then these should be the updates values
    assert construction_line_brandenburg_civ.get_construction_cost() == 9000
    assert construction_line_baden_mil.get_construction_cost() == 2880
    assert construction_line_baden_mil.get_assigned_civs() == 6
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert construction_line_baden_mil.get_amount_of_constructions() == 2
    assert germany.get_construction().get_construction_line_size() == 2
    
    #When new constructions start
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    assert germany.get_free_civs() == 0

    #and 155 days pass
    for i in range(155): 
        new_game.pass_day()

    #Then these should be the new costs
    assert construction_line_brandenburg_civ.get_construction_cost() == 10500

    #Mil construction done for the first 150 days is with 6 free factories, accounting for 3600 construction cost, reducing it down to 6480 cost
    #Mil construction for the 5 days after is with 7 free factories, accounting for 140 construction cost, reduing it down to 6340
    assert construction_line_baden_mil.get_construction_cost() == 6340
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert construction_line_baden_mil.get_amount_of_constructions() == 2
    assert construction_line_holstein_dockyard.get_amount_of_constructions() == 1
    assert germany.get_construction().get_construction_line_size() == 3

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_assigned_civs() == 7
    assert germany.get_total_civs() == 37
    assert germany.get_free_civs() == 0


def test_construction_carries_over_to_next_factory_in_construction_line(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    assert germany.get_free_civs() == 20

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    #and when when one of the civs has 30 construction left over

    set_construction_left(construction_line_brandenburg_civ, 30)

    #Then it should give the 30 extra to the next civ in line after a day passes

    new_game.pass_day()

    assert construction_line_brandenburg_civ.get_construction_cost() == 10770
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert germany.get_construction().get_construction_line_size() == 1

def test_construction_does_not_carry_over_to_other_construction_line(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #and when when the Brandenburg civ has 30 construction left over

    set_construction_left(construction_line_brandenburg_civ, 30)

    #Then it should not give 30 extra to the Baden mil after a day

    new_game.pass_day()

    assert construction_line_baden_mil.get_construction_cost() == 7180
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400

def test_amount_of_time_left_on_factories_with_default_construction_speed(germany, new_game): 
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
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 360

def test_amount_of_time_left_for_factories_with_no_assigned_civs_is_infinite(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then the time left should be infinite for the dockyard
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

def test_construction_time_reduces_by_one_after_day_passes(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then the times should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

    #When a day passes
    new_game.pass_day()

    #Then the construction times should be 1 less
    assert construction_line_brandenburg_civ.get_time_left() == 179
    assert construction_line_baden_mil.get_time_left() == 359
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

def test_construction_time_reduces_after_many_day_pass(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then the times should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

    #When a day passes
    for i in range(155): 
        new_game.pass_day()

    #Then the construction times should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 25
    assert construction_line_baden_mil.get_time_left() == 205
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

def test_construction_cost_is_the_same_even_if_priority_level_changes(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    #and some time passes
    for i in range(123): 
        new_game.pass_day()

    #Then the construction costs should be the following
    construction_line_brandenburg_civ.get_construction_cost() == 3420
    construction_line_baden_mil.get_construction_cost() == 4740
    construction_line_holstein_dockyard.get_construction_cost() == 6400
    
    #When the priority level is moved
    move_priority_level(find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany), 0, germany)

    assert construction_line_brandenburg_civ.get_priority() == 1
    assert construction_line_baden_mil.get_priority() == 2
    assert construction_line_holstein_dockyard.get_priority() == 0

    #Then the construction costs should be the same
    assert construction_line_brandenburg_civ.get_construction_cost() == 3420
    assert construction_line_baden_mil.get_construction_cost() == 4740
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400

def test_construction_time_resets_when_building_finishes(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    #and one factory finishes
    for i in range(180): 
        new_game.pass_day()
    
    #Then the time should be reset to 180 days
    assert construction_line_brandenburg_civ.get_time_left() == 180
    
def test_construction_time_for_multiple_buildings_in_construction_line(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    #and one factory finishes
    for i in range(225): 
        new_game.pass_day()
    
    #Then the time should be reset to 180 days
    assert construction_line_brandenburg_civ.get_time_left() == 135

def test_construction_time_changes_when_priority_levels_change(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    #and some time passes
    for i in range(123): 
        new_game.pass_day()

    #Then the construction times should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 57
    assert construction_line_baden_mil.get_time_left() == 237
    assert construction_line_holstein_dockyard.get_time_left() == math.inf
    
    #When the priority level is moved
    move_priority_level(find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany), 0, germany)

    assert construction_line_brandenburg_civ.get_priority() == 1
    assert construction_line_baden_mil.get_priority() == 2
    assert construction_line_holstein_dockyard.get_priority() == 0

    #Then the construction times should be the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 3420
    assert construction_line_baden_mil.get_construction_cost() == 4740
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400

    assert construction_line_brandenburg_civ.get_time_left() == 171
    assert construction_line_baden_mil.get_time_left() == math.inf
    assert construction_line_holstein_dockyard.get_time_left() == 107

    #When more days pass
    for i in range(78): 
        new_game.pass_day()

    #Then the construction time should be correct
    assert construction_line_brandenburg_civ.get_time_left() == 93
    assert construction_line_baden_mil.get_time_left() == math.inf
    assert construction_line_holstein_dockyard.get_time_left() == 29

def test_construction_time_changes_when_construction_line_is_deleted(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    #and some time passes
    for i in range(179): 
        new_game.pass_day()

    #Then the construction times should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 1
    assert construction_line_baden_mil.get_time_left() == 181
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

    #When one more day passes
    new_game.pass_day()

    #Then the construction times should be changed when construction line is deleted
    assert construction_line_baden_mil.get_construction_cost() == 3600
    assert construction_line_holstein_dockyard.get_construction_cost() == 6400

    assert construction_line_baden_mil.get_time_left() == 60
    assert construction_line_holstein_dockyard.get_time_left() == 267

    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert construction_line_holstein_dockyard.get_assigned_civs() == 6

def test_should_add_civ_to_count_if_civ_finishes_building(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #and when when the construction left is small
    set_construction_left(construction_line_brandenburg_civ, 30)
    set_construction_left(construction_line_baden_mil, 10)

    #Then the time left should be the following

    new_game.pass_day()

    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 300
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_assigned_civs() == 6
    assert construction_line_holstein_dockyard.get_assigned_civs() == 0

def test_civ_count_is_updated_if_civ_finishes_construction(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert germany.get_total_civs() == 35

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the amount of civs should be one larger for country and state
    assert germany.get_total_civs() == 36
    assert brandenburg_state.get_civs() == 5

def test_mil_count_is_updated_if_mil_finishes_construction(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)

    assert germany.get_total_mils() == 28
    assert brandenburg_state.get_mils() == 5

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the amount of mils should be one larger for country and state
    assert germany.get_total_mils() == 29
    assert brandenburg_state.get_mils() == 6

def test_dockyard_count_is_updated_if_dockyard_finishes_construction(germany, new_game): 
    #Given default Germany start

    holstein_state = germany.states["holstein"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    assert germany.get_total_dockyards() == 10
    assert holstein_state.get_dockyards() == 6

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the amount of mils should be one larger for country and state
    assert germany.get_total_dockyards() == 11
    assert holstein_state.get_dockyards() == 7

def test_free_construction_slots_should_be_affected_by_finished_factory(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    assert brandenburg_state.get_free_construction_slots() == 3

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert brandenburg_state.get_free_construction_slots() == 2

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    #Then the amount of free slots should be 2

    assert brandenburg_state.get_free_construction_slots() == 2

def test_should_not_be_able_to_start_construction_in_state_where_factories_are_already_constructed(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    assert brandenburg_state.get_free_construction_slots() == 3

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert brandenburg_state.get_free_construction_slots() == 0

    #When 180 days pass
    for i in range(540): 
        new_game.pass_day()

    #Then the amount of free slots should be 0
    assert brandenburg_state.get_free_construction_slots() == 0

    #When a new civ starts construction in Brandenburg
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then there should not be a new construction line created because there are no more free construction slots

    assert germany.construction.get_construction_line_size() == 0

def test_more_free_civs_when_civ_is_constructed(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    assert germany.get_free_civs() == 5

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 64

    #Then germany should have one more free civ(is not eaten up by consumer goods because 0.24*65=15.36, and it rounds down)
    assert germany.get_civs_used_on_consumer_goods() == 15
    assert germany.get_free_civs() == 21

def test_free_civs_when_construction_done_and_a_construction_is_still_ongoing(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    total_civs = germany.get_total_civs()
    assert total_civs == 35

    assert germany.get_free_civs() == 5

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 64

    total_civs = germany.get_total_civs()
    assert total_civs == 36

    #Then germany should have one more free civ(is not eaten up by consumer goods because 0.24*65=15.36, and it rounds down)
    assert germany.get_civs_used_on_consumer_goods() == 15
    assert germany.get_free_civs() == 6


def test_civs_help_constructing_when_finished(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)

    assert germany.get_construction().get_construction_line_size() == 2

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    total_civs = germany.get_total_civs()
    assert total_civs == 35

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)

    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_mil.get_time_left() == 360

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_mil.get_assigned_civs() == 5

    #When 180 days pass
    for i in range(180): 
        new_game.pass_day()

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 64

    total_civs = germany.get_total_civs()
    assert total_civs == 36

    assert germany.get_civs_used_on_consumer_goods() == 15
    assert germany.get_free_civs() == 0

    #Then the time left should be updated
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_mil.get_time_left() == 150

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_mil.get_assigned_civs() == 6

def test_consumer_goods_affect_the_amount_of_free_factories(germany, new_game): 
    #Given default Germany start

    moselland_state = germany.states["moselland"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    #When the 4 civs are done
    for i in range(720): 
        new_game.pass_day()

    #Then the amount of free civs should be 23, because 20 is the default and 3 of them become free, while 1 gets used on consumer goods

    assert germany.get_free_civs() == 23
    assert germany.get_civs_used_on_consumer_goods() == 16


def test_constructed_mils_should_affect_the_amount_of_free_civs_and_civs_used_on_consumer_goods(germany, new_game): 
    #Given default Germany start

    moselland_state = germany.states["moselland"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    #When the 4 mils are done
    for i in range(480): 
        new_game.pass_day()

    #Then the amount of free civs should be 19, because 20 is the default and with 4 extra factories, consumer goods require an extra one

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 67

    assert germany.get_free_civs() == 19
    assert germany.get_civs_used_on_consumer_goods() == 16

def test_constructed_mils_should_not_affect_the_amount_of_free_civs_and_civs_used_on_consumer_goods_if_amount_dont_add_up_to_new_consumer_goods_factories_amount(germany, new_game): 
    #Given default Germany start

    moselland_state = germany.states["moselland"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    #When the 3 mils are done
    for i in range(360): 
        new_game.pass_day()

    #Then the amount of free civs should be 20, because 20 is the default and with 3 extra factories, consumer goods require 15 still

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 66

    assert germany.get_free_civs() == 20
    assert germany.get_civs_used_on_consumer_goods() == 15

def test_constructed_dockyards_should_not_affect_the_amount_of_free_civs_and_civs_used_on_consumer_goods(germany, new_game): 
    #Given default Germany start

    konigsberg_state = germany.states["konigsberg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, konigsberg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, konigsberg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, konigsberg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, konigsberg_state, germany)

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    assert germany.get_civs_used_on_consumer_goods() == 15

    #When the 4 dockyards are done
    for i in range(427): 
        new_game.pass_day()

    #Then the amount of free civs should be 20, because 20 is the default and dockyards don't affect free civs or consumer goods factories

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63

    assert germany.get_total_dockyards() == 14

    assert germany.get_free_civs() == 20
    assert germany.get_civs_used_on_consumer_goods() == 15

def test_construction_time_for_pass_month(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    assert construction_line_brandenburg_civ.get_time_left() == 180

    #and a month passes
    new_game.pass_month()

    #Then there should be 149 days left on the construction
    assert construction_line_brandenburg_civ.get_time_left() == 149

    #When another month passes
    new_game.pass_month()

    #Then there should be 121 days left
    assert construction_line_brandenburg_civ.get_time_left() == 121

def test_constructing_factories_affected_by_finished_factories_and_free_civs_and_consumer_goods_factories(germany, new_game): 
    #Given default Germany start

    moselland_state = germany.states["moselland"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)

    construction_line_moselland_civ = find_construction_line(construction_types.Constructions.CIV, moselland_state, germany)

    #and the first 3 civs are done
    for i in range(540): 
        new_game.pass_day()
    
    #Then the amount of free civs is 8

    assert germany.get_free_civs() == 8
    assert germany.get_civs_used_on_consumer_goods() == 15

    #When new constructions start
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    assert construction_line_baden_mil.get_assigned_civs() == 8
    assert germany.get_free_civs() == 0
    assert germany.get_civs_used_on_consumer_goods() == 15

    #and the last civ is constructed
    for i in range(180): 
        new_game.pass_day()

    #Then the amount of assigned civs to the dockyard line should be 8, and civs used on consumer goods should be 16
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert construction_line_holstein_dockyard.get_assigned_civs() == 8
    assert germany.get_free_civs() == 0
    assert germany.get_civs_used_on_consumer_goods() == 16

    #When everything finishes: 
    for i in range(1000): 
        new_game.pass_day()

    #Then the free civs and civs on consumer goods should be correct

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 71
    assert germany.get_total_civs() == 39
    assert germany.get_total_dockyards() == 11

    assert germany.get_free_civs() == 22
    assert germany.get_civs_used_on_consumer_goods() == 17

def test_free_civs_and_consumer_goods_factories_work_in_scenario_one(germany, new_game): 
    #Given default Germany start

    moselland_state = germany.states["moselland"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)

    #and everything is done
    for i in range (2000): 
        new_game.pass_day()

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 72
    assert germany.get_total_civs() == 40
    assert germany.get_total_mils() == 32
    assert germany.get_total_dockyards() == 11
    
    #Then the amount of free civs and civs used on consumer goods is the following
    assert germany.get_free_civs() == 23
    assert germany.get_civs_used_on_consumer_goods() == 17

def test_free_civs_and_consumer_goods_factories_work_in_scenario_two(germany, new_game): 
    #Given default Germany start

    moselland_state = germany.states["moselland"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    hannover_state = germany.states["hannover"]
    ermland_masuren_state = germany.states["ermland_masuren"]
    wurttemberg_state = germany.states["wurttemberg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, hannover_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, hannover_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, hannover_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, ermland_masuren_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, ermland_masuren_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, wurttemberg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, wurttemberg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, wurttemberg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, wurttemberg_state, germany)

    #and everything is done
    for i in range (5000): 
        new_game.pass_day()

    total_factories = germany.get_total_civs() + germany.get_total_mils() 
    assert total_factories == 63 + 18
    assert germany.get_total_civs() == 46
    assert germany.get_total_mils() == 35
    assert germany.get_total_dockyards() == 11
    
    #Then the amount of free civs and civs used on consumer goods is the following
    assert germany.get_free_civs() == 27
    assert germany.get_civs_used_on_consumer_goods() == 19

def test_after_constructing_83_mils_there_should_be_no_free_factories_left(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #Adds 1000 construction slots for testing purposes
    add_total_construction_slots(brandenburg_state, 1000)

    #When germany has constructed 83 more mils
    for i in range(83): 
        germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)

    #30000 days to make sure all mils are done
    for i in range(30000): 
        new_game.pass_day()

    #Then there should be no free civs(since all are used on consumer goods)
    assert germany.get_total_mils() == 111
    assert germany.get_total_civs() == 35

    assert germany.get_free_civs() == 0
    assert germany.get_civs_used_on_consumer_goods() == 35

    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    #Then the time left should be infinite
    assert construction_line_baden_civ.get_time_left() == math.inf



def test_after_having_82_mils_there_should_be_one_free_factories_left(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #Adds 1000 construction slots for testing purposes
    add_total_construction_slots(brandenburg_state, 1000)

    #When germany has constructed 82 more mils
    for i in range(82): 
        germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)

    #30000 days to make sure all mils are done
    for i in range(30000): 
        new_game.pass_day()

    #Then there should be 1 free civs(since 34 are used on consumer goods)
    assert germany.get_total_mils() == 110
    assert germany.get_total_civs() == 35

    assert germany.get_free_civs() == 1
    assert germany.get_civs_used_on_consumer_goods() == 34

    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    #Then the time left should be 2700 days
    assert construction_line_baden_civ.get_time_left() == 2700

def test_can_delete_civ(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When a civ is deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    #Then it should be successful, and the amount of civs in Brandenburg should be reduced to 3
    assert brandenburg_state.get_civs() == 3
    assert germany.get_total_civs() == 34

def test_can_delete_mil(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When a mil is deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)

    #Then it should be successful, and the amount of mils in Brandenburg should be reduced to 4
    assert brandenburg_state.get_civs() == 4
    assert germany.get_total_mils() == 27

def test_can_delete_dockyard(germany, new_game): 
    #Given default Germany start

    holstein_state = germany.states["holstein"]

    #When a dockyard is deleted
    delete_factory(germany, holstein_state, construction_types.Constructions.DOCKYARD)

    #Then it should be successful, and the amount of dockyards in Brandenburg should be reduced to 5
    assert holstein_state.get_dockyards() == 5
    assert germany.get_total_dockyards() == 9

def test_a_deleted_factory_has_no_effect_on_other_factory_counts(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When a civ is deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    #Then it should be successful, and the amount of civs in Brandenburg should be reduced to 3, and the amount of other factories should see no change
    assert brandenburg_state.get_civs() == 3
    assert brandenburg_state.get_mils() == 5
    assert brandenburg_state.get_dockyards() == 0

    assert germany.get_total_civs() == 34
    assert germany.get_total_mils() == 28
    assert germany.get_total_dockyards() == 10


def test_can_delete_different_factories(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When some factories are deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)
    delete_factory(germany, baden_state, construction_types.Constructions.MIL)
    delete_factory(germany, holstein_state, construction_types.Constructions.DOCKYARD)
    delete_factory(germany, holstein_state, construction_types.Constructions.DOCKYARD)

    #Then it should be successful, and the amount of factories should be correct in states and country
    assert brandenburg_state.get_civs() == 3
    assert brandenburg_state.get_mils() == 3
    assert brandenburg_state.get_dockyards() == 0

    assert baden_state.get_civs() == 0
    assert baden_state.get_mils() == 1
    assert baden_state.get_dockyards() == 0

    assert holstein_state.get_civs() == 0
    assert holstein_state.get_mils() == 1
    assert holstein_state.get_dockyards() == 4

    assert germany.get_total_civs() == 34
    assert germany.get_total_mils() == 25
    assert germany.get_total_dockyards() == 8

def test_cannot_delete_civ_if_there_is_no_civ_in_state(germany, new_game): 
    #Given default Germany start

    baden_state = germany.states["baden"]

    #When a civ is deleted in Baden(which has no civs)
    delete_factory(germany, baden_state, construction_types.Constructions.CIV)

    #Then the deletion should not happen, and the amount of factories should stay the same
    assert baden_state.get_civs() == 0
    assert baden_state.get_mils() == 2
    assert baden_state.get_dockyards() == 0

    assert germany.get_total_civs() == 35
    assert germany.get_total_mils() == 28
    assert germany.get_total_dockyards() == 10

def test_cannot_delete_mil_if_there_is_no_mil_in_state(germany, new_game): 
    #Given default Germany start

    weser_ems_state = germany.states["weser_ems"]

    #When a mil is deleted in weser-ems(which has no mils)
    delete_factory(germany, weser_ems_state, construction_types.Constructions.MIL)

    #Then the deletion should not happen, and the amount of factories should stay the same
    assert weser_ems_state.get_civs() == 2
    assert weser_ems_state.get_mils() == 0
    assert weser_ems_state.get_dockyards() == 2

    assert germany.get_total_civs() == 35
    assert germany.get_total_mils() == 28
    assert germany.get_total_dockyards() == 10

def test_cannot_delete_dockyard_if_there_is_no_dockyard_in_state(germany, new_game): 
    #Given default Germany start

    schleswig_state = germany.states["schleswig"]

    #When a dockyard is deleted in schleswig(which has no dockyards)
    delete_factory(germany, schleswig_state, construction_types.Constructions.DOCKYARD)

    #Then the deletion should not happen, and the amount of factories should stay the same
    assert schleswig_state.get_civs() == 0
    assert schleswig_state.get_mils() == 1
    assert schleswig_state.get_dockyards() == 0

    assert germany.get_total_civs() == 35
    assert germany.get_total_mils() == 28
    assert germany.get_total_dockyards() == 10

def test_cannot_delete_dockyard_if_state_is_not_coastal(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When a dockyard is deleted in brandenburg(which is not coastal)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.DOCKYARD)

    #Then the deletion should not happen, and the amount of factories should stay the same
    assert brandenburg_state.get_civs() == 4
    assert brandenburg_state.get_mils() == 5
    assert brandenburg_state.get_dockyards() == 0

    assert germany.get_total_civs() == 35
    assert germany.get_total_mils() == 28
    assert germany.get_total_dockyards() == 10

def test_can_construct_a_civ_and_remove_it_afterward(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    #and it finishes building
    for i in range(180):
        new_game.pass_day()

    #Then there should be 5 civs in Brandenburg
    assert brandenburg_state.get_civs() == 5

    #When a civ is then deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    #Then the amount of civs in Brandenburg should be 4
    assert brandenburg_state.get_civs() == 4

def test_deleted_factories_should_affect_free_construction_slots_in_state(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When a civ and mil is deleted from Brandenburg 
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)

    #Then the amount of free construction slots should be 5 in Brandenburg
    assert brandenburg_state.get_free_construction_slots() == 5

def test_deleted_and_built_factories_should_affect_free_construction_slots_in_state(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When a civ and mil is deleted from Brandenburg 
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)

    #Then the amount of free construction slots should be 5 in Brandenburg
    assert brandenburg_state.get_free_construction_slots() == 5

    #When new factories are built in Brandenburg
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)

    #Then the amount of free construction slots should be 2
    assert brandenburg_state.get_free_construction_slots() == 2

    #When the factories finish
    for i in range(500): 
        new_game.pass_day()
    
    #Then the amount of free construction slots should be 2 still
    assert brandenburg_state.get_free_construction_slots() == 2

def test_construction_slots_being_filled_with_deleted_and_constructed_factories_means_more_factories_cannot_be_built(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    #baden_state = germany.states["baden"]

    #When a civ and mil is deleted from Brandenburg 
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)

    #Then the amount of free construction slots should be 5 in Brandenburg
    assert brandenburg_state.get_free_construction_slots() == 5

    #When new civs are built in Brandenburg which fills up all free construction slots
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)

    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then the amount of free construction slots should be 0
    assert brandenburg_state.get_free_construction_slots() == 0
    construction_line_baden_civ.get_amount_of_constructions() == 5

    #and no new ones can be constructed
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    
    construction_line_baden_civ.get_amount_of_constructions() == 5
    germany.get_construction().get_construction_line_size() == 1

    #When the factories finish
    for i in range(1000): 
        new_game.pass_day()
    
    #Then the amount of free construction slots should be 0 still
    assert brandenburg_state.get_free_construction_slots() == 0

def test_deleted_civ_should_affect_time_left(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    #Then the time left should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

    #When two civs are deleted(since 1 civ will just reduce the amount of consumer goods used)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    assert germany.get_civs_used_on_consumer_goods() == 14
    assert germany.get_free_civs() == 0

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_assigned_civs() == 4

    #Then the construction times should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 450
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

def test_deleting_one_civ_has_no_effect_on_time_left(germany, new_game):  
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    #Then the time left should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

    #When one civs are deleted, then it will take away one civ on consumer goods, since 62*0.24=14.88, rounded down to 14 civs used on consumer goods, while 20 are used on constructions
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    assert germany.get_civs_used_on_consumer_goods() == 14
    assert germany.get_free_civs() == 0

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_assigned_civs() == 5

    #Then the construction times should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

def test_deleting_civs_until_a_construction_line_has_no_assigned_civs_means_the_time_left_becomes_infinite(germany, new_game):
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]
    sachsen_state = germany.states["sachsen"]
    assert germany.get_free_civs() == 20
  
    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)
    
    #Then the time left should be the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

    #When 7 civs are deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, sachsen_state, construction_types.Constructions.CIV)
    delete_factory(germany, sachsen_state, construction_types.Constructions.CIV)
    delete_factory(germany, sachsen_state, construction_types.Constructions.CIV)
    delete_factory(germany, sachsen_state, construction_types.Constructions.CIV)

    assert germany.get_total_civs() == 28
    assert germany.get_free_civs() == 0
    assert germany.get_civs_used_on_consumer_goods() == 13
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_assigned_civs() == 0
    assert construction_line_holstein_dockyard.get_assigned_civs() == 0

    #Then the time left on the Baden mil should be infinite
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_baden_mil.get_time_left() == math.inf
    assert construction_line_holstein_dockyard.get_time_left() == math.inf

def test_deleting_two_civs_should_affect_construction(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #and 30 days pass
    for i in range(30): 
        new_game.pass_day()

    #Then the construction costs should be the following
    #10800-(60*30)=9000
    assert construction_line_brandenburg_civ.get_construction_cost() == 9000
    #7200-(20*30)=6600
    assert construction_line_baden_mil.get_construction_cost() == 6600

    #When 2 civs are deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    assert germany.get_civs_used_on_consumer_goods() == 14
    #and 30 days pass
    for i in range(30): 
        new_game.pass_day()

    #Then the construction costs should be the following
    #9000-(60*30)=7200
    assert construction_line_brandenburg_civ.get_construction_cost() == 7200
    #6600-(16*30)=6120
    assert construction_line_baden_mil.get_construction_cost() == 6120

def test_deleting_one_civ_should_not_affect_construction(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #and 30 days pass
    for i in range(30): 
        new_game.pass_day()

    #Then the construction costs should be the following
    #10800-(60*30)=9000
    assert construction_line_brandenburg_civ.get_construction_cost() == 9000
    #7200-(20*30)=6600
    assert construction_line_baden_mil.get_construction_cost() == 6600

    #When 1 civ is deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    assert germany.get_civs_used_on_consumer_goods() == 14

    #and 30 days pass
    for i in range(30): 
        new_game.pass_day()

    #Then the construction costs should be the following(no factories are removed from construction, only factory used on consumer goods)
    #9000-(60*30)=7200
    assert construction_line_brandenburg_civ.get_construction_cost() == 7200
    #6600-(20*30)=6000
    assert construction_line_baden_mil.get_construction_cost() == 6000

def test_deleting_one_civ_should_affect_consumer_goods_factories(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When one civ is deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    #Then the amount of consumer goods factories should be one less, since 62*0.24=14.88
    assert germany.get_total_civs() == 34
    assert germany.get_free_civs() == 20
    assert germany.get_civs_used_on_consumer_goods() == 14

def test_deleting_two_civs_should_affect_consumer_goods_factories_and_free_civs(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When two civs are deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    #Then the amount of consumer goods factories should be one less, since 62*0.24=14.88
    assert germany.get_total_civs() == 33
    assert germany.get_free_civs() == 19
    assert germany.get_civs_used_on_consumer_goods() == 14

def test_deleting_one_mil_should_affect_consumer_goods_factories_and_free_civs(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When one mil is deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)

    #Then the amount of consumer goods factories and free civs should be the following
    assert germany.get_free_civs() == 21
    assert germany.get_civs_used_on_consumer_goods() == 14


def test_deleting_two_mils_should_affect_consumer_goods_factories_and_free_civs(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]

    #When one mil is deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.MIL)

    #Then the amount of consumer goods factories and free civs should be the following
    assert germany.get_free_civs() == 21
    assert germany.get_civs_used_on_consumer_goods() == 14

def test_deleting_one_dockyard_should_not_affect_consumer_goods_factories_or_free_civs(germany, new_game): 
    #Given default Germany start

    holstein_state = germany.states["holstein"]

    #When one dockyard is deleted
    delete_factory(germany, holstein_state, construction_types.Constructions.DOCKYARD)

    #Then the amount of consumer goods factories and free civs should be the same
    assert germany.get_free_civs() == 20
    assert germany.get_civs_used_on_consumer_goods() == 15

def test_deleting_two_dockyards_should_not_affect_consumer_goods_factories_or_free_civs(germany, new_game): 
    #Given default Germany start

    holstein_state = germany.states["holstein"]

    #When two dockyards are deleted
    delete_factory(germany, holstein_state, construction_types.Constructions.DOCKYARD)
    delete_factory(germany, holstein_state, construction_types.Constructions.DOCKYARD)

    #Then the amount of consumer goods factories and free civs should be the same
    assert germany.get_free_civs() == 20
    assert germany.get_civs_used_on_consumer_goods() == 15

def test_deleting_two_civs_and_switching_priority_levels_assigns_civs_correctly(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #and when two civs are deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    #Then the amount of assigned civs should be the following
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_civ.get_priority() == 0
    assert construction_line_baden_mil.get_assigned_civs() == 4
    assert construction_line_baden_mil.get_priority() == 1

    #When priority levels are switched
    move_priority_level(construction_line_brandenburg_civ, 1, germany)

    #Then the assigned civs should be the following
    assert construction_line_brandenburg_civ.get_assigned_civs() == 4
    assert construction_line_brandenburg_civ.get_priority() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_priority() == 0

    #When two new civs are constructed
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    

    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    move_priority_level(construction_line_baden_civ, 0, germany)

    #Then after 360 days, the assigned civs should be correct
    for i in range(360): 
        new_game.pass_day()

    assert germany.get_construction().get_construction_line_size() == 3

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    assert construction_line_baden_mil.get_priority() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 5

    assert construction_line_baden_civ.get_priority() == 0
    assert construction_line_baden_civ.get_assigned_civs() == 15

def test_deleting_construction_line_affects_priority_levels(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When constructions start in state
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then the priority levels should be the following
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_civ.get_priority() == 0

    assert construction_line_baden_mil.get_assigned_civs() == 5
    assert construction_line_baden_mil.get_priority() == 1

    assert construction_line_baden_civ.get_assigned_civs() == 0
    assert construction_line_baden_civ.get_priority() == 2

    assert construction_line_holstein_dockyard.get_assigned_civs() == 0
    assert construction_line_holstein_dockyard.get_priority() == 3

    #When a construction line is removed   
    remove_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)

    #Then the priority levels should be the following
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_priority() == 0

    assert construction_line_baden_civ.get_assigned_civs() == 5
    assert construction_line_baden_civ.get_priority() == 1

    assert construction_line_holstein_dockyard.get_assigned_civs() == 0
    assert construction_line_holstein_dockyard.get_priority() == 2

def test_finishing_construction_line_affects_priority_levels(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    holstein_state = germany.states["holstein"]

    #When constructions start in state
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.DOCKYARD, holstein_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)
    construction_line_holstein_dockyard = find_construction_line(construction_types.Constructions.DOCKYARD, holstein_state, germany)

    #Then the priority levels should be the following
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_civ.get_priority() == 0

    assert construction_line_baden_mil.get_assigned_civs() == 5
    assert construction_line_baden_mil.get_priority() == 1

    assert construction_line_baden_civ.get_assigned_civs() == 0
    assert construction_line_baden_civ.get_priority() == 2

    assert construction_line_holstein_dockyard.get_assigned_civs() == 0
    assert construction_line_holstein_dockyard.get_priority() == 3

    #When the Brandenburg civ finishes
    for i in range(180): 
        new_game.pass_day()

    #Then the priority levels should be the following
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_priority() == 0

    assert construction_line_baden_civ.get_assigned_civs() == 6
    assert construction_line_baden_civ.get_priority() == 1

    assert construction_line_holstein_dockyard.get_assigned_civs() == 0
    assert construction_line_holstein_dockyard.get_priority() == 2

    #When priority levels are now switched
    move_priority_level(construction_line_holstein_dockyard, 0, germany)

    #Then the priority levels should be the following
    assert construction_line_baden_mil.get_assigned_civs() == 6
    assert construction_line_baden_mil.get_priority() == 1

    assert construction_line_baden_civ.get_assigned_civs() == 0
    assert construction_line_baden_civ.get_priority() == 2

    assert construction_line_holstein_dockyard.get_assigned_civs() == 15
    assert construction_line_holstein_dockyard.get_priority() == 0
     
def test_switching_priority_levels_and_deleting_two_civs_assigns_civs_correctly(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #and when priority levels are switched
    move_priority_level(construction_line_baden_mil, 0, germany)

    #Then the assigned civs should be the following
    assert construction_line_brandenburg_civ.get_assigned_civs() == 5
    assert construction_line_brandenburg_civ.get_priority() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_priority() == 0

    #and when two civs are deleted
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)
    delete_factory(germany, brandenburg_state, construction_types.Constructions.CIV)

    #Then the amount of assigned civs should be the following
    assert construction_line_brandenburg_civ.get_assigned_civs() == 4
    assert construction_line_brandenburg_civ.get_priority() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 15
    assert construction_line_baden_mil.get_priority() == 0

    #When two new civs are constructed
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)    

    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    move_priority_level(construction_line_baden_civ, 0, germany)

    #Then after 360 days, the assigned civs should be correct
    for i in range(360): 
        new_game.pass_day()

    assert germany.get_construction().get_construction_line_size() == 3

    assert construction_line_brandenburg_civ.get_priority() == 2
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    assert construction_line_baden_mil.get_priority() == 1
    assert construction_line_baden_mil.get_assigned_civs() == 5

    assert construction_line_baden_civ.get_priority() == 0
    assert construction_line_baden_civ.get_assigned_civs() == 15

def test_deleting_a_civ_from_two_states_without_a_civ_should_leave_time_left_unaffected(germany, new_game): 
    #Given default Germany start

    schleswig_state = germany.states["schleswig"]
    vorpommern_state = germany.states["vorpommern"]
    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then the amount of time left is the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_baden_mil.get_assigned_civs() == 5

    #When civs are deleted from states which don't have any civs
    delete_factory(germany, schleswig_state, construction_types.Constructions.CIV)
    delete_factory(germany, vorpommern_state, construction_types.Constructions.CIV)

    #Then the time left should be the same(since no civs are deleted)
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_baden_mil.get_assigned_civs() == 5

def test_deleting_a_civ_from_two_states_without_a_civ_should_leave_time_left_unaffected(germany, new_game): 
    #Given default Germany start

    schleswig_state = germany.states["schleswig"]
    vorpommern_state = germany.states["vorpommern"]
    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then the amount of time left is the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_baden_mil.get_assigned_civs() == 5

    #When civs are deleted from states which don't have any civs
    delete_factory(germany, schleswig_state, construction_types.Constructions.CIV)
    delete_factory(germany, vorpommern_state, construction_types.Constructions.CIV)

    #Then the time left should be the same(since no civs are deleted)
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_baden_mil.get_assigned_civs() == 5

    assert germany.get_civs_used_on_consumer_goods() == 15

def test_deleting_a_mil_from_two_states_without_a_mil_it_should_leave_time_left_unaffected(germany, new_game): 
    #Given default Germany start

    thuringen_state = germany.states["thuringen"]
    vorpommern_state = germany.states["vorpommern"]
    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then the amount of time left is the following
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_baden_mil.get_assigned_civs() == 5

    #When civs are deleted from states which don't have any civs
    delete_factory(germany, thuringen_state, construction_types.Constructions.MIL)
    delete_factory(germany, vorpommern_state, construction_types.Constructions.MIL)

    #Then the time left should be the same(since no civs are deleted)
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_baden_mil.get_assigned_civs() == 5

    assert germany.get_civs_used_on_consumer_goods() == 15

def test_deleting_a_civ_from_two_states_without_a_civ_should_leave_construction_cost_unaffected(germany, new_game): 
    #Given default Germany start

    schleswig_state = germany.states["schleswig"]
    vorpommern_state = germany.states["vorpommern"]
    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then the construction cost is the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_construction_cost() == 7200
    assert construction_line_baden_mil.get_assigned_civs() == 5

    #When civs are deleted from states which don't have any civs
    delete_factory(germany, schleswig_state, construction_types.Constructions.CIV)
    delete_factory(germany, vorpommern_state, construction_types.Constructions.CIV)

    #and 60 days pass
    for i in range(60): 
        new_game.pass_day()

    #Then the construction cost should be the same(since no civs are deleted)
    assert construction_line_brandenburg_civ.get_construction_cost() == 7200
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_construction_cost() == 6000
    assert construction_line_baden_mil.get_assigned_civs() == 5

    assert germany.get_civs_used_on_consumer_goods() == 15

def test_deleting_a_civ_from_two_states_without_a_civ_should_leave_construction_cost_unaffected(germany, new_game): 
    #Given default Germany start

    thuringen_state = germany.states["thuringen"]
    vorpommern_state = germany.states["vorpommern"]
    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    #Then the construction cost is the following
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_construction_cost() == 7200
    assert construction_line_baden_mil.get_assigned_civs() == 5

    #When civs are deleted from states which don't have any civs
    delete_factory(germany, thuringen_state, construction_types.Constructions.MIL)
    delete_factory(germany, vorpommern_state, construction_types.Constructions.MIL)

    #and 60 days pass
    for i in range(60): 
        new_game.pass_day()

    #Then the construction cost should be the same(since no civs are deleted)
    assert construction_line_brandenburg_civ.get_construction_cost() == 7200
    assert construction_line_brandenburg_civ.get_assigned_civs() == 15

    assert construction_line_baden_mil.get_construction_cost() == 6000
    assert construction_line_baden_mil.get_assigned_civs() == 5

    assert germany.get_civs_used_on_consumer_goods() == 15

def test_deleting_all_civs_means_nothing_can_be_constructed(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    moselland_state = germany.states["moselland"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, baden_state, germany)    

    construction_line_brandenburg_civ = find_construction_line(construction_types.Constructions.CIV, brandenburg_state, germany)
    construction_line_baden_mil = find_construction_line(construction_types.Constructions.MIL, baden_state, germany)

    assert germany.get_total_civs() == 35

    assert construction_line_brandenburg_civ.get_assigned_civs() == 15
    assert construction_line_brandenburg_civ.get_time_left() == 180
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800

    assert construction_line_baden_mil.get_assigned_civs() == 5
    assert construction_line_baden_mil.get_time_left() == 360
    assert construction_line_baden_mil.get_construction_cost() == 7200

    #and all civs are deleted in Germany
    delete_all_factories_of_type(germany, construction_types.Constructions.CIV)

    assert germany.get_total_civs() == 0
    assert germany.get_civs_used_on_consumer_goods() == 0

    #Then the time left and construction costs should be the following
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0
    assert construction_line_brandenburg_civ.get_time_left() == math.inf
    assert construction_line_brandenburg_civ.get_construction_cost() == 10800

    assert construction_line_baden_mil.get_assigned_civs() == 0
    assert construction_line_baden_mil.get_time_left() == math.inf
    assert construction_line_baden_mil.get_construction_cost() == 7200

    assert brandenburg_state.get_free_construction_slots() == 6

    #When some new constructions happen
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, moselland_state, germany)

    construction_line_moselland_civ = find_construction_line(construction_types.Constructions.CIV, moselland_state, germany)

    move_priority_level(construction_line_moselland_civ, 1, germany)

    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 7

    #Then the amount of civs used on consumer goods should be the following when the constructions finish
    germany.get_construction().finish_construction(construction_line_brandenburg_civ)
    #29*0.24=6.96 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 1
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 6
    assert brandenburg_state.get_free_construction_slots() == 0
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    germany.get_construction().finish_construction(construction_line_brandenburg_civ)
    #30*0.24=7.20 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 2
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 5
    assert brandenburg_state.get_free_construction_slots() == 0
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    germany.get_construction().finish_construction(construction_line_brandenburg_civ)
    #31*0.24=7.44 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 3
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 4
    assert brandenburg_state.get_free_construction_slots() == 0
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    germany.get_construction().finish_construction(construction_line_brandenburg_civ)
    #32*0.24=7.68 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 4
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 3
    assert brandenburg_state.get_free_construction_slots() == 0
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    germany.get_construction().finish_construction(construction_line_brandenburg_civ)
    #33*0.24=7.92 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 5
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 2
    assert brandenburg_state.get_free_construction_slots() == 0
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    germany.get_construction().finish_construction(construction_line_brandenburg_civ)
    #34*0.24=8.16 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 6
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_civ.get_amount_of_constructions() == 1
    assert brandenburg_state.get_free_construction_slots() == 0
    assert construction_line_brandenburg_civ.get_assigned_civs() == 0

    germany.get_construction().finish_construction(construction_line_brandenburg_civ)
    #35*0.24=8.4 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 7
    assert germany.get_free_civs() == 0

    assert germany.get_construction().get_construction_line_size() == 2

    germany.get_construction().finish_construction(construction_line_moselland_civ)
    #36*0.24=8.64 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 8
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_civ.get_amount_of_constructions() == 6
    assert construction_line_moselland_civ.get_assigned_civs() == 0

    germany.get_construction().finish_construction(construction_line_moselland_civ)
    #37*0.24=8.88 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 8
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_civ.get_amount_of_constructions() == 5
    assert construction_line_moselland_civ.get_assigned_civs() == 1

    germany.get_construction().finish_construction(construction_line_moselland_civ)
    #38*0.24=9.12 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_civ.get_amount_of_constructions() == 4
    assert construction_line_moselland_civ.get_assigned_civs() == 1

    germany.get_construction().finish_construction(construction_line_moselland_civ)
    #39*0.24=9.36 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_civ.get_amount_of_constructions() == 3
    assert construction_line_moselland_civ.get_assigned_civs() == 2

    germany.get_construction().finish_construction(construction_line_moselland_civ)
    #40*0.24=9.6 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_civ.get_amount_of_constructions() == 2
    assert construction_line_moselland_civ.get_assigned_civs() == 3

    germany.get_construction().finish_construction(construction_line_moselland_civ)
    #41*0.24=9.84 vs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_civ.get_amount_of_constructions() == 1
    assert construction_line_moselland_civ.get_assigned_civs() == 4

    germany.get_construction().finish_construction(construction_line_moselland_civ)
    #42*0.24=10.08 vs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 10
    assert germany.get_free_civs() == 0
    assert construction_line_baden_mil.get_assigned_civs() == 4

def test_deleting_all_mils_should_affect_free_civs_and_consumer_goods_factories(germany, new_game): 
    #Given default Germany start

    brandenburg_state = germany.states["brandenburg"]
    baden_state = germany.states["baden"]
    moselland_state = germany.states["moselland"]

    #When constructions start in states
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.CIV, baden_state, germany)

    construction_line_brandenburg_mil = find_construction_line(construction_types.Constructions.MIL, brandenburg_state, germany)
    construction_line_baden_civ = find_construction_line(construction_types.Constructions.CIV, baden_state, germany)

    assert germany.get_total_civs() == 35

    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_brandenburg_mil.get_time_left() == 120
    assert construction_line_brandenburg_mil.get_construction_cost() == 7200

    assert construction_line_baden_civ.get_assigned_civs() == 5
    assert construction_line_baden_civ.get_time_left() == 540
    assert construction_line_baden_civ.get_construction_cost() == 10800

    #and all mils are deleted in Germany
    delete_all_factories_of_type(germany, construction_types.Constructions.MIL)

    assert germany.get_total_mils() == 0
    assert germany.get_civs_used_on_consumer_goods() == 8

    #Then the time left and construction costs should be the following
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_brandenburg_mil.get_time_left() == 120
    assert construction_line_brandenburg_mil.get_construction_cost() == 7200

    assert construction_line_baden_civ.get_assigned_civs() == 12
    assert construction_line_baden_civ.get_time_left() == 225
    assert construction_line_baden_civ.get_construction_cost() == 10800

    assert brandenburg_state.get_free_construction_slots() == 7

    #When some new constructions happen
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, brandenburg_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)
    germany.construction.start_construction(construction_types.Constructions.MIL, moselland_state, germany)

    construction_line_moselland_mil = find_construction_line(construction_types.Constructions.MIL, moselland_state, germany)

    move_priority_level(construction_line_moselland_mil, 1, germany)

    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 8

    #Then the amount of civs used on consumer goods should be the following when the constructions finish
    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #36*0.24=8.64 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 8
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 7
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_moselland_mil.get_assigned_civs() == 12

    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #37*0.24=8.88 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 8
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 6
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_moselland_mil.get_assigned_civs() == 12

    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #38*0.24=9.12 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 5
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_moselland_mil.get_assigned_civs() == 11

    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #39*0.24=9.36 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 4
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_moselland_mil.get_assigned_civs() == 11

    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #40*0.24=9.6 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 3
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_moselland_mil.get_assigned_civs() == 11

    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #41*0.24=9.84 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 9
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 2
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_moselland_mil.get_assigned_civs() == 11

    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #42*0.24=10.08 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 10
    assert germany.get_free_civs() == 0
    assert construction_line_brandenburg_mil.get_amount_of_constructions() == 1
    assert construction_line_brandenburg_mil.get_assigned_civs() == 15
    assert construction_line_moselland_mil.get_assigned_civs() == 10

    germany.get_construction().finish_construction(construction_line_brandenburg_mil)
    #43*0.24=10.32 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 10
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_mil.get_assigned_civs() == 15
    assert construction_line_baden_civ.get_assigned_civs() == 10

    assert germany.get_construction().get_construction_line_size() == 2

    construction_line_moselland_mil.get_amount_of_constructions() == 6

    germany.get_construction().finish_construction(construction_line_moselland_mil)
    #44*0.24=10.56 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 10
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_mil.get_amount_of_constructions() == 5
    assert construction_line_moselland_mil.get_assigned_civs() == 15
    assert construction_line_baden_civ.get_assigned_civs() == 10

    germany.get_construction().finish_construction(construction_line_moselland_mil)
    #45*0.24=10.8 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 10
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_mil.get_amount_of_constructions() == 4
    assert construction_line_moselland_mil.get_assigned_civs() == 15
    assert construction_line_baden_civ.get_assigned_civs() == 10

    germany.get_construction().finish_construction(construction_line_moselland_mil)
    #46*0.24=10.8 civs need to be used on consumer goods
    assert germany.get_civs_used_on_consumer_goods() == 11
    assert germany.get_free_civs() == 0
    assert construction_line_moselland_mil.get_amount_of_constructions() == 3
    assert construction_line_moselland_mil.get_assigned_civs() == 15
    assert construction_line_baden_civ.get_assigned_civs() == 9

    assert germany.get_total_civs() == 35
    assert germany.get_total_mils() == 11




def create_germany(): 
    return setup_countries.create_simple_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def remove_building_slots(state): 
    state.total_construction_slots -= 3

def get_construction_line(country, number): 
    return country.construction.get_construction_line_list()[number]

def find_construction_line(construction_type, state, country): 
    return country.construction.find_construction_line(construction_type, state)

def move_priority_level(construction_line, new_priority_level, country): 
    country.construction.move_priority_level(construction_line, new_priority_level, country)

def remove_building_from_construction_line(construction_type, state, country): 
    country.construction.remove_building_from_construction_line(find_construction_line(construction_type, state, country))

def remove_construction_line(construction_type, state, country): 
    country.construction.delete_construction_line(find_construction_line(construction_type, state, country), country)

def get_construction_line_list(country): 
    return country.construction.get_construction_line_list()

def check_date(date_one, date_two): 
    return date_one.get_day() == date_two.get_day() and date_one.get_month() == date_two.get_month() and date_one.get_year() == date_two.get_year()

def set_construction_left(construction_line, amount): 
    construction_line.construction_cost = amount

def add_total_construction_slots(state, amount): 
    state.total_construction_slots += amount

def delete_factory(country, state, construction_type): 
    country.get_construction().delete_factory(construction_type, state)

def delete_all_factories_of_type(country, construction_type): 
    construction = country.get_construction()
    for state_name in country.get_states(): 
        state = country.states[state_name]
        while state.get_amount_of_building_type(construction_type) > 0: 
            construction.delete_factory(construction_type, state)

