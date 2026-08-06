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

def test_modifier_removed_after_end_date(germany, new_game): 
    #Given a testing country
    testing_country = create_custom_country(new_game)

    print(35.0-10.0)
    print(0.35-0.10)

    assert len(testing_country.get_modifiers()) == 2
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.35
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10

    #Some things are left alone
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
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
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
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
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
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
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10

def test_multiple_countries_modifiers_can_be_removed(germany, new_game):
    #Given Germany with a new modifier
    testing_country = create_custom_country(new_game)

    germany_testing_modifier = modifier.Modifier("germany_testing_modifier", "Germany testing modifier", 0, modifier_classes.Modifier_classes.BASE, date.Date(25, 7, 1939), {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.15, 
    modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: 0.10,                                                                                         modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, True)

    germany.modifiers.append(germany_testing_modifier)
    germany.add_to_full_added_bonuses(germany_testing_modifier)

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.35
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10

    #Some things are left alone
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10

    #When 59 days pass
    for i in range(59): 
        new_game.pass_day()

    #Then the first testing modifier has to be removed
    assert len(testing_country.get_modifiers()) == 1
    assert len(germany.get_modifiers()) == 4
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == pytest.approx(0.25)
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)

    #Some things are left alone
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10

    #When 1240 more days pass
    for i in range(1240): 
        new_game.pass_day()

    #Then nothing should happen
    assert len(testing_country.get_modifiers()) == 1
    assert len(germany.get_modifiers()) == 4
    #This has a small floating point error
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == pytest.approx(0.25)
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)

    #Some things are left alone
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10

    #When 1 more day passes
    for i in range(1): 
        new_game.pass_day()

    #Then the second testing_country modifier should be removed
    assert len(testing_country.get_modifiers()) == 0
    assert len(germany.get_modifiers()) == 3
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == pytest.approx(0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.20)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10





















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 

    partial_mobilization = modifier.Modifier("Partial_mobilization", "Partial Mobilization", 0, modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, True)

    testing_country = custom_country.create_custom_country(game)

    testing_country.full_added_bonuses = testing_country.create_default_bonuses_map()

    testing_country.add_to_full_added_bonuses(partial_mobilization)

    testing_modifier_1 = modifier.Modifier("Testing_modifier_1", "Testing modifier 1", 0, modifier_classes.Modifier_classes.BASE, date.Date(3, 1, 1936), {modifier_types.Modifier_types.STABILITY: 0.10, modifier_types.Modifier_types.WAR_SUPPORT: 0.10, modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.10}, True)

    testing_modifier_2 = modifier.Modifier("Testing_modifier_2", "Testing modifier 2", 0, modifier_classes.Modifier_classes.BASE, date.Date(25, 7, 1939), {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.25}, True)

    testing_country.modifiers.append(testing_modifier_1)
    testing_country.add_to_full_added_bonuses(testing_modifier_1)

    testing_country.modifiers.append(testing_modifier_2)
    testing_country.add_to_full_added_bonuses(testing_modifier_2)

    #game.countries.append(testing_country)

    return testing_country