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

def test_ig_farben(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0

    #When IG Farben is hired
    germany.add_political_power(150)

    germany.hire_industrial_concern("IG_farben")

    assert germany.get_political_power() == 0

    #Then IG Farben has the following bonuses
    ig_farben = germany.find_modifier_by_id("IG_farben")

    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because IG Farben is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15

def test_ig_farben_without_fulfilling_political_power_cost(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0

    #When IG Farben is hired without fulfilling political power cost
    germany.add_political_power(149)

    germany.hire_industrial_concern("IG_farben")

    assert germany.get_political_power() == 149

    #Then IG Farben has the following bonuses
    ig_farben = germany.find_modifier_by_id("IG_farben")

    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15

    #but Germany has the following bonuses because IG Farben is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0

def test_krupp(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0

    #When Krupp is hired
    germany.add_political_power(150)

    germany.hire_industrial_concern("Krupp")

    assert germany.get_political_power() == 0

    #Then Krupp has the following bonuses
    krupp = germany.find_modifier_by_id("Krupp")

    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL] == 6
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.05
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because Krupp is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 6
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.15

def test_krupp_without_fulfilling_political_power_cost(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0

    #When Krupp is hired without enough political power
    germany.add_political_power(100)

    germany.hire_industrial_concern("Krupp")

    assert germany.get_political_power() == 100

    #Then Krupp has the following bonuses
    krupp = germany.find_modifier_by_id("Krupp")

    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL] == 6
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.05
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.15

    #but Germany has the following bonuses because Krupp is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0

def test_siemens(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED] == 0

    #When Siemens is hired
    germany.add_political_power(150)

    germany.hire_industrial_concern("Siemens")

    assert germany.get_political_power() == 0

    #Then Krupp has the following bonuses
    siemens = germany.find_modifier_by_id("Siemens")

    assert siemens.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.10
    assert siemens.get_modifier_bonuses()[modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because Siemens is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED] == 0.15

def test_siemens_without_fulfilling_political_power_cost(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED] == 0

    #When Siemens is hired without enough political power
    germany.add_political_power(50)

    germany.hire_industrial_concern("Siemens")

    assert germany.get_political_power() == 50

    #Then Krupp has the following bonuses
    siemens = germany.find_modifier_by_id("Siemens")

    assert siemens.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.10
    assert siemens.get_modifier_bonuses()[modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED] == 0.15

    #but Germany has the following bonuses because Siemens is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED] == 0

def test_vereinigte_stahlwerke(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.0

    #When Vereinigte Stahlwerke is hired
    germany.add_political_power(150)

    germany.hire_industrial_concern("Vereinigte_stahlwerke")

    assert germany.get_political_power() == 0

    #Then Vereinigte Stahlwerke has the following bonuses
    vereinigte_stahlwerke = germany.find_modifier_by_id("Vereinigte_stahlwerke")

    assert vereinigte_stahlwerke.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.10
    assert vereinigte_stahlwerke.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.15
    assert vereinigte_stahlwerke.get_modifier_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because Vereinigte Stahlwerke is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.15

def test_vereinigte_stahlwerke_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.0

    #When Vereinigte Stahlwerke is hired without enough political power
    germany.add_political_power(0)

    germany.hire_industrial_concern("Vereinigte_stahlwerke")

    assert germany.get_political_power() == 0

    #Then Vereinigte Stahlwerke has the following bonuses
    vereinigte_stahlwerke = germany.find_modifier_by_id("Vereinigte_stahlwerke")

    assert vereinigte_stahlwerke.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.10
    assert vereinigte_stahlwerke.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.15
    assert vereinigte_stahlwerke.get_modifier_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.15

    #but Germany has the following bonuses because Vereinigte Stahlwerke is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.0

def test_deutsche_reichsbahn(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_ARMOR] == 0.0

    #When Deutsche Reichsbahn is hired
    germany.add_political_power(150)

    germany.hire_industrial_concern("Deutsche_reichsbahn")

    assert germany.get_political_power() == 0

    #Then Deutsche Reichsbahn has the following bonuses
    deutsche_reichsbahn = germany.find_modifier_by_id("Deutsche_reichsbahn")

    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.15
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED] == 0.15
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.TRAIN_PRODUCTION_COST] == -0.25
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.TRAIN_ARMOR] == 0.15

    #and Germany has the following bonuses because Deutsche Reichsbahn is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_PRODUCTION_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_ARMOR] == 0.15

def test_deutsche_reichsbahn_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_ARMOR] == 0.0

    #When Deutsche Reichsbahn is hired without enough political power
    germany.add_political_power(149)

    germany.hire_industrial_concern("Deutsche_reichsbahn")

    assert germany.get_political_power() == 149

    #Then Deutsche Reichsbahn has the following bonuses
    deutsche_reichsbahn = germany.find_modifier_by_id("Deutsche_reichsbahn")

    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.15
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED] == 0.15
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.TRAIN_PRODUCTION_COST] == -0.25
    assert deutsche_reichsbahn.get_modifier_bonuses()[modifier_types.Modifier_types.TRAIN_ARMOR] == 0.15

    #but Germany has the following bonuses because Deutsche Reichsbahn is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRAIN_ARMOR] == 0.0

def test_philipp_holzmann(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.0

    #When Philipp Holzmann is hired
    germany.add_political_power(150)

    germany.hire_industrial_concern("Philipp_holzmann")

    assert germany.get_political_power() == 0

    #Then Philipp Holzmann has the following bonuses
    philipp_holzmann = germany.find_modifier_by_id("Philipp_holzmann")

    assert philipp_holzmann.get_modifier_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert philipp_holzmann.get_modifier_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.10

    #and Germany has the following bonuses because Philipp Holzmann is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.10

def test_philipp_holzmann_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.0

    #When Philipp Holzmann is hired without enough political power
    germany.add_political_power(100)

    germany.hire_industrial_concern("Philipp_holzmann")

    assert germany.get_political_power() == 100

    #Then Philipp Holzmann has the following bonuses
    philipp_holzmann = germany.find_modifier_by_id("Philipp_holzmann")

    assert philipp_holzmann.get_modifier_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert philipp_holzmann.get_modifier_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.10

    #but Germany has the following bonuses because Philipp Holzmann is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED] == 0.0

def test_rwe(germany, new_game):
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED] == 0.0

    #When RWE is hired
    germany.add_political_power(150)

    germany.hire_industrial_concern("RWE")

    assert germany.get_political_power() == 0

    #Then RWE has the following bonuses
    rwe = germany.find_modifier_by_id("RWE")

    assert rwe.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.075
    assert rwe.get_modifier_bonuses()[modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED] == 0.05

    #and Germany has the following bonuses because RWE is hired
    #25% * ((1+10%)*(1-12.4%)*(1-7.5%)) = 0.2228325
    assert germany.get_consumer_goods() == pytest.approx(0.2228325)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.099)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED] == 0.05

def test_rwe_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED] == 0.0

    #When RWE is hired without enough political power
    germany.add_political_power(149.99)

    germany.hire_industrial_concern("RWE")

    assert germany.get_political_power() == 149.99

    #Then RWE has the following bonuses
    rwe = germany.find_modifier_by_id("RWE")

    assert rwe.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.075
    assert rwe.get_modifier_bonuses()[modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED] == 0.05

    #but Germany has the following bonuses because RWE is not hired
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED] == 0.0

def test_reichswerke(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST] == 0.0

    #When Reichswerke is hired when having completed focus Establish the reichswerke
    germany.complete_focus("Establish_the_reichswerke")
    germany.add_political_power(150)

    germany.hire_industrial_concern("Reichswerke")

    assert germany.get_political_power() == 0

    #Then Reichswerke has the following bonuses
    reichswerke = germany.find_modifier_by_id("Reichswerke")

    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST] == -0.025
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST] == -0.025

    #and Germany has the following bonuses because Reichswerke is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    #25% * ((1+10%)*(1-12.4%)*(1+5%)) = 0.252945
    assert germany.get_consumer_goods() == pytest.approx(0.252945)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.026)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST] == -0.025

def test_reichswerke_without_fulfilling_having_completed_focus_establish_the_reichswerke(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST] == 0.0

    #When Reichswerke is hired when not having completed focus Establish the reichswerke
    germany.add_political_power(150)

    germany.hire_industrial_concern("Reichswerke")

    assert germany.get_political_power() == 150

    #Then Reichswerke has the following bonuses
    reichswerke = germany.find_modifier_by_id("Reichswerke")

    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST] == -0.025
    assert reichswerke.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST] == -0.025

    #but Germany has the following bonuses because Reichswerke is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST] == 0.0

def test_cannot_have_more_than_one_industrial_concern(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0

    #When IG Farben is hired
    germany.add_political_power(300)

    germany.hire_industrial_concern("IG_farben")

    assert germany.get_political_power() == 150

    #Then IG Farben has the following bonuses
    ig_farben = germany.find_modifier_by_id("IG_farben")

    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because IG Farben is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.0

    #Then hiring another industrial concern

    germany.hire_industrial_concern("Krupp")

    assert germany.get_political_power() == 0

    #Then Krupp has the following bonuses
    krupp = germany.find_modifier_by_id("Krupp")

    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL] == 6
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.05
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because Krupp is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 6
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.05

    #and the length of industrial concerns hired is only 1
    industrial_concern_list = [germany.get_industrial_concern()]
    assert len(industrial_concern_list) == 1

def test_swapping_industrial_concern(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0

    #When IG Farben is hired
    germany.add_political_power(300)

    germany.hire_industrial_concern("IG_farben")

    assert germany.get_political_power() == 150

    #Then IG Farben has the following bonuses
    ig_farben = germany.find_modifier_by_id("IG_farben")

    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert ig_farben.get_modifier_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because IG Farben is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.0

    #Then hiring another industrial concern

    germany.hire_industrial_concern("Krupp")

    assert germany.get_political_power() == 0

    #Then Krupp has the following bonuses
    krupp = germany.find_modifier_by_id("Krupp")

    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL] == 6
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.05
    assert krupp.get_modifier_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.15

    #and Germany has the following bonuses because Krupp is hired while IG Farben is replaced
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL] == 6
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY] == 0.05


def test_another_country_cannot_hire_german_industrial_concern(germany, new_game): 
    #Given a testing country that is not Germany
    testing_country = create_custom_country(new_game)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0

    #When testing country hires IG Farben
    testing_country.add_political_power(150)

    testing_country.hire_industrial_concern("IG_farben")

    #Then IG Farben should not be hired
    assert testing_country.get_political_power() == 150

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED] == 0.0
















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)