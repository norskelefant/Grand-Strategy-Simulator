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
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Gerd von Rundstedt is hired
    germany.add_political_power(100)

    germany.hire_high_commander("Gerd_von_rundstedt", 0)

    assert germany.get_political_power() == 0

    #Then Gerd von Rundstedt has the following bonuses
    gerd_von_rundstedt = germany.find_modifier_by_id("Gerd_von_rundstedt")

    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Gerd von Rundstedt is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_gerd_von_rundstedt_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Gerd von Rundstedt is hired without enough political power
    germany.add_political_power(0)

    germany.hire_high_commander("Gerd_von_rundstedt", 0)

    assert germany.get_political_power() == 0

    #Then Gerd von Rundstedt has the following bonuses
    gerd_von_rundstedt = germany.find_modifier_by_id("Gerd_von_rundstedt")

    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Gerd von Rundstedt is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0

def test_werner_von_fritsch(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Werner von Fritsch is hired when Werner is not hired elsewhere and Germany has not completed focus Reorganize the wehrmacht
    germany.add_political_power(100)

    germany.hire_high_commander("Werner_von_fritsch_hc", 0)

    assert germany.get_political_power() == 0

    #Then Werner von Fritsch has the following bonuses
    werner_von_fritsch = germany.find_modifier_by_id("Werner_von_fritsch_hc")

    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == -0.08
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Werner von Fritsch is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == -0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_werner_von_fritsch_without_fulfilling_werner_not_being_hired_somewhere_else(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Werner von Fritsch is hired when Werner is hired elsewhere and Germany has not completed focus Reorganize the wehrmacht
    germany.complete_focus("Prussian_artillery_doctrine")
    germany.add_political_power(200)

    germany.hire_chief_of_army("Werner_von_fritsch_coa")

    assert germany.get_political_power() == 100

    germany.hire_high_commander("Werner_von_fritsch_hc", 0)

    assert germany.get_political_power() == 100

    #Then Werner von Fritsch has the following bonuses
    werner_von_fritsch = germany.find_modifier_by_id("Werner_von_fritsch_hc")

    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == -0.08
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Werner von Fritsch is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_werner_von_fritsch_without_fulfilling_having_not_completed_focus_reorganize_the_wehrmacht(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Werner von Fritsch is hired when Werner is not hired elsewhere and Germany has completed focus Reorganize the wehrmacht
    germany.complete_focus("Reorganize_the_wehrmacht")
    germany.add_political_power(100)

    germany.hire_high_commander("Werner_von_fritsch_hc", 0)

    assert germany.get_political_power() == 100

    #Then Werner von Fritsch has the following bonuses
    werner_von_fritsch = germany.find_modifier_by_id("Werner_von_fritsch_hc")

    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == -0.08
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Werner von Fritsch is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_werner_von_fritsch_without_fulfilling_both_requirements(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Werner von Fritsch is hired when Werner is hired elsewhere and Germany has completed focus Reorganize the wehrmacht
    germany.complete_focus("Prussian_artillery_doctrine")
    germany.complete_focus("Reorganize_the_wehrmacht")
    germany.add_political_power(200)

    germany.hire_chief_of_army("Werner_von_fritsch_coa")

    assert germany.get_political_power() == 100

    germany.hire_high_commander("Werner_von_fritsch_hc", 0)

    assert germany.get_political_power() == 100

    #Then Werner von Fritsch has the following bonuses
    werner_von_fritsch = germany.find_modifier_by_id("Werner_von_fritsch_hc")

    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == -0.08
    assert werner_von_fritsch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Werner von Fritsch is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTRITION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_gunther_lutjens(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Günther Lütjens is hired
    germany.add_political_power(100)

    germany.hire_high_commander("Gunther_lutjens", 1)

    assert germany.get_political_power() == 0

    #Then Günther Lütjens has the following bonuses
    gunther_lutjens = germany.find_modifier_by_id("Gunther_lutjens")

    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Günther Lütjens is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_gunther_lutjens_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Günther Lütjens is hired without enough political power
    germany.add_political_power(0)

    germany.hire_high_commander("Gunther_lutjens", 2)

    assert germany.get_political_power() == 0

    #Then Günther Lütjens has the following bonuses
    gunther_lutjens = germany.find_modifier_by_id("Gunther_lutjens")

    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Günther Lütjens is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0

def test_ferdinand_schorner(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Ferdinand Schörner is hired
    germany.add_political_power(100)

    germany.hire_high_commander("Ferdinand_schorner", 1)

    assert germany.get_political_power() == 0

    #Then Ferdinand Schörner has the following bonuses
    ferdinand_schorner = germany.find_modifier_by_id("Ferdinand_schorner")

    assert ferdinand_schorner.get_modifier_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK] == 0.10
    assert ferdinand_schorner.get_modifier_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE] == 0.15
    assert ferdinand_schorner.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Ferdinand Schörner is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_ferdinand_schorner_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Ferdinand Schörner is hired without enough political power
    germany.add_political_power(99)

    germany.hire_high_commander("Ferdinand_schorner", 2)

    assert germany.get_political_power() == 99

    #Then Ferdinand Schörner has the following bonuses
    ferdinand_schorner = germany.find_modifier_by_id("Ferdinand_schorner")

    assert ferdinand_schorner.get_modifier_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK] == 0.10
    assert ferdinand_schorner.get_modifier_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE] == 0.15
    assert ferdinand_schorner.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Ferdinand Schörner is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_erich_bey(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erich Bey is hired
    germany.add_political_power(100)

    germany.hire_high_commander("Erich_bey", 1)

    assert germany.get_political_power() == 0

    #Then Erich Bey has the following bonuses
    erich_bey = germany.find_modifier_by_id("Erich_bey")

    assert erich_bey.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15
    assert erich_bey.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Erich Bey is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_erich_bey_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erich Bey is hired without enough political power
    germany.add_political_power(50)

    germany.hire_high_commander("Erich_bey", 1)

    assert germany.get_political_power() == 50

    #Then Erich Bey has the following bonuses
    erich_bey = germany.find_modifier_by_id("Erich_bey")

    assert erich_bey.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15
    assert erich_bey.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Erich Bey is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_viktor_schutze(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Viktor Schütze is hired
    germany.add_political_power(50)

    germany.hire_high_commander("Viktor_schutze", 0)

    assert germany.get_political_power() == 0

    #Then Viktor Schütze has the following bonuses
    viktor_schutze = germany.find_modifier_by_id("Viktor_schutze")

    assert viktor_schutze.get_modifier_bonuses()[modifier_types.Modifier_types.SUBMARINE_ATTACK] == 0.10
    assert viktor_schutze.get_modifier_bonuses()[modifier_types.Modifier_types.SUBMARINE_DEFENSE] == 0.05
    assert viktor_schutze.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

    #and Germany has the following bonuses because Viktor Schütze is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_ATTACK] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_DEFENSE] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

def test_viktor_schutze_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Viktor Schütze is hired without enough political power
    germany.add_political_power(49)

    germany.hire_high_commander("Viktor_schutze", 0)

    assert germany.get_political_power() == 49

    #Then Viktor Schütze has the following bonuses
    viktor_schutze = germany.find_modifier_by_id("Viktor_schutze")

    assert viktor_schutze.get_modifier_bonuses()[modifier_types.Modifier_types.SUBMARINE_ATTACK] == 0.10
    assert viktor_schutze.get_modifier_bonuses()[modifier_types.Modifier_types.SUBMARINE_DEFENSE] == 0.05
    assert viktor_schutze.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

    #but Germany has the following bonuses because Viktor Schütze is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBMARINE_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_josef_kammhuber(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Josef Kammhuber is hired
    germany.add_political_power(100)

    germany.hire_high_commander("Josef_kammhuber", 0)

    assert germany.get_political_power() == 0

    #Then Josef Kammhuber has the following bonuses
    josef_kammhuber = germany.find_modifier_by_id("Josef_kammhuber")

    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Josef Kammhuber is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_josef_kammhuber_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Josef Kammhuber is hired without enough political power
    germany.add_political_power(0)

    germany.hire_high_commander("Josef_kammhuber", 0)

    assert germany.get_political_power() == 0

    #Then Josef Kammhuber has the following bonuses
    josef_kammhuber = germany.find_modifier_by_id("Josef_kammhuber")

    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Josef Kammhuber is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_erwin_rommel(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erwin Rommel is hired when Germany has completed focus Adopt new panzer doctrine
    germany.complete_focus("Adopt_new_panzer_doctrine")
    germany.add_political_power(200)

    germany.hire_high_commander("Erwin_rommel", 0)

    assert germany.get_political_power() == 0

    #Then Erwin Rommel has the following bonuses
    erwin_rommel = germany.find_modifier_by_id("Erwin_rommel")

    assert erwin_rommel.get_modifier_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK] == 0.15
    assert erwin_rommel.get_modifier_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE] == 0.15
    assert erwin_rommel.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 30

    #and Germany has the following bonuses because Erwin Rommel is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 30

def test_erwin_rommel_without_fulfilling_having_completed_focus_adopt_new_panzer_doctrine(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erwin Rommel is hired when Germany has not completed focus Adopt new panzer doctrine
    germany.add_political_power(200)

    germany.hire_high_commander("Erwin_rommel", 0)

    assert germany.get_political_power() == 200

    #Then Erwin Rommel has the following bonuses
    erwin_rommel = germany.find_modifier_by_id("Erwin_rommel")

    assert erwin_rommel.get_modifier_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK] == 0.15
    assert erwin_rommel.get_modifier_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE] == 0.15
    assert erwin_rommel.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 30

    #but Germany has the following bonuses because Erwin Rommel is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_kurt_student(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Kurt Student is hired when Germany has completed focus Fallschirmjäger
    germany.complete_focus("Fallschirmjager")
    germany.add_political_power(100)

    germany.hire_high_commander("Kurt_student", 0)

    assert germany.get_political_power() == 0

    #Then Kurt Student has the following bonuses
    kurt_student = germany.find_modifier_by_id("Kurt_student")

    assert kurt_student.get_modifier_bonuses()[modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING] == 1.80
    assert kurt_student.get_modifier_bonuses()[modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE] == 0.15
    assert kurt_student.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Kurt Student is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING] == 1.80
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_kurt_student_without_fulfilling_having_completed_focus_fallschirmjager(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Kurt Student is hired when Germany has not completed focus Fallschirmjäger
    germany.add_political_power(100)

    germany.hire_high_commander("Kurt_student", 0)

    assert germany.get_political_power() == 100

    #Then Kurt Student has the following bonuses
    kurt_student = germany.find_modifier_by_id("Kurt_student")

    assert kurt_student.get_modifier_bonuses()[modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING] == 1.80
    assert kurt_student.get_modifier_bonuses()[modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE] == 0.15
    assert kurt_student.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Kurt Student is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_hugo_sperrle(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_ATTACK_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Hugo Sperrle is hired when Germany has completed focus Dive bombers
    germany.complete_focus("Dive_bombers")
    germany.add_political_power(100)

    germany.hire_high_commander("Hugo_sperrle", 0)

    assert germany.get_political_power() == 0

    #Then Hugo Sperrle has the following bonuses
    hugo_sperrle = germany.find_modifier_by_id("Hugo_sperrle")

    assert hugo_sperrle.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY] == 0.10
    assert hugo_sperrle.get_modifier_bonuses()[modifier_types.Modifier_types.GROUND_ATTACK_FACTOR] == 0.05
    assert hugo_sperrle.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Hugo Sperrle is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_ATTACK_FACTOR] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_hugo_sperrle_without_fulfilling_having_completed_focus_dive_bombers(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_ATTACK_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Hugo Sperrle is hired when Germany has not completed focus Dive bombers
    germany.add_political_power(100)

    germany.hire_high_commander("Hugo_sperrle", 0)

    assert germany.get_political_power() == 100

    #Then Hugo Sperrle has the following bonuses
    hugo_sperrle = germany.find_modifier_by_id("Hugo_sperrle")

    assert hugo_sperrle.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY] == 0.10
    assert hugo_sperrle.get_modifier_bonuses()[modifier_types.Modifier_types.GROUND_ATTACK_FACTOR] == 0.05
    assert hugo_sperrle.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Hugo Sperrle is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_ATTACK_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_erhard_milch(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erhard Milch is hired when Germany has completed focus Tactical bombers
    germany.complete_focus("Tactical_bombers")
    germany.add_political_power(100)

    germany.hire_high_commander("Erhard_milch", 0)

    assert germany.get_political_power() == 0

    #Then Erhard Milch has the following bonuses
    erhard_milch = germany.find_modifier_by_id("Erhard_milch")

    assert erhard_milch.get_modifier_bonuses()[modifier_types.Modifier_types.GROUND_SUPPORT] == 0.15
    assert erhard_milch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Erhard Milch is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_SUPPORT] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_erhard_milch_without_fulfilling_having_completed_focus_tactical_bombers(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Erhard Milch is hired when Germany has not completed focus Tactical bombers
    germany.add_political_power(100)

    germany.hire_high_commander("Erhard_milch", 0)

    assert germany.get_political_power() == 100

    #Then Erhard Milch has the following bonuses
    erhard_milch = germany.find_modifier_by_id("Erhard_milch")

    assert erhard_milch.get_modifier_bonuses()[modifier_types.Modifier_types.GROUND_SUPPORT] == 0.15
    assert erhard_milch.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Erhard Milch is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GROUND_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0

def test_robert_knauss(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBING] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BOMBER_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Robert Knauss is hired when Germany has completed focus Uralbomber program
    germany.complete_focus("Uralbomber_program")
    germany.add_political_power(100)

    germany.hire_high_commander("Robert_knauss", 0)

    assert germany.get_political_power() == 0

    #Then Robert Knauss has the following bonuses
    robert_knauss = germany.find_modifier_by_id("Robert_knauss")

    assert robert_knauss.get_modifier_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBING] == 0.05
    assert robert_knauss.get_modifier_bonuses()[modifier_types.Modifier_types.BOMBER_DEFENSE] == 0.02
    assert robert_knauss.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Robert Knauss is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBING] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BOMBER_DEFENSE] == 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_robert_knauss_without_fulfilling_having_completed_focus_uralbomber_program(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBING] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BOMBER_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Robert Knauss is hired when Germany has not completed focus Uralbomber program
    germany.add_political_power(100)

    germany.hire_high_commander("Robert_knauss", 0)

    assert germany.get_political_power() == 100

    #Then Robert Knauss has the following bonuses
    robert_knauss = germany.find_modifier_by_id("Robert_knauss")

    assert robert_knauss.get_modifier_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBING] == 0.05
    assert robert_knauss.get_modifier_bonuses()[modifier_types.Modifier_types.BOMBER_DEFENSE] == 0.02
    assert robert_knauss.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Robert Knauss is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBING] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BOMBER_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_alfred_becker(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Alfred Becker is hired when Germany has completed focus Salvage captured equipment
    germany.complete_focus("Salvage_captured_equipment")
    germany.add_political_power(100)

    germany.hire_high_commander("Alfred_becker", 0)

    assert germany.get_political_power() == 0

    #Then Alfred Becker has the following bonuses
    alfred_becker = germany.find_modifier_by_id("Alfred_becker")

    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.15
    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED] == 0.10
    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR] == 0.05
    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Alfred Becker is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_alfred_becker_without_fulfilling_having_completed_focus_salvage_captured_equipment(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Alfred Becker is hired when Germany has not completed focus Salvage captured equipment
    germany.add_political_power(100)

    germany.hire_high_commander("Alfred_becker", 0)

    assert germany.get_political_power() == 100

    #Then Alfred Becker has the following bonuses
    alfred_becker = germany.find_modifier_by_id("Alfred_becker")

    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.15
    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED] == 0.10
    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR] == 0.05
    assert alfred_becker.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Alfred Becker is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_walter_dornberger_while_fulfilling_all_requirements(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Walter Dornberger is hired when Germany has completed all 3 focuses
    germany.complete_focus("Rocketry_innovations")
    germany.complete_focus("Wonder_weapons")
    germany.complete_focus("Glorious_mechanical_machinations")
    germany.add_political_power(100)

    germany.hire_high_commander("Walter_dornberger", 0)

    assert germany.get_political_power() == 0

    #Then Walter Dornberger has the following bonuses
    walter_dornberger = germany.find_modifier_by_id("Walter_dornberger")

    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Walter Dornberger is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_walter_dornberger_while_fulfilling_having_completed_focus_rocketry_innovations(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Walter Dornberger is hired when Germany has completed focus Rocketry innovations
    germany.complete_focus("Rocketry_innovations")

    germany.add_political_power(100)

    germany.hire_high_commander("Walter_dornberger", 0)

    assert germany.get_political_power() == 0

    #Then Walter Dornberger has the following bonuses
    walter_dornberger = germany.find_modifier_by_id("Walter_dornberger")

    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Walter Dornberger is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_walter_dornberger_while_fulfilling_having_completed_focus_wonder_weapons(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Walter Dornberger is hired when Germany has completed focus Wonder weapons
    germany.complete_focus("Wonder_weapons")
    germany.add_political_power(100)

    germany.hire_high_commander("Walter_dornberger", 0)

    assert germany.get_political_power() == 0

    #Then Walter Dornberger has the following bonuses
    walter_dornberger = germany.find_modifier_by_id("Walter_dornberger")

    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Walter Dornberger is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_walter_dornberger_while_fulfilling_having_completed_focus_glorious_mechanical_machinations(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Walter Dornberger is hired when Germany has completed focus Glorious mechanical machinations
    germany.complete_focus("Glorious_mechanical_machinations")
    germany.add_political_power(100)

    germany.hire_high_commander("Walter_dornberger", 0)

    assert germany.get_political_power() == 0

    #Then Walter Dornberger has the following bonuses
    walter_dornberger = germany.find_modifier_by_id("Walter_dornberger")

    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Walter Dornberger is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_walter_dornberger_without_fulfilling_having_done_at_least_one_of_the_focuses(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Walter Dornberger is hired when Germany has completed none of the 3 focuses
    germany.add_political_power(100)

    germany.hire_high_commander("Walter_dornberger", 0)

    assert germany.get_political_power() == 100

    #Then Walter Dornberger has the following bonuses
    walter_dornberger = germany.find_modifier_by_id("Walter_dornberger")

    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.10
    assert walter_dornberger.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Walter Dornberger is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_having_three_high_commanders(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Günther Lütjens, Gerd von Rundstedt and Josef Kammhuber are all hired
    germany.add_political_power(300)

    germany.hire_high_commander("Gunther_lutjens", 0)
    germany.hire_high_commander("Gerd_von_rundstedt", 1)
    germany.hire_high_commander("Josef_kammhuber", 2)

    assert germany.get_political_power() == 0

    #Then they have the following bonuses
    gunther_lutjens = germany.find_modifier_by_id("Gunther_lutjens")
    gerd_von_rundstedt = germany.find_modifier_by_id("Gerd_von_rundstedt")
    josef_kammhuber = germany.find_modifier_by_id("Josef_kammhuber")

    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because all 3 are hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 60

def test_replacing_a_high_commander(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.0

    #When Günther Lütjens is hired
    germany.add_political_power(200)

    germany.hire_high_commander("Gunther_lutjens", 1)

    assert germany.get_political_power() == 100

    #Then Günther Lütjens has the following bonuses
    gunther_lutjens = germany.find_modifier_by_id("Gunther_lutjens")

    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Günther Lütjens is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.0

    #When Günther Lütjens is swapped with Erich Bey
    germany.hire_high_commander("Erich_bey", 1)

    assert germany.get_political_power() == 0

    #Then Erich Bey has the following bonuses
    erich_bey = germany.find_modifier_by_id("Erich_bey")

    assert erich_bey.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15
    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Günther Lütjens is replaced with Erich Bey
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15

def test_replacing_a_high_commander_with_three_high_commanders(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.0

    #When Günther Lütjens, Gerd von Rundstedt and Josef Kammhuber are all hired
    germany.add_political_power(400)

    germany.hire_high_commander("Gunther_lutjens", 0)
    germany.hire_high_commander("Gerd_von_rundstedt", 1)
    germany.hire_high_commander("Josef_kammhuber", 2)

    assert germany.get_political_power() == 100

    #Then they have the following bonuses
    gunther_lutjens = germany.find_modifier_by_id("Gunther_lutjens")
    gerd_von_rundstedt = germany.find_modifier_by_id("Gerd_von_rundstedt")
    josef_kammhuber = germany.find_modifier_by_id("Josef_kammhuber")

    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert gerd_von_rundstedt.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because all 3 are hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 60
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.0

    #When Günther is replaced with Erich Bey
    germany.hire_high_commander("Erich_bey", 0)

    assert germany.get_political_power() == 0

    #The Erich Bey should have the following bonuses
    erich_bey = germany.find_modifier_by_id("Erich_bey")

    assert erich_bey.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15
    assert josef_kammhuber.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses since Günther is replaced with Erich
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 60
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_AA_ATTACK] == 0.15

def test_one_cannot_hire_high_commanders_with_illegal_slot(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Günther Lütjens is hired with an illegal slot
    germany.add_political_power(100)

    germany.hire_high_commander("Gunther_lutjens", -1)
    germany.hire_high_commander("Gunther_lutjens", 3)

    assert germany.get_political_power() == 100

    #Then Günther Lütjens has the following bonuses
    gunther_lutjens = germany.find_modifier_by_id("Gunther_lutjens")

    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.10
    assert gunther_lutjens.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Günther Lütjens is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0

def test_another_country_cannot_hire_german_high_commander(germany, new_game): 
    #Given a testing country that is not Germany
    testing_country = create_custom_country(new_game)

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When testing country hires Günther Lütjens
    testing_country.add_political_power(100)

    testing_country.hire_chief_of_navy("Gunther_lutjens")

    #Then Günther Lütjens should not be hired
    assert testing_country.get_political_power() == 100

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0





















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)

