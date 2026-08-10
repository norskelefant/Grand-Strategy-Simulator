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
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Werner von Blomberg is hired when focus Reorganize the wehrmacht has not been completed
    germany.add_political_power(150)

    germany.hire_theorist("Werner_von_blomberg")

    assert germany.get_political_power() == 0

    #Then Werner von Blomberg has the following bonuses
    werner_von_blomberg = germany.find_modifier_by_id("Werner_von_blomberg")

    assert werner_von_blomberg.get_modifier_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Werner von Blomberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.15

def test_werner_von_blomberg_without_fulfilling_not_having_completed_focus_reorganize_the_wehrmacht(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Werner von Blomberg is hired when focus Reorganize the wehrmacht has been completed
    germany.complete_focus("Reorganize_the_wehrmacht")
    germany.add_political_power(150)

    germany.hire_theorist("Werner_von_blomberg")

    assert germany.get_political_power() == 150

    #Then Werner von Blomberg has the following bonuses
    werner_von_blomberg = germany.find_modifier_by_id("Werner_von_blomberg")

    assert werner_von_blomberg.get_modifier_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.15

    #but Germany has the following bonuses because Werner von Blomberg is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0

def test_erich_von_manstein(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Erich von Manstein is hired
    germany.add_political_power(150)

    germany.hire_theorist("Erich_von_manstein")

    assert germany.get_political_power() == 0

    #Then Erich von Manstein has the following bonuses
    erich_von_manstein = germany.find_modifier_by_id("Erich_von_manstein")

    assert erich_von_manstein.get_modifier_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Erich von Manstein is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

def test_erich_von_manstein_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Erich von Manstein is hired when not having enough political power
    germany.add_political_power(0)

    germany.hire_theorist("Erich_von_manstein")

    assert germany.get_political_power() == 0

    #Then Erich von Manstein has the following bonuses
    erich_von_manstein = germany.find_modifier_by_id("Erich_von_manstein")

    assert erich_von_manstein.get_modifier_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

    #but Germany has the following bonuses because Erich von Manstein is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

def test_w_von_richthofen(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN] == 0.0

    #When W. von Richthofen is hired
    germany.add_political_power(150)

    germany.hire_theorist("W_von_richthofen")

    assert germany.get_political_power() == 0

    #Then W. von Richthofen has the following bonuses
    w_von_richthofen = germany.find_modifier_by_id("W_von_richthofen")

    assert w_von_richthofen.get_modifier_bonuses()[modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because W. von Richthofen is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN] == 0.15

def test_w_von_richthofen_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN] == 0.0

    #When W. von Richthofen is hired without enough political power
    germany.add_political_power(0)

    germany.hire_theorist("W_von_richthofen")

    assert germany.get_political_power() == 0

    #Then W. von Richthofen has the following bonuses
    w_von_richthofen = germany.find_modifier_by_id("W_von_richthofen")

    assert w_von_richthofen.get_modifier_bonuses()[modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN] == 0.15

    #but Germany has the following bonuses because W. von Richthofen is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN] == 0.0

def test_walther_wever(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == 0.0

    #When Walther Wever is hired
    germany.add_political_power(100)

    germany.hire_theorist("Walther_wever")

    assert germany.get_political_power() == 0

    #Then Walther Wever has the following bonuses
    walther_wever = germany.find_modifier_by_id("Walther_wever")

    assert walther_wever.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == -0.10

    #and Germany has the following bonuses because Walther Wever is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == -0.10

def test_walther_wever_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == 0.0

    #When Walther Wever is hired without enough political power
    germany.add_political_power(99)

    germany.hire_theorist("Walther_wever")

    assert germany.get_political_power() == 99

    #Then Walther Wever has the following bonuses
    walther_wever = germany.find_modifier_by_id("Walther_wever")

    assert walther_wever.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == -0.10

    #but Germany has the following bonuses because Walther Wever is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == 0.0

def test_otto_ciliax(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_DOCTRINE_COST] == 0.0

    #When Otto Ciliax is hired
    germany.add_political_power(100)

    germany.hire_theorist("Otto_ciliax")

    assert germany.get_political_power() == 0

    #Then Otto Ciliax has the following bonuses
    otto_ciliax = germany.find_modifier_by_id("Otto_ciliax")

    assert otto_ciliax.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_DOCTRINE_COST] == -0.10

    #and Germany has the following bonuses because Otto Ciliax is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_DOCTRINE_COST] == -0.10

def test_otto_ciliax_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_DOCTRINE_COST] == 0.0

    #When Otto Ciliax is hired without enough political power
    germany.add_political_power(99)

    germany.hire_theorist("Otto_ciliax")

    assert germany.get_political_power() == 99

    #Then Otto Ciliax has the following bonuses
    otto_ciliax = germany.find_modifier_by_id("Otto_ciliax")

    assert otto_ciliax.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_DOCTRINE_COST] == -0.10

    #but Germany has the following bonuses because Otto Ciliax is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_DOCTRINE_COST] == 0.0

def test_heinz_guderian(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Heinz Guderian is hired and focus Adopt new panzer doctrine has been completed
    germany.complete_focus("Adopt_new_panzer_doctrine")
    germany.add_political_power(200)

    germany.hire_theorist("Heinz_guderian")

    assert germany.get_political_power() == 0

    #Then Heinz Guderian has the following bonuses
    heinz_guderian = germany.find_modifier_by_id("Heinz_guderian")

    assert heinz_guderian.get_modifier_bonuses()[modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED] == 0.10
    assert heinz_guderian.get_modifier_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Heinz Guderian is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

def test_heinz_guderian_without_fulfilling_having_completed_focus_adopt_new_panzer_doctrine(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Heinz Guderian is hired and focus Adopt new panzer doctrine has been not completed
    germany.add_political_power(200)

    germany.hire_theorist("Heinz_guderian")

    assert germany.get_political_power() == 200

    #Then Heinz Guderian has the following bonuses
    heinz_guderian = germany.find_modifier_by_id("Heinz_guderian")

    assert heinz_guderian.get_modifier_bonuses()[modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED] == 0.10
    assert heinz_guderian.get_modifier_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

    #but Germany has the following bonuses because Heinz Guderian is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

def test_alfred_saalwachter(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Alfred Saalwächter is hired and focus Wolfpack tactics has been completed
    germany.complete_focus("Wolfpack_tactics")
    germany.add_political_power(150)

    germany.hire_theorist("Alfred_saalwachter")

    assert germany.get_political_power() == 0

    #Then Alfred Saalwächter has the following bonuses
    alfred_saalwachter = germany.find_modifier_by_id("Alfred_saalwachter")

    assert alfred_saalwachter.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Alfred Saalwächter is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN] == 0.15

def test_alfred_saalwächter_without_fulfilling_having_completed_focus_wolfpack_tactics(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Alfred Saalwächter is hired and focus Wolfpack tactics has been not completed
    germany.add_political_power(150)

    germany.hire_theorist("Alfred_saalwachter")

    assert germany.get_political_power() == 150

    #Then Alfred Saalwächter has the following bonuses
    alfred_saalwachter = germany.find_modifier_by_id("Alfred_saalwachter")

    assert alfred_saalwachter.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN] == 0.15

    #but Germany has the following bonuses because Alfred Saalwächter is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN] == 0.0

def test_ernst_udet(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == 0.0

    #When Ernst Udet is hired and focus Dive bombers has been completed
    germany.complete_focus("Dive_bombers")
    germany.add_political_power(100)

    germany.hire_theorist("Ernst_udet")

    assert germany.get_political_power() == 0

    #Then Ernst Udet has the following bonuses
    ernst_udet = germany.find_modifier_by_id("Ernst_udet")

    assert ernst_udet.get_modifier_bonuses()[modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK] == 0.10
    assert ernst_udet.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == -0.10

    #and Germany has the following bonuses because Ernst Udet is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == -0.10

def test_ernst_udet_without_fulfilling_having_completed_focus_dive_bombers(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == 0.0

    #When Ernst Udet is hired and focus Dive bombers has been not completed
    germany.add_political_power(100)

    germany.hire_theorist("Ernst_udet")

    assert germany.get_political_power() == 100

    #Then Ernst Udet has the following bonuses
    ernst_udet = germany.find_modifier_by_id("Ernst_udet")

    assert ernst_udet.get_modifier_bonuses()[modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK] == 0.10
    assert ernst_udet.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == -0.10

    #but Germany has the following bonuses because Ernst Udet is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_DOCTRINE_COST] == 0.0

def test_cannot_have_more_than_one_theorist(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Werner von Blomberg is hired
    germany.add_political_power(300)

    germany.hire_theorist("Werner_von_blomberg")

    assert germany.get_political_power() == 150

    #Then Werner von Blomberg has the following bonuses
    werner_von_blomberg = germany.find_modifier_by_id("Werner_von_blomberg")

    assert werner_von_blomberg.get_modifier_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Werner von Blomberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #Then hiring another theorist
    germany.hire_theorist("Erich_von_manstein")

    assert germany.get_political_power() == 0

    #Then Erich von Manstein has the following bonuses
    erich_von_manstein = germany.find_modifier_by_id("Erich_von_manstein")

    assert erich_von_manstein.get_modifier_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Erich von Manstein is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

    #and the length of theorists hired is only 1
    theorist_list = [germany.get_theorist()]
    assert len(theorist_list) == 1

def test_swapping_theorist(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #When Werner von Blomberg is hired
    germany.add_political_power(300)

    germany.hire_theorist("Werner_von_blomberg")

    assert germany.get_political_power() == 150

    #Then Werner von Blomberg has the following bonuses
    werner_von_blomberg = germany.find_modifier_by_id("Werner_von_blomberg")

    assert werner_von_blomberg.get_modifier_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Werner von Blomberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.0

    #Then hiring another theorist
    germany.hire_theorist("Erich_von_manstein")

    assert germany.get_political_power() == 0

    #Then Erich von Manstein has the following bonuses
    erich_von_manstein = germany.find_modifier_by_id("Erich_von_manstein")

    assert erich_von_manstein.get_modifier_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

    #and Germany has the following bonuses because Werner von Blomberg is swapped with Erich von Manstein
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN] == 0.15

def test_another_country_cannot_hire_german_theorist(germany, new_game): 
    #Given a testing country that is not Germany
    testing_country = create_custom_country(new_game)

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN] == 0.0

    #When testing country hires Werner von Blomberg
    testing_country.add_political_power(150)

    testing_country.hire_theorist("Werner_von_blomberg")

    #Then Werner von Blomberg should not be hired
    assert testing_country.get_political_power() == 150

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0























def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)