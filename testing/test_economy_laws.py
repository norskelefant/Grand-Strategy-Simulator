import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_partial_mobilization_is_default_economy_law_for_germany(germany, new_game): 
    #Given Germany start

    #When asking for the economy law of germany
    economy_law = germany.get_economy_law()

    #Then the economy law should be partial mobilization
    assert economy_law.get_name() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10

def test_can_switch_economy_law_to_civilian_economy_if_prerequisites_are_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the economy law to civilian economy
    germany.switch_economy_law(economy_laws.Economy_laws.CIVILIAN_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should be Civilian economy
    assert economy_law.get_name() == "Civilian_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.35
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.30

def test_can_switch_economy_law_to_early_mobilization(germany, new_game): 
    #Given Germany start

    #When switching the economy law to civilian economy
    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be Civilian economy
    assert economy_law.get_name() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10

def test_can_switch_economy_law_to_war_economy(germany, new_game): 
    #Given Germany start

    #When switching the economy law to civilian economy
    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should be Civilian economy
    assert economy_law.get_name() == "War_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.20

def test_can_switch_economy_law_to_total_mobilization(germany, new_game): 
    #Given Germany start

    #When switching the economy law to civilian economy
    germany.switch_economy_law(economy_laws.Economy_laws.TOTAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be Civilian economy
    assert economy_law.get_name() == "Total_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.15
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.30








def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])


