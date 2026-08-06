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

def test_gerd_von_rundstedt(germany, new_game):
    assert True == False

def test_werner_von_fritsch(germany, new_game):
    assert True == False

def test_günther_lütjens(germany, new_game):
    assert True == False

def test_ferdinand_schörner(germany, new_game):
    assert True == False

def test_erich_bey(germany, new_game):
    assert True == False

def test_viktor_schütze(germany, new_game):
    assert True == False

def test_josef_kammhuber(germany, new_game):
    assert True == False

def test_erwin_rommel(germany, new_game):
    assert True == False

def test_kurt_student(germany, new_game):
    assert True == False

def test_hugo_sperrle(germany, new_game):
    assert True == False

def test_erhard_milch(germany, new_game):
    assert True == False

def test_robert_knauss(germany, new_game):
    assert True == False

def test_alfred_becker(germany, new_game):
    assert True == False

def test_walter_dornberger(germany, new_game):
    assert True == False

def test_having_three_high_commanders(germany, new_game): 
    assert True == False

def test_replacing_a_high_commander(germany, new_game): 
    assert True == False

def test_one_cannot_hire_high_commanders_with_illegal_slot(germany, new_game): 
    assert True == False

def test_another_country_cannot_hire_german_high_commander(germany, new_game): 
    assert True == False





















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(): 
    return custom_country.create_custom_country()