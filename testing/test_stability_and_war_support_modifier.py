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

def test_stability_modifier_at_50_percent(germany, new_game): 
    assert True == False

def test_stability_modifier_at_70_percent(germany, new_game): 
    assert True == False

def test_stability_modifier_at_71_percent(germany, new_game): 
    assert True == False

def test_stability_modifier_at_20_percent(germany, new_game): 
    assert True == False

def test_stability_modifier_at_21_percent(germany, new_game): 
    assert True == False

def test_stability_modifier_at_100_percent(germany, new_game): 
    assert True == False

def test_stability_modifier_at_0_percent(germany, new_game): 
    assert True == False

def test_stability_increased_from_60_to_70_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_decreased_from_84_to_62_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_increased_from_10_to_22_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_decreased_from_49_to_40_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_increased_from_50_to_57_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_decreased_from_50_to_43_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_increased_from_40_to_60_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_decreased_from_60_to_40_changes_modifier(germany, new_game): 
    assert True == False

def test_stability_bonuses_do_not_go_under_0_percent(germany, new_game): 
    assert True == False

def test_stability_bonuses_do_not_go_over_100_percent(germany, new_game): 
    assert True == False


def test_war_support_modifier_at_50_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_80_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_81_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_26_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_27_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_100_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_0_percent(germany, new_game): 
    assert True == False

def test_war_support_increased_from_53_to_96_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_73_to_70_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_increased_from_7_to_31_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_43_to_30_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_increased_from_50_to_60_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_50_to_25_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_increased_from_40_to_60_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_60_to_40_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_bonuses_do_not_go_under_0_percent(germany, new_game): 
    assert True == False

def test_war_support_bonuses_do_not_go_over_100_percent(germany, new_game): 
    assert True == False


def test_stability_and_war_support_changes_at_the_same_time_changes_modifier(germany, new_game): 
    assert True == False


































def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])