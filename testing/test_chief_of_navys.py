import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, custom_country

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_erich_raeder(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erich Raeder is hired when Erich is not country leader
    germany.add_political_power(100)

    germany.hire_chief_of_navy("Erich_raeder_con")

    assert germany.get_political_power() == 0

    #Then Erich Raeder has the following bonuses
    erich_raeder = germany.find_modifier_by_id("Erich_raeder_con")

    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.30
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.SCREEN_ATTACK] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.SCREEN_DEFENSE] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Erich Raeder is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_DEFENSE] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_erich_raeder_without_fulfilling_erich_not_being_country_leader(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erich Raeder is hired when Erich is country leader
    germany.switch_leader("Erich_raeder_l")
    germany.add_political_power(100)

    germany.hire_chief_of_navy("Erich_raeder_con")

    assert germany.get_political_power() == 100

    #Then Erich Raeder has the following bonuses
    erich_raeder = germany.find_modifier_by_id("Erich_raeder_con")

    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.30
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.SCREEN_ATTACK] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.SCREEN_DEFENSE] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Erich Raeder is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    
def test_karl_dönitz(germany, new_game):
    assert True == False

def test_karl_dönitz_without_fulfilling_having_completed_focus_trade_interdiction(germany, new_game):
    assert True == False

def test_rolf_carls(germany, new_game):
    assert True == False

def test_rolf_carls_without_fulfilling_having_completed_focus_reestablish_the_seekriegsleitung(germany, new_game):
    assert True == False

def test_cannot_have_more_than_one_chief_of_navy(germany, new_game): 
    assert True == False

def test_swapping_chief_of_army(germany, new_game): 
    assert True == False

def test_another_country_cannot_hire_german_chief_of_navy(germany, new_game): 
    assert True == False






















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)
