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

def test_konrad_adenauer(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05

    #When Konrad Adenauer becomes leader
    germany.switch_leader("Konrad_adenauer")

    #Then Konrad Adenauer has the following bonuses
    konrad_adenauer = germany.find_modifier_by_id("Konrad_adenauer")
    assert konrad_adenauer.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert konrad_adenauer.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert konrad_adenauer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -50
    assert konrad_adenauer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50
    assert konrad_adenauer.get_modifier_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05

    #and Germany has the following bonuses because Konrad Adenauer is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.182
    assert germany.get_full_stability() == pytest.approx(0.91)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.10

def test_hans_vogel(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MASTER_IMPACT] == 0.0

    #When Hans Vogel becomes leader
    germany.switch_leader("Hans_vogel")

    #Then Hans Vogel has the following bonuses
    hans_vogel = germany.find_modifier_by_id("Hans_vogel")
    assert hans_vogel.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert hans_vogel.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.05
    assert hans_vogel.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.05
    assert hans_vogel.get_modifier_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == -0.10
    assert hans_vogel.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -25
    assert hans_vogel.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50
    assert hans_vogel.get_modifier_bonuses()[modifier_types.Modifier_types.MASTER_IMPACT] == -0.10

    #and Germany has the following bonuses because Hans Vogel is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MASTER_IMPACT] == -0.10

def test_wilhelm_pieck(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.00

    #When Wilhelm Pieck becomes leader
    germany.switch_leader("Wilhelm_pieck")

    #Then Wilhelm Pieck has the following bonuses
    wilhelm_pieck = germany.find_modifier_by_id("Wilhelm_pieck")
    assert wilhelm_pieck.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.10
    assert wilhelm_pieck.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15

    #and Germany has the following bonuses because Wilhelm Pieck is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.274
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15


def test_walther_ulbricht(germany, new_game):
    # Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162

    # When Walther Ulbricht becomes leader
    germany.switch_leader("Walter_ulbricht_l")

    # Then Walther Ulbricht has the following bonuses
    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_l")
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10

    # And Germany has the following bonuses because Walther Ulbricht is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162

def test_ernst_thalmann(germany, new_game):
    # Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.09
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162

    # When Ernst Thälmann becomes leader
    germany.switch_leader("Ernst_thalmann_l")

    # Then Ernst Thälmann has the following bonuses
    ernst_thalmann = germany.find_modifier_by_id("Ernst_thalmann_l")
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.09
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.20
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.05

    # And Germany has the following bonuses because Ernst Thälmann is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.09
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == pytest.approx(0.11)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.012)

def test_heinrich_brandler(germany, new_game):
    # Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_CAP] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.00

    # When Heinrich Brandler becomes leader
    germany.switch_leader("Heinrich_brandler")

    # Then Heinrich Brandler has the following bonuses
    heinrich_brandler = germany.find_modifier_by_id("Heinrich_brandler")
    assert heinrich_brandler.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.10
    assert heinrich_brandler.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.15
    assert heinrich_brandler.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.25
    assert heinrich_brandler.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_CAP] == 0.05
    assert heinrich_brandler.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.05

    # And Germany has the following bonuses because Heinrich Brandler is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(-0.038)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_CAP] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.05

def test_otto_grotewohl(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_OPINION] == 0.00
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_DEMOCRATIC_DIPLOMACY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MASTER_IMPACT] == 0.00

    #When Otto Grotewohl becomes leader
    germany.switch_leader("Otto_grotewohl")

    #Then Otto Grotewohl has the following bonuses
    otto_grotewohl = germany.find_modifier_by_id("Otto_grotewohl")
    assert otto_grotewohl.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert otto_grotewohl.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.25
    assert otto_grotewohl.get_modifier_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_OPINION] == 0.10
    assert otto_grotewohl.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert otto_grotewohl.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_DEMOCRATIC_DIPLOMACY] == 25
    assert otto_grotewohl.get_modifier_bonuses()[modifier_types.Modifier_types.MASTER_IMPACT] == -0.10

    #and Germany has the following bonuses because Otto Grotewohl is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.182
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_OPINION] == 0.10
    assert germany.get_full_stability() == pytest.approx(0.91)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_DEMOCRATIC_DIPLOMACY] == 25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MASTER_IMPACT] == -0.10

def test_adolf_hitler(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.001
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AI_DESIRED_DIVISIONS_FACTOR] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET] == 0.05

    #When Germany switches away from Adolf Hitler and then back to him
    germany.switch_leader("Wilhelm_iv")
    germany.switch_leader("Adolf_hitler")

    #Then Adolf Hitler has the following bonuses
    adolf_hitler = germany.find_modifier_by_id("Adolf_hitler")
    assert adolf_hitler.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.001
    assert adolf_hitler.get_modifier_bonuses()[modifier_types.Modifier_types.AI_DESIRED_DIVISIONS_FACTOR] == 0.20
    assert adolf_hitler.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.1
    assert adolf_hitler.get_modifier_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.02
    assert adolf_hitler.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET] == 0.05

    #and Germany has the following bonuses because Adolf Hitler is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.001
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AI_DESIRED_DIVISIONS_FACTOR] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET] == 0.05

def test_heinrich_himmler(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAMAGE_TO_GARRISONS] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COUNTER_INTELLIGENCE] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTELLIGENCE_GAINED_FROM_COMBAT] == 0.00

    #When Heinrich Himmler becomes leader
    germany.switch_leader("Heinrich_himmler")

    #Then Heinrich Himmler has the following bonuses
    heinrich_himmler = germany.find_modifier_by_id("Heinrich_himmler")
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.DAMAGE_TO_GARRISONS] == -0.25
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == -0.30
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.02
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == -0.25
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.COUNTER_INTELLIGENCE] == 0.20
    assert heinrich_himmler.get_modifier_bonuses()[modifier_types.Modifier_types.INTELLIGENCE_GAINED_FROM_COMBAT] == 0.25

    #and Germany has the following bonuses because Heinrich Himmler is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAMAGE_TO_GARRISONS] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == -0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COUNTER_INTELLIGENCE] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INTELLIGENCE_GAINED_FROM_COMBAT] == 0.25

def test_hermann_goring(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_CAP] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.00

    #When Hermann Göring becomes leader
    germany.switch_leader("Hermann_goring_l")

    #Then Hermann Göring has the following bonuses
    hermann_goring = germany.find_modifier_by_id("Hermann_goring_l")

    print(hermann_goring.get_modifier_bonuses())
    print(hermann_goring.get_modifier_bonuses().keys())
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_CAP] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.05

    #and Germany has the following bonuses because Hermann Göring is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_CAP] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.05

def test_fritz_todt(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Fritz Todt becomes leader
    germany.switch_leader("Fritz_todt")

    #Then Fritz Todt has the following bonuses
    fritz_todt = germany.find_modifier_by_id("Fritz_todt")
    assert fritz_todt.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert fritz_todt.get_modifier_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10
    assert fritz_todt.get_modifier_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert fritz_todt.get_modifier_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.10
    assert fritz_todt.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert fritz_todt.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #and Germany has the following bonuses because Fritz Todt is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.20

def test_albert_speer(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174

    #When Albert Speer becomes leader
    germany.switch_leader("Albert_speer")

    #Then Albert Speer has the following bonuses
    albert_speer = germany.find_modifier_by_id("Albert_speer")
    assert albert_speer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert albert_speer.get_modifier_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert albert_speer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.01
    assert albert_speer.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.10
    assert albert_speer.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.10

    #and Germany has the following bonuses because Albert Speer is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.274
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.274


def test_joseph_goebbels(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.00
    assert germany.get_full_war_support() == 0.35
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.09
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BOOST_IDEOLOGY_MISSION_EFFECTS] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRENGTHEN_RESISTANCE_EFFICIENCY] == 0.00

    #When Joseph Goebbels becomes leader
    germany.switch_leader("Joseph_goebbels")

    #Then Joseph Goebbels has the following bonuses
    joseph_goebbels = germany.find_modifier_by_id("Joseph_goebbels")
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.10
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.20
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.10
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.10
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.10
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 2
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.BOOST_IDEOLOGY_MISSION_EFFECTS] == 0.15
    assert joseph_goebbels.get_modifier_bonuses()[modifier_types.Modifier_types.STRENGTHEN_RESISTANCE_EFFICIENCY] == 0.15

    #and Germany has the following bonuses because Joseph Goebbels is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert germany.get_full_war_support() == 0.45
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.07
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 2
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BOOST_IDEOLOGY_MISSION_EFFECTS] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRENGTHEN_RESISTANCE_EFFICIENCY] == 0.15


def test_rudolf_hess(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUNDS_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITARY_INDUSTRIAL_ORGANIZATION_RESEARCH_BONUS] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01

    #When Rudolf Hess becomes leader
    germany.switch_leader("Rudolf_hess")

    #Then Rudolf Hess has the following bonuses
    rudolf_hess = germany.find_modifier_by_id("Rudolf_hess")
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 1.0
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.FUNDS_GAIN] == 0.15
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.MILITARY_INDUSTRIAL_ORGANIZATION_RESEARCH_BONUS] == 0.15
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.05
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.15
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == -0.25
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.25
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.25
    assert rudolf_hess.get_modifier_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.05

    #and Germany has the following bonuses because Rudolf Hess is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 1.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUNDS_GAIN] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITARY_INDUSTRIAL_ORGANIZATION_RESEARCH_BONUS] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.212
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == pytest.approx(0.06)

def test_martin_bormann(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.THEORIST_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01

    #When Martin Bormann becomes leader
    germany.switch_leader("Martin_bormann")

    #Then Martin Bormann has the following bonuses
    martin_bormann = germany.find_modifier_by_id("Martin_bormann")
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.50
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.THEORIST_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.05
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.15
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.25
    assert martin_bormann.get_modifier_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.05

    #and Germany has the following bonuses because Martin Bormann is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_POLITICAL_POWER_GAIN] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.THEORIST_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.212
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == pytest.approx(0.06)

def test_eva_braun(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_war_support() == 0.35
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.00

    #When Eva Braun becomes leader
    germany.switch_leader("Eva_braun")

    #Then Eva Braun has the following bonuses
    eva_braun = germany.find_modifier_by_id("Eva_braun")
    assert eva_braun.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.15
    assert eva_braun.get_modifier_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == -0.10
    assert eva_braun.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.50
    assert eva_braun.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.05
    assert eva_braun.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE] == 0.05
    assert eva_braun.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.05

    #and Germany has the following bonuses because Eva Braun is leader
    assert germany.get_full_war_support() == 0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.05

def test_otto_strasser(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == 0.00
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_war_support() == 0.35

    #When Otto Strasser becomes leader
    germany.switch_leader("Otto_strasser")

    print(germany.get_leader().get_id())

    #Then Otto Strasser has the following bonuses
    otto_strasser = germany.find_modifier_by_id("Otto_strasser")
    assert otto_strasser.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == -0.05
    assert otto_strasser.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == -0.05
    assert otto_strasser.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -20
    assert otto_strasser.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert otto_strasser.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05

    #and Germany has the following bonuses because Otto Strasser is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.124
    #25% * ((1+10%)*(1-10%)*(1-12.4%)) = 0.21681
    assert germany.get_consumer_goods() == pytest.approx(0.21681)
    assert germany.get_full_war_support() == 0.40


def test_august_von_mackensen(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_war_support() == 0.35
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.00

    #When August von Mackensen becomes leader
    germany.switch_leader("August_von_mackensen")

    #Then August von Mackensen has the following bonuses
    august_von_mackensen = germany.find_modifier_by_id("August_von_mackensen")
    assert august_von_mackensen.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
    assert august_von_mackensen.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.05
    assert august_von_mackensen.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.10
    assert august_von_mackensen.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.10
    assert august_von_mackensen.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.05

    #and Germany has the following bonuses because August von Mackensen is leader
    assert germany.get_full_war_support() == 0.40
    assert germany.get_full_stability() == 0.86
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_RECOVERY_RATE] == 0.05

def test_wilhelm_ii(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_DEMOCRATIC_DIPLOMACY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.00
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_OPINION] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == 0.00

    #When Wilhelm II becomes leader
    germany.switch_leader("Wilhelm_ii")

    #Then Wilhelm II has the following bonuses
    wilhelm_ii = germany.find_modifier_by_id("Wilhelm_ii")
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_DEMOCRATIC_DIPLOMACY] == -50
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == -0.02
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.10
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_OPINION] == -0.15
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.25
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.25
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == -0.25
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.25
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == -0.25
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == -0.25
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == -0.25
    assert wilhelm_ii.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == -0.25

    #and Germany has the following bonuses because Wilhelm II is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_DEMOCRATIC_DIPLOMACY] == -50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == -0.02
    assert germany.get_full_stability() == pytest.approx(0.91)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(-0.018)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_OPINION] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == -0.25

def test_wilhelm_iii(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_stability() == pytest.approx(0.81)

    #When Wilhelm III becomes leader
    germany.switch_leader("Wilhelm_iii")

    #Then Wilhelm III has the following bonuses
    wilhelm_iii = germany.find_modifier_by_id("Wilhelm_iii")
    assert wilhelm_iii.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.05

    #and Germany has the following bonuses because Wilhelm III is leader
    assert germany.get_full_stability() == 0.86

def test_wilhelm_iv(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.001
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AI_DESIRED_DIVISIONS_FACTOR] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET] == 0.05

    #When Wilhelm IV becomes leader
    germany.switch_leader("Wilhelm_iv")

    #Then Wilhelm IV has the following bonuses
    wilhelm_iv = germany.find_modifier_by_id("Wilhelm_iv")
    assert wilhelm_iv.get_modifier_bonuses() == {}

    #and Germany has the following bonuses because Wilhelm IV is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AI_DESIRED_DIVISIONS_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET] == 0.0

def test_victoria(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_STABILITY] == 0.00
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_war_support() == 0.35
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162

    #When Victoria becomes leader
    germany.switch_leader("Victoria")

    #Then Victoria has the following bonuses
    victoria = germany.find_modifier_by_id("Victoria")
    assert victoria.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_STABILITY] == 0.001
    assert victoria.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert victoria.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
    assert victoria.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.10
    assert victoria.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.15

    #and Germany has the following bonuses because Victoria is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_STABILITY] == 0.001
    assert germany.get_full_stability() == pytest.approx(0.91)
    assert germany.get_full_war_support() == 0.40
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.232)

def test_erich_raeder(germany, new_game):
    # Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FLEET_COORDINATION] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SHIP_RECOVERY_RATE] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == 0.00

    #When Erich Raeder becomes leader
    germany.switch_leader("Erich_raeder_l")

    #Then Erich Raeder has the following bonuses
    erich_raeder = germany.find_modifier_by_id("Erich_raeder_l")
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.FLEET_COORDINATION] == 0.15
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.SHIP_RECOVERY_RATE] == 0.10
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.08
    assert erich_raeder.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == -0.05

    #and Germany has the following bonuses because Erich Raeder is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FLEET_COORDINATION] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SHIP_RECOVERY_RATE] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN] == 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ORGANIZATION] == -0.05


def test_fourth_supreme_army_command(germany, new_game):
    # Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_EXPERIENCE_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_EXPERIENCE_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == 0.00
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == 0.00

    # When Fourth Supreme Army Command becomes leader
    germany.switch_leader("Fourth_supreme_army_command")

    # Then Fourth Supreme Army Command has the following bonuses
    leader = germany.find_modifier_by_id("Fourth_supreme_army_command")
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.15
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == -0.10
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.10
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.ARMY_EXPERIENCE_GAIN] == 0.10
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.NAVAL_EXPERIENCE_GAIN] == 0.10
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == -0.25
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == -0.25
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == -0.25
    assert leader.get_modifier_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == -0.25

    # And Germany has the following bonuses because Fourth Supreme Army Command is leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(-0.108)
    assert germany.get_full_stability() == 0.71
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_PLANNING_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_EXPERIENCE_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVAL_EXPERIENCE_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST] == -0.25






















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)