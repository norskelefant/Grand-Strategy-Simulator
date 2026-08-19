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

def test_daily_political_power_gain_as_germany_for_one_day(germany, new_game): 
    #Given Germany

    #When one day passes
    new_game.pass_day()

    #Then Germany should have (2) * (1 + 16.2%) = 2.324 pp 
    assert germany.get_political_power() == 2.324

def test_daily_political_power_gain_as_germany_for_100_days(germany, new_game): 
    #Given Germany

    #When 100 days pass
    for i in range(100): 
        new_game.pass_day()

    #Then Germany should have ((2) * (1 + 16.2%)) * 100 = 232.4 pp
    assert germany.get_political_power() == pytest.approx(232.4)

def test_daily_political_power_gain_as_germany_with_advisors(germany, new_game): 
    #Given Germany
    
    #When parts of goverment is hired that give extra political power bonuses and a day passes
    germany.add_political_power(450)

    germany.complete_focus("Start_the_proletarian_revolution")
    germany.complete_focus("Monarchist_sentiment")
    germany.complete_focus("Legacy_of_the_spartacus_league")
    germany.activate_event("Ernst_thalmann_has_been_freed_from_prison")


    germany.hire_advisor("Walter_ulbricht_a", 0)
    germany.hire_advisor("Otto_ruhle", 1)
    germany.hire_advisor("Ernst_thalmann_a", 2)

    germany.switch_leader("Fritz_todt")

    new_game.pass_day()

    #Then Germany should have (2 + 0.25) * (1 + 31.2%) = 2.952 pp
    assert germany.get_political_power() == pytest.approx(2.952)

def test_political_power_can_max_be_2000(germany, new_game): 
    #Given Germany

    #When 1000 days pass
    for i in range(1000): 
        new_game.pass_day()

    #Then Germany should have 2000 political power
    assert germany.get_political_power() == 2000

    #When another day passes
    new_game.pass_day()

    #Then Germany should still have 2000 political power
    assert germany.get_political_power() == 2000

def test_political_power_can_min_be_minus_500(germany, new_game): 
    #Given Germany

    #When -600 political power is given to Germany
    germany.add_political_power(-600)

    #Then Germany should have -500 political power
    assert germany.get_political_power() == -500

    #When -10 political power is given to Germany
    germany.add_political_power(-10)

    #Then Germany should still have -500 political power
    assert germany.get_political_power() == -500

def test_political_power_gain_while_doing_a_focus(germany, new_game): 
    assert True == False

















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)