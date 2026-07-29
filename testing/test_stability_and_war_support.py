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

def test_stability_caps_at_100_percent(germany, new_game): 
    #Given default germany start
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_base_stability() == 0.70

    #When base stability increases by 35 percent
    germany.add_base_stability(0.35)

    #Then the base and full stability should both be 1.0
    assert germany.get_full_stability() == 1.0
    assert germany.get_base_stability() == 1.0

    #When some base stability is removed
    germany.add_base_stability(-0.05)

    #Then full stability should still be 1
    assert germany.get_full_stability() == 1.0
    assert germany.get_base_stability() == 0.95

    #When base stability falls to 0.88
    germany.add_base_stability(-0.07)

    #Then full stability should be 0.99
    assert germany.get_full_stability() == pytest.approx(0.99)
    assert germany.get_base_stability() == pytest.approx(0.88)

def test_war_support_caps_at_100_percent(germany, new_game): 
    #Given default germany start
    assert germany.get_full_war_support() == 0.40
    assert germany.get_base_war_support() == 0.30

    #When base war support increases by 75 percent
    germany.add_base_war_support(0.75)

    #Then the base and full war support should both be 1.0
    assert germany.get_full_war_support() == 1.0
    assert germany.get_base_war_support() == 1.0

    #When some base war support is removed
    germany.add_base_war_support(-0.05)

    #Then full war support should still be 1
    assert germany.get_full_war_support() == 1.0
    assert germany.get_base_war_support() == 0.95

    #When base war support falls to 0.89
    germany.add_base_war_support(-0.06)

    #Then full war support should be 0.99
    assert germany.get_full_war_support() == pytest.approx(0.99)
    assert germany.get_base_war_support() == pytest.approx(0.89)





































def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])