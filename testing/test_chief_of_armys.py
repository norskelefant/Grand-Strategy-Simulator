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

def test_ludwig_beck(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Ludwig Beck is hired
    germany.add_political_power(100)

    germany.hire_chief_of_army("Ludwig_beck")

    assert germany.get_political_power() == 0

    #Then Ludwig Beck has the following bonuses
    ludwig_beck = germany.find_modifier_by_id("Ludwig_beck")

    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Ludwig Beck is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_ludwig_beck_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Ludwig Beck is hired without enough political power
    germany.add_political_power(50)

    germany.hire_chief_of_army("Ludwig_beck")

    assert germany.get_political_power() == 50

    #Then Ludwig Beck has the following bonuses
    ludwig_beck = germany.find_modifier_by_id("Ludwig_beck")

    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Ludwig Beck is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_wilhelm_keitel(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Wilhelm Keitel is hired when Germany is fascist
    germany.add_political_power(100)

    germany.hire_chief_of_army("Wilhelm_keitel")

    assert germany.get_political_power() == 0

    #Then Wilhelm Keitel has the following bonuses
    wilhelm_keitel = germany.find_modifier_by_id("Wilhelm_keitel")

    assert wilhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert wilhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == -0.10
    assert wilhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Wilhelm Keitel is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_wilhelm_keitel_without_fulfilling_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Wilhelm Keitel is hired when Germany is not fascist
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(100)

    germany.hire_chief_of_army("Wilhelm_keitel")

    assert germany.get_political_power() == 100

    #Then Wilhelm Keitel has the following bonuses
    wilhelm_keitel = germany.find_modifier_by_id("Wilhelm_keitel")

    assert wilhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert wilhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == -0.10
    assert wilhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Wilhelm Keitel is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_werner_von_fritsch(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Werner von Fritsch is hired when Werner von Fritsch is not already hired elsewhere and Germany has completed focus Prussian artillery doctrine
    germany.complete_focus("Prussian_artillery_doctrine")
    germany.add_political_power(100)

    germany.hire_chief_of_army("Werner_von_fritsch_coa")

    assert germany.get_political_power() == 0

    #Then Werner von Fritsch has the following bonuses
    werner_von_fritsch = germany.find_modifier_by_id("Werner_von_fritsch_coa")

    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.15
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.10
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.10
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Werner von Fritsch is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_werner_von_fritsch_without_fulfilling_werner_being_hired_elsewhere(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Werner von Fritsch is hired when Werner von Fritsch is already hired elsewhere and Germany has completed focus Prussian artillery doctrine
    germany.add_political_power(200)
    germany.hire_high_commander("Werner_von_fritsch_hc", 0)
    germany.complete_focus("Prussian_artillery_doctrine")

    assert germany.get_political_power() == 100

    germany.hire_chief_of_army("Werner_von_fritsch_coa")

    assert germany.get_political_power() == 100

    #Then Werner von Fritsch has the following bonuses
    werner_von_fritsch_coa = germany.find_modifier_by_id("Werner_von_fritsch_coa")

    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.15
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.10
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.10
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Werner von Fritsch is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.0
    #High commander Werner gives 20 max command power increase
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20.0

def test_werner_von_fritsch_without_fulfilling_having_completed_focus_prussian_artillery_doctrine(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Werner von Fritsch is hired when Werner von Fritsch is not already hired elsewhere and Germany has not completed focus Prussian artillery doctrine
    germany.add_political_power(100)

    germany.hire_chief_of_army("Werner_von_fritsch_coa")

    assert germany.get_political_power() == 100

    #Then Werner von Fritsch has the following bonuses
    werner_von_fritsch_coa = germany.find_modifier_by_id("Werner_von_fritsch_coa")

    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.15
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.10
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.10
    assert werner_von_fritsch_coa.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Werner von Fritsch is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARITLLERY_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARTILLERY_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_franz_halder(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Franz Halder is hired when Germany has completed focus Instill auftragstaktik
    germany.complete_focus("Instill_auftragstaktik")
    germany.add_political_power(100)

    germany.hire_chief_of_army("Franz_halder")

    assert germany.get_political_power() == 0

    #Then Franz Halder has the following bonuses
    franz_halder = germany.find_modifier_by_id("Franz_halder")

    assert franz_halder.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert franz_halder.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.10
    assert franz_halder.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Franz Halder is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_franz_halder_without_fulfilling_having_completed_focus_instill_auftragstaktik(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Franz Halder is hired when Germany has not completed focus Instill auftragstaktik
    germany.add_political_power(100)

    germany.hire_chief_of_army("Franz_halder")

    assert germany.get_political_power() == 100

    #Then Franz Halder has the following bonuses
    franz_halder = germany.find_modifier_by_id("Franz_halder")

    assert franz_halder.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert franz_halder.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.10
    assert franz_halder.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Franz Halder is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_w_von_brauchitsch(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When W. von Brauchitsch is hired when Germany has completed focus Develop modern maneuver warfare
    germany.complete_focus("Develop_modern_maneuver_warfare")
    germany.add_political_power(100)

    germany.hire_chief_of_army("W_von_brauchitsch")

    assert germany.get_political_power() == 0

    #Then W. von Brauchitsch has the following bonuses
    w_von_brauchitsch = germany.find_modifier_by_id("W_von_brauchitsch")

    assert w_von_brauchitsch.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert w_von_brauchitsch.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_SPEED] == 0.10
    assert w_von_brauchitsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because W. von Brauchitsch is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
def test_w_von_brauchitsch_without_fulfilling_having_completed_focus_develop_modern_maneuver_warfare(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When W. von Brauchitsch is hired when Germany has not completed focus Develop modern maneuver warfare
    germany.add_political_power(100)

    germany.hire_chief_of_army("W_von_brauchitsch")

    assert germany.get_political_power() == 100

    #Then W. von Brauchitsch has the following bonuses
    w_von_brauchitsch = germany.find_modifier_by_id("W_von_brauchitsch")

    assert w_von_brauchitsch.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert w_von_brauchitsch.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_SPEED] == 0.10
    assert w_von_brauchitsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because W. von Brauchitsch is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_cannot_have_more_than_one_chief_of_army(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == 0.0

    #When Ludwig Beck is hired
    germany.add_political_power(200)

    germany.hire_chief_of_army("Ludwig_beck")

    assert germany.get_political_power() == 100

    #Then Ludwig Beck has the following bonuses
    ludwig_beck = germany.find_modifier_by_id("Ludwig_beck")

    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Ludwig Beck is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == 0.0

    #Then hiring another chief of army
    germany.hire_chief_of_army("Wilhelm_keitel")

    assert germany.get_political_power() == 0

    #Then WIlhelm Keitel has the following bonuses
    wIlhelm_keitel = germany.find_modifier_by_id("Wilhelm_keitel")

    assert wIlhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert wIlhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == -0.10
    assert wIlhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because WIlhelm Keiteln is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == -0.10

    #and the length of chiefs of army hired is only 1
    chief_of_army_list = [germany.get_chief_of_army()]
    assert len(chief_of_army_list) == 1

def test_swapping_chief_of_army(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == 0.0

    #When Ludwig Beck is hired
    germany.add_political_power(200)

    germany.hire_chief_of_army("Ludwig_beck")

    assert germany.get_political_power() == 100

    #Then Ludwig Beck has the following bonuses
    ludwig_beck = germany.find_modifier_by_id("Ludwig_beck")

    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert ludwig_beck.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Ludwig Beck is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == 0.0

    #Then hiring another chief of army
    germany.hire_chief_of_army("Wilhelm_keitel")

    assert germany.get_political_power() == 0

    #Then WIlhelm Keitel has the following bonuses
    wIlhelm_keitel = germany.find_modifier_by_id("Wilhelm_keitel")

    assert wIlhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert wIlhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == -0.10
    assert wIlhelm_keitel.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Ludwig Beck is replaced with WIlhelm Keitel
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_TRAINING_TIME] == -0.10

def test_another_country_cannot_hire_german_chief_of_army(germany, new_game): 
    #Given a testing country that is not Germany
    testing_country = create_custom_country(new_game)

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When testing country hires Ludwig Beck
    testing_country.add_political_power(100)

    testing_country.hire_chief_of_army("Ludwig_beck")

    #Then Ludwig Beck should not be hired
    assert testing_country.get_political_power() == 100

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0


















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)
