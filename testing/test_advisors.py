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

#def test_hjalmar_schact(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_consumer_goods() == 0.24
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired
    germany.hire_advisor("Hjalmar_schacht", 0)

    #Then the full added bonuses should be the following
    assert germany.get_consumer_goods() == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.20













































def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])