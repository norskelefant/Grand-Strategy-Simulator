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
    assert True == False

def test_karl_dönitz(germany, new_game):
    assert True == False

def test_rolf_carls(germany, new_game):
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

def create_custom_country(): 
    return custom_country.create_custom_country()
