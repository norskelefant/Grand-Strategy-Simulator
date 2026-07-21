import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, trade_laws

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_germany_has_limited_exports_by_default(germany, new_game): 
    assert True == False

def test_can_switch_to_free_trade(germany, new_game): 
    assert True == False

def test_can_switch_to_export_focus(germany, new_game): 
    assert True == False

def test_can_switch_to_limited_exports_if_requirements_are_fulfilled(germany, new_game): 
    assert True == False

def test_can_switch_to_closed_economy_if_requirements_are_fulfilled(germany, new_game): 
    assert True == False

def test_cannot_switch_trade_law_if_not_enough_political_power(germany, new_game): 
    assert True == False

def test_cannot_switch_to_limited_exports_if_requirements_are_not_fulfilled(germany, new_game): 
    assert True == False

def test_cannot_switch_to_free_trade_if_requirements_are_not_fulfilled(germany, new_game):
    assert True == False


























def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(): 

    custom_state = state.State("Custom_state", 50, 15, 15, 10, 3, True, None)

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
                       modifiers=[], 
                       base_stability=70, 
                       economy_law=modifier.Modifier("Partial_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}), 
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
                       trade_law=None, 
                       conscription_law=None, 
                       advisors=[], 
                       industrial_concern=None, 
                       theorist=None, 
                       chief_of_army=None, 
                       chief_of_navy=None, 
                       chief_of_air_force=None, 
                       high_commanders=[])
    
    custom_country.states["Custom_state"].set_country(custom_country)

    return custom_country