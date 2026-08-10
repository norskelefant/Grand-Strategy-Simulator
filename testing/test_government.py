
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

def test_having_full_government(germany, new_game): 
    #Given a normal Germany Game

    #When Germany hires many different parts of government
    germany.complete_focus("Formalize_the_intelligence_wing")
    germany.add_political_power(2000)

    germany.hire_advisor("Reinhard_heydrich", 0)
    germany.hire_advisor("Wilhelm_zaisser", 1)
    germany.hire_advisor("Hanns_kerrl", 2)
    germany.hire_industrial_concern("IG_farben")
    germany.hire_theorist("Erich_von_manstein")
    germany.hire_chief_of_army("Ludwig_beck")
    germany.hire_chief_of_navy("Erich_raeder_con")
    germany.hire_chief_of_air_force("Albert_kesselring")
    germany.hire_high_commander("Erich_bey", 0)
    germany.hire_high_commander("Gerd_von_rundstedt", 1)
    germany.hire_high_commander("Gunther_lutjens", 2)

    print(germany.get_theorist().id)
    print(germany.get_industrial_concern().id)
    print(germany.get_chief_of_army().id)
    print(germany.get_chief_of_navy().id)
    print(germany.get_chief_of_air_force().id)
    print(germany.get_high_commanders()[0].id)
    print(germany.get_high_commanders()[1].id)
    print(germany.get_high_commanders()[2].id)


    assert germany.get_political_power() == 650

    #The Germany should have the following bonuses because of all the hirings
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESITANCE_GROWTH_SPEED] == -0.07
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 2
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.152
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.252
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == pytest.approx(-0.015)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0020
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SCREEN_DEFENSE] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 120



































def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])