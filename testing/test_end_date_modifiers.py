import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_modifier_removed_after_end_date(germany, new_game): 
    #Given a testing country
    testing_country = create_custom_country(new_game)

    assert len(testing_country.get_modifiers()) == 2
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.35
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10

    #Some things are left alone
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10

    #When 59 days pass
    for i in range(59): 
        new_game.pass_day()

    #Then the first testing modifier has to be removed
    assert len(testing_country.get_modifiers()) == 1
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == pytest.approx(0.25)
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0

    #Some things are left alone
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10

    #When 1240 more days pass
    for i in range(1240): 
        new_game.pass_day()

    #Then nothing should happen
    assert len(testing_country.get_modifiers()) == 1
    #This has a small floating point error
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == pytest.approx(0.25)
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0

    #Some things are left alone
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10

    #When 1 more day passes
    for i in range(1): 
        new_game.pass_day()

    #Then the second testing_country modifier should be removed
    assert len(testing_country.get_modifiers()) == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
























def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 

    custom_state = state.State("Custom_state", 50, 15, 15, 10, 3, True, None)

    partial_mobilization = modifier.Modifier("Partial_mobilization", "Partial Mobilization", 0, modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, True)

    custom_country = country.Country(name="Custom_country", 
                       states={"Custom_state": custom_state},
                       tiles=None, 
                       resources=None, 
                       free_civs=15, 
                       civs_used_on_consumer_goods=0, 
                       free_mils=15, 
                       free_dockyards=10, 
                       construction=construction.Construction(), 
                       base_ic=4, 
                       base_stability=70, 
                       economy_law=partial_mobilization, 
                       base_war_support=30, 
                       political_power=0, 
                       population=0, 
                       fuel=0, 
                       command_power=0, 
                       convoys=0, 
                       army_exp=0, 
                       navy_exp=0, 
                       air_exp=0, 
                       ideology=ideologies.Ideologies.FASCIST, 
                       democratic_support=35, 
                       non_aligned_support=15, 
                       communist_support=10, 
                       fascist_support=40, 
                       at_war=False, 
                       countries_at_war_with=[], 
                       research_slots=4, 
                       has_researched=[], 
                       can_research=[],
                       trade_law=None, 
                       conscription_law=None, 
                       advisors=[], 
                       possible_advisors=[],
                       industrial_concern=None, 
                       possible_industrial_concerns=[],
                       theorist=None, 
                       possible_theorists=[],
                       chief_of_army=None, 
                       possible_chiefs_of_army=[],
                       chief_of_navy=None, 
                       possible_chiefs_of_navy=[],
                       chief_of_air_force=None, 
                       possible_chiefs_of_air_force=[],
                       high_commanders=[], 
                       possible_high_commanders=[],
                       focus_tree=[], 
                       focuses_done=[], 
                       focuses_that_can_be_done=[], 
                       national_spirits=[], 
                       modifiers=[], 
                       full_added_bonuses={})
    
    custom_country.states["Custom_state"].set_country(custom_country)

    custom_country.full_added_bonuses = custom_country.create_default_bonuses_map()

    custom_country.add_to_full_added_bonuses(partial_mobilization)

    testing_modifier_1 = modifier.Modifier("Testing_modifier_1", "Testing modifier 1", 0, modifier_classes.Modifier_classes.BASE, date.Date(3, 1, 1936), {modifier_types.Modifier_types.STABILITY: 0.10, modifier_types.Modifier_types.WAR_SUPPORT: 0.10, modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.10}, True)

    testing_modifier_2 = modifier.Modifier("Testing_modifier_2", "Testing modifier 2", 0, modifier_classes.Modifier_classes.BASE, date.Date(25, 7, 1939), {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.25}, True)

    custom_country.modifiers.append(testing_modifier_1)
    custom_country.add_to_full_added_bonuses(testing_modifier_1)

    custom_country.modifiers.append(testing_modifier_2)
    custom_country.add_to_full_added_bonuses(testing_modifier_2)

    game.countries.append(custom_country)

    return custom_country