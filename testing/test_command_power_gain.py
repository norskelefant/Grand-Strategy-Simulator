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

def test_daily_command_power_gain_as_germany_for_one_day(germany, new_game): 
    #Given Germany

    #When a day passes
    new_game.pass_day()

    #Then Germany should have (0.4) * (1 - 28.5%) = 0.286 command power
    #Remember each war support percent drop below 50% give -1.9% command power gain
    assert germany.get_command_power() == pytest.approx(0.286)

def test_daily_command_power_gain_as_germany_for_100_days(germany, new_game): 
    #Given Germany

    #When 100 days pass
    for i in range(100): 
        new_game.pass_day()

    #Then Germany should have ((0.4) * (1 - 28.5%)) * 100 = 28.6 command power
    #Remember each war support percent drop below 50% give -1.9% command power gain
    assert germany.get_command_power() == pytest.approx(28.6)

def test_command_power_never_goes_above_80_by_default(germany, new_game): 
    #Given Germany

    #When 500 days pass
    for i in range(500): 
        new_game.pass_day()

    #Then Germany should have 80 command power, since it is the maximum
    assert germany.get_command_power() == 80

    #When another day passes
    new_game.pass_day()

    #Then Germany should still have 80 command power
    assert germany.get_command_power() == 80

def test_command_power_never_goes_above_limit_with_full_government(germany, new_game): 
    #Given Germany

    #When Germany hires different parts of government that gives extra room for command power
    germany.add_political_power(4000)
    assert germany.get_political_power() == 2000

    germany.complete_focus("Adopt_new_panzer_doctrine")

    germany.hire_chief_of_air_force("Albert_kesselring")
    germany.hire_chief_of_army("Ludwig_beck")
    germany.hire_chief_of_navy("Erich_raeder_con")
    germany.hire_high_commander("Erwin_rommel", 0)
    germany.hire_high_commander("Gerd_von_rundstedt", 1)
    germany.hire_high_commander("Gunther_lutjens", 2)

    #Then the command power limit should be 80+20+20+20+30+20+20 = 210
    assert germany.get_maximum_command_power() == 210

    #When 2000 days pass
    for i in range(2000): 
        new_game.pass_day()

    #Then Germany should have 210 command power
    assert germany.get_command_power() == 210


def test_command_power_limit_changes_when_command_power_is_full(germany, new_game): 
    #Given Germany

    #When 500 days pass
    for i in range(500): 
        new_game.pass_day()

    #Then Germany should have 80 command power, since it is the maximum
    assert germany.get_command_power() == 80

    #When another day passes
    new_game.pass_day()

    #Then Germany should still have 80 command power
    assert germany.get_command_power() == 80

    #When many parts of government is hired to increase command power maximum to 210
    germany.add_political_power(2000)

    germany.complete_focus("Adopt_new_panzer_doctrine")

    germany.hire_chief_of_air_force("Albert_kesselring")
    germany.hire_chief_of_army("Ludwig_beck")
    germany.hire_chief_of_navy("Erich_raeder_con")
    germany.hire_high_commander("Erwin_rommel", 0)
    germany.hire_high_commander("Gerd_von_rundstedt", 1)
    germany.hire_high_commander("Gunther_lutjens", 2)

    #and a day passes
    new_game.pass_day()

    #Then Germany should have 80 + 0.286 command power
    assert germany.get_command_power() == 80.286

    #When 2000 more days pass
    for i in range(2000): 
        new_game.pass_day()

    #Then Germany should have 210 command power
    assert germany.get_command_power() == 210

def test_command_power_maximum_when_replacing_advisor(germany, new_game): 
    #Given Germany

    #When Germany hires Erwin Rommel
    germany.add_political_power(2000)

    germany.complete_focus("Adopt_new_panzer_doctrine")

    germany.hire_high_commander("Erwin_rommel", 0)

    #Then the max command power is 110
    assert germany.get_maximum_command_power() == 110

    #When Erwin Rommel is replaced with Gerd von Rundstedt
    germany.hire_high_commander("Gerd_von_rundstedt", 0)

    #Then the max command power is 100
    assert germany.get_maximum_command_power() == 100

def test_command_power_when_maximum_command_power_is_reduced_by_replacing_advisor(germany, new_game): 
    #Given Germany

    #When Germany hires Erwin Rommel and gets 110 command power
    germany.add_political_power(2000)

    germany.complete_focus("Adopt_new_panzer_doctrine")

    germany.hire_high_commander("Erwin_rommel", 0)

    germany.add_command_power(110)

    #Then the max command power is 110
    assert germany.get_maximum_command_power() == 110
    assert germany.get_command_power() == 110

    #When Erwin Rommel is replaced with Gerd von Rundstedt
    germany.hire_high_commander("Gerd_von_rundstedt", 0)

    #Then the max command power is 100 and the command power is reduced to 80
    assert germany.get_maximum_command_power() == 100
    assert germany.get_command_power() == 80

def test_command_power_never_goes_below_0(germany, new_game): 
    #Given Germany

    #When -50 command power is given
    germany.add_command_power(-50)

    #Then Germany should have 0 command power
    assert germany.get_command_power() == 0




































def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)