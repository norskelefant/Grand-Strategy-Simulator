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

def test_werner_von_blomberg(germany, new_game):
    assert True == False

def test_werner_von_blomberg_without_fulfilling_not_having_completed_focus_reorganize_the_wehrmacht(germany, new_game):
    assert True == False

def test_erich_von_manstein(germany, new_game):
    assert True == False

def test_erich_von_manstein_without_fulfilling_political_power_cost(germany, new_game):
    assert True == False

def test_w_von_richthofen(germany, new_game):
    assert True == False

def test_w_von_richthofen_without_fulfilling_political_power_cost(germany, new_game):
    assert True == False

def test_walther_wever(germany, new_game):
    assert True == False

def test_walther_wever_without_fulfilling_political_power_cost(germany, new_game):
    assert True == False

def test_otto_ciliax(germany, new_game):
    assert True == False

def test_otto_ciliax_without_fulfilling_political_power_cost(germany, new_game):
    assert True == False

def test_heinz_guderian(germany, new_game):
    assert True == False

def test_heinz_guderian_without_fulfilling_having_completed_focus_adopt_new_panzer_doctrine(germany, new_game):
    assert True == False

def test_alfred_saalwächter(germany, new_game):
    assert True == False

def test_alfred_saalwächter_without_fulfilling_having_completed_focus_wolfpack_tactics(germany, new_game):
    assert True == False

def test_ernst_udet(germany, new_game):
    assert True == False

def test_ernst_udet_without_fulfilling_having_completed_focus_dive_bombers(germany, new_game):
    assert True == False

def test_cannot_have_more_than_one_theorist(germany, new_game): 
    assert True == False

def test_swapping_theorist(germany, new_game): 
    assert True == False

def test_another_country_cannot_hire_german_theorist(germany, new_game): 
    assert True == False






















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)