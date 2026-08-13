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

def test_hjalmar_schact(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany has enough political power
    germany.add_political_power(75)

    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 0

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #and the full added bonuses should be the following
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.124
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.20

def test_hjalmar_schacht_without_fulfilling_political_power_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany does not have enough political power
    germany.hire_advisor("Hjalmar_schacht", 0)

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #but the full bonuses should remain the same as Schacht should not be hired
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

def test_hjalmar_schacht_without_fulfilling_not_communist_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany is communist
    germany.add_political_power(75)

    germany.change_ideology(ideologies.Ideologies.COMMUNIST)

    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 75

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #but the full bonuses should remain the same as Schacht should not be hired
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

def test_hjalmar_schacht_without_fulfilling_not_having_hired_walther_funk_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany already has Walther Funk hired
    germany.add_political_power(225)

    germany.hire_advisor("Walther_funk", 1)

    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 75

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #but the full bonuses should remain the same as Schacht should not be hired
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681(since Walther Funk also has -10% consumer goods bonus)
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.124)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

def test_walther_funk(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0

    #When Walther Funk is hired when all requirements are fulfilled
    germany.add_political_power(150)

    germany.hire_advisor("Walther_funk", 1)

    assert germany.get_political_power() == 0

    #Then Walther Funk has the following bonuses
    walther_funk = germany.find_modifier_by_id("Walther_funk")

    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.15
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15

    #and the full bonuses should be the following
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.124)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15

def test_walther_funk_without_fulfilling_party_is_fascist_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0

    #When Walther Funk is hired when Germany is not fascist
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)

    germany.add_political_power(150)

    germany.hire_advisor("Walther_funk", 1)

    assert germany.get_political_power() == 150

    #Then Walther Funk has the following bonuses
    walther_funk = germany.find_modifier_by_id("Walther_funk")

    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.15
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15

    #but the full bonuses should be the following since Walther Funk is not hired
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0

def test_walther_funk_without_fulfilling_not_having_hired_hjalmar_schacht_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0

    #When Walther Funk is hired when Germany has already hired Hjalmar Schacht
    germany.add_political_power(225)

    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 150

    germany.hire_advisor("Walther_funk", 1)

    assert germany.get_political_power() == 150

    #Then Walther Funk has the following bonuses
    walther_funk = germany.find_modifier_by_id("Walther_funk")

    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.15
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15

    #but the full bonuses should be the following since Walther Funk is not hired(but Hjalmar Schacht is)
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.124)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0

def test_walther_funk_without_fulfilling_not_having_hired_ludwig_erhard_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0

    #When Walther Funk is hired when Germany has already hired Ludwig Erhard
    germany.add_political_power(300)

    germany.complete_focus("Prioritize_economic_growth")

    germany.hire_advisor("Ludwig_erhard", 0)

    assert germany.get_political_power() == 150

    germany.hire_advisor("Walther_funk", 1)

    assert germany.get_political_power() == 150

    #Then Walther Funk has the following bonuses
    walther_funk = germany.find_modifier_by_id("Walther_funk")

    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.15
    assert walther_funk.get_modifier_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.15

    #but the full bonuses should be the following since Walther Funk is not hired(but Hjalmar Schacht is)
    #25% * ((1+10%)*(1-12.4%)*(1-15%)) = 0.204765
    assert germany.get_consumer_goods() == 0.204765
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.174)

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FREE_REPAIR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED] == 0.0

def test_franz_seldte_while_fulfilling_having_reinstated_nazi_leadership(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

    #When Franz Seldte is hired when nazi leadership is reinstated
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(150)

    germany.activate_event("Reinstated_nazi_leadership")

    germany.hire_advisor("Franz_seldte", 2)

    assert germany.get_political_power() == 0

    #Then Franz Seldte has the following bonuses
    franz_seldte = germany.find_modifier_by_id("Franz_seldte")

    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == -0.05
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.03
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.01

    #and the full bonuses should be the following since Franz Seldte is hired
    assert germany.get_full_stability() == 0.76
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.025
    #2% lost by stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.179
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.179
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.01

def test_franz_seldte_while_fulfilling_being_fascist(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

    #When Franz Seldte is hired when Germany is fascist
    germany.add_political_power(150)

    germany.hire_advisor("Franz_seldte", 2)

    assert germany.get_political_power() == 0

    #Then Franz Seldte has the following bonuses
    franz_seldte = germany.find_modifier_by_id("Franz_seldte")

    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == -0.05
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.03
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.01

    #and the full bonuses should be the following since Franz Seldte is hired
    assert germany.get_full_stability() == 0.76
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.025
    #2% lost by stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.179
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.179
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.01

def test_franz_seldte_without_fulfilling_having_gotten_event_reinstated_nazi_leadership_and_being_fascist(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

    #When Franz Seldte is hired when Germany is is not fascist or has gotten event reinstated nazi leadership
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(150)

    germany.hire_advisor("Franz_seldte", 2)

    assert germany.get_political_power() == 150

    #Then Franz Seldte has the following bonuses
    franz_seldte = germany.find_modifier_by_id("Franz_seldte")

    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == -0.05
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.025
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.03
    assert franz_seldte.get_modifier_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == -0.01

    #but the full bonuses should remain the same since Franz Seldte is not hired
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

def test_hanns_kerrl(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0

    #When Hanns Kerrl is hired when requirements are fulfilled
    germany.add_political_power(150)

    germany.hire_advisor("Hanns_kerrl", 0)

    assert germany.get_political_power() == 0

    #Then Hanns Kerrl has the following bonuses
    hanns_kerrl = germany.find_modifier_by_id("Hanns_kerrl")

    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == -0.025
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.02
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0020

    #and the full bonuses should be the following after hiring Hanns Kerrl
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == pytest.approx(-0.015)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0020

def test_hanns_kerrl_without_fulfilling_having_gotten_event_reinstated_nazi_leadership_and_being_fascist(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0

    #When Hanns Kerrl is hired when Germany is not fascist or has gotten event reinstated nazi leadership
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)

    germany.add_political_power(150)

    germany.hire_advisor("Hanns_kerrl", 0)

    assert germany.get_political_power() == 150

    #Then Hanns Kerrl has the following bonuses
    hanns_kerrl = germany.find_modifier_by_id("Hanns_kerrl")

    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == -0.025
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.02
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0020

    #but the full bonuses should be the same since hanns Kerrl is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0

def test_hanns_kerrl_without_fulfilling_not_having_done_focus_hegemony_of_the_ss(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0

    #When Hanns Kerrl is hired when Germany has completed focus Hegemony of the SS
    germany.complete_focus("Hegemony_of_the_ss")
    
    germany.add_political_power(150)

    germany.hire_advisor("Hanns_kerrl", 0)

    assert germany.get_political_power() == 150

    #Then Hanns Kerrl has the following bonuses
    hanns_kerrl = germany.find_modifier_by_id("Hanns_kerrl")

    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == -0.025
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.02
    assert hanns_kerrl.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0020

    #but the full bonuses should be the same since hanns Kerrl is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING] == 0.0

def test_reinhard_heydrich_while_fulfilling_having_reinstated_nazi_leadership(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.25

    #When Reinhard Heydrich is hired when Germany has gotten event reinstated nazi leadership
    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)
    germany.activate_event("Reinstated_nazi_leadership")
    
    germany.add_political_power(150)

    germany.hire_advisor("Reinhard_heydrich", 0)

    assert germany.get_political_power() == 0

    #Then Reinhard Heydrich has the following bonuses
    reinhard_heydrich = germany.find_modifier_by_id("Reinhard_heydrich")

    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.05
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.002
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.002

    #and the full bonuses should be the following since Reinhard Heydrich is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.152
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.252

def test_reinhard_heydrich_while_fulfilling_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.25

    #When Reinhard Heydrich is hired when Germany is fascist
    germany.add_political_power(150)

    germany.hire_advisor("Reinhard_heydrich", 0)

    assert germany.get_political_power() == 0

    #Then Reinhard Heydrich has the following bonuses
    reinhard_heydrich = germany.find_modifier_by_id("Reinhard_heydrich")

    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.05
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.002
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.002

    #and the full bonuses should be the following since Reinhard Heydrich is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.152
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.252

def test_reinhard_heydrich_without_fulfilling_having_gotten_event_reinstated_nazi_leadership_and_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.25

    #When Reinhard Heydrich is hired when Germany is not fascist or has gotten event reinstate nazi leadership
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(150)

    germany.hire_advisor("Reinhard_heydrich", 0)

    assert germany.get_political_power() == 150

    #Then Reinhard Heydrich has the following bonuses
    reinhard_heydrich = germany.find_modifier_by_id("Reinhard_heydrich")

    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.05
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.002
    assert reinhard_heydrich.get_modifier_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.002

    #but the full bonuses should be the same as Reinhard is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == -0.25

def test_joachim_von_ribbentrop_while_fulfilling_having_completed_focus_reorganize_the_wehrmacht_and_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0

    #When Joachim von Ribbentrop is hired when Germany is fascist and has completed focus Reorganize the wehrmacht
    germany.complete_focus("Reorganize_the_wehrmacht")
    germany.add_political_power(50)

    germany.hire_advisor("Joachim_von_ribbentrop", 0)

    assert germany.get_political_power() == 0

    #Then Joachim von Ribbentrop has the following bonuses
    Joachim_von_ribbentrop = germany.find_modifier_by_id("Joachim_von_ribbentrop")

    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == -0.25
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 5.0
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == -0.15
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.25

    #and the full bonuses should be the following since Joachim von Ribbentrop is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 5.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.25

def test_joachim_von_ribbentrop_while_fulfilling_having_reinstated_nazi_leadership(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0

    #When Joachim von Ribbentrop is hired when Germany is fascist and has completed focus Reorganize the wehrmacht
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)
    germany.activate_event("Reinstated_nazi_leadership")
    germany.add_political_power(50)

    germany.hire_advisor("Joachim_von_ribbentrop", 0)

    assert germany.get_political_power() == 0

    #Then Joachim von Ribbentrop has the following bonuses
    Joachim_von_ribbentrop = germany.find_modifier_by_id("Joachim_von_ribbentrop")

    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == -0.25
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 5.0
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == -0.15
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.25

    #and the full bonuses should be the following since Joachim von Ribbentrop is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 5.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.25

def test_joachim_von_ribbentrop_without_fulfilling_having_reinstated_nazi_leadership_and_having_completed_focus_reorganize_the_wehrmacht_and_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0

    #When Joachim von Ribbentrop is hired when Germany is not fascist or has completed focus reorganize the wehrmacht and has gotten event reinstated nazi leadership
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)
    germany.add_political_power(50)

    germany.hire_advisor("Joachim_von_ribbentrop", 0)

    assert germany.get_political_power() == 50

    #Then Joachim von Ribbentrop has the following bonuses
    Joachim_von_ribbentrop = germany.find_modifier_by_id("Joachim_von_ribbentrop")

    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == -0.25
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 5.0
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == -0.15
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert Joachim_von_ribbentrop.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.25

    #but the full bonuses should reamin the same since Joachim von Ribbentrop is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0

def test_konstantin_von_neurath(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

    #When Konstantin von Neurath is when Germany is not communist and has completed focus Heed von Neurath's concerns
    germany.complete_focus("Heed_von_neuraths_concerns")
    germany.add_political_power(50)

    germany.hire_advisor("Konstantin_von_neurath", 0)

    assert germany.get_political_power() == 0

    #Then Konstantin von Neurath has the following bonuses
    konstantin_von_neurath = germany.find_modifier_by_id("Konstantin_von_neurath")

    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == -0.25
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == -0.50
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == -0.10
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.01

    #and the full bonuses should be the following since Konstantin von Neurath is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == -0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.01

def test_konstantin_von_neurath_without_fulfilling_not_being_communist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

    #When Konstantin von Neurath is when Germany is not communist and has completed focus Heed von Neurath's concerns
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(50)

    germany.hire_advisor("Konstantin_von_neurath", 0)

    assert germany.get_political_power() == 50

    #Then Konstantin von Neurath has the following bonuses
    konstantin_von_neurath = germany.find_modifier_by_id("Konstantin_von_neurath")

    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == -0.25
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == -0.50
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == -0.10
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.01

    #but the full bonuses should be the same since Konstantin von Neurath is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

def test_konstantin_von_neurath_without_fulfilling_having_completed_focus_heed_von_neuraths_concerns(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

    #When Konstantin von Neurath is when Germany is not communist and has completed focus Heed von Neurath's concerns
    germany.add_political_power(50)

    germany.hire_advisor("Konstantin_von_neurath", 0)

    assert germany.get_political_power() == 50

    #Then Konstantin von Neurath has the following bonuses
    konstantin_von_neurath = germany.find_modifier_by_id("Konstantin_von_neurath")

    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == -0.25
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == -0.50
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.10
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == -0.10
    assert konstantin_von_neurath.get_modifier_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.01

    #but the full bonuses should be the same since Konstantin von Neurath is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED] == 0.0

def test_leni_riefenstahl_while_fulfilling_both_requirements(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0

    #When Leni Reifenstahl is hired when Germany has reinstated nazi leadership and has completed focus fund the film department
    germany.complete_focus("Fund_the_film_department")
    germany.activate_event("Reinstated_nazi_leadership")
    germany.add_political_power(150)

    germany.hire_advisor("Leni_riefenstahl", 0)

    assert germany.get_political_power() == 0

    #Then Leni Reifenstahl has the following bonuses
    leni_reifenstahl = germany.find_modifier_by_id("Leni_riefenstahl")

    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15
    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0010

    #and the full bonuses should be the following since Leni Reifenstahl is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0010

def test_leni_riefenstahl_without_fulfilling_having_reinstated_nazi_leadership_and_having_completed_focus_fund_the_film_department(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0

    #When Leni Reifenstahl is hired when Germany has not gotten reinstated nazi leadership and has not completed focus fund the film department
    germany.add_political_power(150)

    germany.hire_advisor("Leni_riefenstahl", 0)

    assert germany.get_political_power() == 150

    #Then Leni Reifenstahl has the following bonuses
    leni_reifenstahl = germany.find_modifier_by_id("Leni_riefenstahl")

    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15
    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert leni_reifenstahl.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0010

    #but the full bonuses should be the same as Leni is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0

def test_wilhelm_canaris(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

    #When Wilhelm Canaris is hired when Germany has an intelligency agency and has not completed focuses Reorganize secret services and Start the proletarian revolution
    germany.create_intelligence_agency("Testing_agency")
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_canaris", 0)

    assert germany.get_political_power() == 0

    #Then Wilhelm Canaris has the following bonuses
    wilhelm_canaris = germany.find_modifier_by_id("Wilhelm_canaris")

    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1.0
    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

    #and the full bonuses should be the following since Wilhelm Canaris is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

def test_wilhelm_canaris_without_fulfilling_having_created_an_intelligence_agency(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

    #When Wilhelm Canaris is hired when Germany has not created an intelligency agency
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_canaris", 0)

    assert germany.get_political_power() == 150

    #Then Wilhelm Canaris has the following bonuses
    wilhelm_canaris = germany.find_modifier_by_id("Wilhelm_canaris")

    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1.0
    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

    #but the full bonuses should be the same as Wilhelm Canaris is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

def test_wilhelm_canaris_without_fulfilling_having_not_completed_focus_reorganize_secret_services(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

    #When Wilhelm Canaris is hired when Germany has completed focus Reorganize secret services
    germany.create_intelligence_agency("Testing_agency")
    germany.complete_focus("Reorganize_secret_services")
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_canaris", 0)

    assert germany.get_political_power() == 150

    #Then Wilhelm Canaris has the following bonuses
    wilhelm_canaris = germany.find_modifier_by_id("Wilhelm_canaris")

    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1.0
    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

    #but the full bonuses should be the same as Wilhelm Canaris is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

def test_wilhelm_canaris_without_fulfilling_having_not_completed_focus_start_the_proletarian_revolution(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

    #When Wilhelm Canaris is hired when Germany has completed focus Reorganize secret services
    germany.create_intelligence_agency("Testing_agency")
    germany.complete_focus("Start_the_proletarian_revolution")
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_canaris", 0)

    assert germany.get_political_power() == 150

    #Then Wilhelm Canaris has the following bonuses
    wilhelm_canaris = germany.find_modifier_by_id("Wilhelm_canaris")

    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1.0
    assert wilhelm_canaris.get_modifier_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

    #but the full bonuses should be the same as Wilhelm Canaris is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

def test_hans_oster(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.0

    #When Hans Oster is hired when Germany has completed focus Rally the wehrmacht
    germany.complete_focus("Rally_the_wehrmacht")
    germany.add_political_power(150)

    germany.hire_advisor("Hans_oster", 0)

    assert germany.get_political_power() == 0

    #Then Hans Oster has the following bonuses
    hans_oster = germany.find_modifier_by_id("Hans_oster")

    assert hans_oster.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert hans_oster.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05

    #and the full bonuses should be the following since Hans Oster is hired
    assert germany.get_full_stability() == pytest.approx(0.91)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05

def test_hans_oster_without_fulfilling_having_completed_focus_rally_the_wehrmacht(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.0

    #When Hans Oster is hired when Germany has not completed focus Rally the wehrmacht
    germany.add_political_power(150)

    germany.hire_advisor("Hans_oster", 0)

    assert germany.get_political_power() == 150

    #Then Hans Oster has the following bonuses
    hans_oster = germany.find_modifier_by_id("Hans_oster")

    assert hans_oster.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.10
    assert hans_oster.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05

    #but the full bonuses should be the same since Hans Oster is not hired
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.0

def test_alfred_hugenberg_fulfilling_both_requirements(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.0

    #When Alfred Hugenberg is hired when Germany has completed focuses Revive the kaiserreich and Invite german Monarchists
    germany.complete_focus("Revive_the_kaiserreich")
    germany.complete_focus("Invite_german_monarchists")
    germany.add_political_power(150)

    germany.hire_advisor("Alfred_hugenberg", 0)

    assert germany.get_political_power() == 0

    #Then Alfred Hugenberg has the following bonuses
    alfred_hugenberg = germany.find_modifier_by_id("Alfred_hugenberg")

    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.10
    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.10

    #and the full bonuses should be the following since Alfred Hugenberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.10

def test_alfred_hugenberg_fulfilling_having_completed_focus_revive_the_kaiserreich(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.0

    #When Alfred Hugenberg is hired when Germany has completed focus Revive the kaiserreich 
    germany.complete_focus("Revive_the_kaiserreich")
    germany.add_political_power(150)

    germany.hire_advisor("Alfred_hugenberg", 0)

    assert germany.get_political_power() == 0

    #Then Alfred Hugenberg has the following bonuses
    alfred_hugenberg = germany.find_modifier_by_id("Alfred_hugenberg")

    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.10
    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.10

    #and the full bonuses should be the following since Alfred Hugenberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.10

def test_alfred_hugenberg_fulfilling_having_completed_focus_invite_german_monarchists(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.0

    #When Alfred Hugenberg is hired when Germany has completed focus Revive the kaiserreich 
    germany.complete_focus("Invite_german_monarchists")
    germany.add_political_power(150)

    germany.hire_advisor("Alfred_hugenberg", 0)

    assert germany.get_political_power() == 0

    #Then Alfred Hugenberg has the following bonuses
    alfred_hugenberg = germany.find_modifier_by_id("Alfred_hugenberg")

    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.10
    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.10

    #and the full bonuses should be the following since Alfred Hugenberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.10

def test_alfred_hugenberg_without_fulfilling_having_completed_focus_revive_the_kaiserreich_and_invite_german_monachists(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.0

    #When Alfred Hugenberg is hired when Germany has completed focus Revive the kaiserreich 
    germany.add_political_power(150)

    germany.hire_advisor("Alfred_hugenberg", 0)

    assert germany.get_political_power() == 150

    #Then Alfred Hugenberg has the following bonuses
    alfred_hugenberg = germany.find_modifier_by_id("Alfred_hugenberg")

    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.10
    assert alfred_hugenberg.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.10

    #and the full bonuses should be the following since Alfred Hugenberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT] == 0.0


def test_carl_friedrich_goerdeler_fulfilling_having_completed_focus_revive_the_kaiserreich(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0

    #When Carl Friedrich Goerdeler is hired when Germany has completed focus Revive the kaiserreich
    germany.complete_focus("Revive_the_kaiserreich")
    germany.add_political_power(150)

    germany.hire_advisor("Carl_friedrich_goerdeler", 0)

    assert germany.get_political_power() == 0

    #Then Carl Friedrich Goerdeler has the following bonuses
    carl_friedrich_goerdeler = germany.find_modifier_by_id("Carl_friedrich_goerdeler")

    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.15

    #and the full bonuses should be the following since Carl Friedrich Goerdeler is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    #25% * ((1+10%)*(1-12.4%)*(1-5%)) = 0.228855
    assert germany.get_consumer_goods() == 0.228855
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.074
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.15

def test_carl_friedrich_goerdeler_fulfilling_having_completed_focus_invite_german_monarchists(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0

    #When Carl Friedrich Goerdeler is hired when Germany has completed focus Invite german monarchists
    germany.complete_focus("Invite_german_monarchists")
    germany.add_political_power(150)

    germany.hire_advisor("Carl_friedrich_goerdeler", 0)

    assert germany.get_political_power() == 0

    #Then Carl Friedrich Goerdeler has the following bonuses
    carl_friedrich_goerdeler = germany.find_modifier_by_id("Carl_friedrich_goerdeler")

    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.15

    #and the full bonuses should be the following since Carl Friedrich Goerdeler is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    #25% * ((1+10%)*(1-12.4%)*(1-5%)) = 0.228855
    assert germany.get_consumer_goods() == 0.228855
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.074
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.15

def test_carl_friedrich_goerdeler_fulfilling_having_completed_focus_strive_for_conservative_values(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0

    #When Carl Friedrich Goerdeler is hired when Germany has completed focus Strive for conservative values
    germany.complete_focus("Strive_for_conservative_values")
    germany.add_political_power(150)

    germany.hire_advisor("Carl_friedrich_goerdeler", 0)

    assert germany.get_political_power() == 0

    #Then Carl Friedrich Goerdeler has the following bonuses
    carl_friedrich_goerdeler = germany.find_modifier_by_id("Carl_friedrich_goerdeler")

    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.15

    #and the full bonuses should be the following since Carl Friedrich Goerdeler is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    #25% * ((1+10%)*(1-12.4%)*(1-5%)) = 0.228855
    assert germany.get_consumer_goods() == 0.228855
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.074
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.15

def test_carl_friedrich_goerdeler_without_fulfilling_having_completed_either_of_the_three_focuses(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0

    #When Carl Friedrich Goerdeler is hired when Germany has not completed any of the three focuses
    germany.add_political_power(150)

    germany.hire_advisor("Carl_friedrich_goerdeler", 0)

    assert germany.get_political_power() == 150

    #Then Carl Friedrich Goerdeler has the following bonuses
    carl_friedrich_goerdeler = germany.find_modifier_by_id("Carl_friedrich_goerdeler")

    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert carl_friedrich_goerdeler.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.15

    #but the full bonuses should be the same since Carl Friedrich Goerdeler is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR] == 0.0

def test_julius_leber(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0

    #When Julius Leber is hired when Germany has completed focus Re-establish free elections
    germany.complete_focus("Reestablish_free_elections")
    germany.add_political_power(150)

    germany.hire_advisor("Julius_leber", 0)

    assert germany.get_political_power() == 0

    #Then Julius Leber has the following bonuses
    julius_leber = germany.find_modifier_by_id("Julius_leber")

    assert julius_leber.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert julius_leber.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.05
    assert julius_leber.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15

    #and the full bonuses should be the following since Julius Leber is hired
    #Extra 0.01 from 5% more stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.122)
    assert germany.get_full_stability() == 0.86
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15

def test_julius_leber_without_fulfilling_having_completed_focus_reestablish_free_elections(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0

    #When Julius Leber is hired when Germany has not completed focus Re-establish free elections
    germany.add_political_power(150)

    germany.hire_advisor("Julius_leber", 0)

    assert germany.get_political_power() == 150

    #Then Julius Leber has the following bonuses
    julius_leber = germany.find_modifier_by_id("Julius_leber")

    assert julius_leber.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert julius_leber.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.05
    assert julius_leber.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15

    #and the full bonuses should be the same as Julius Leber is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0

def test_kurt_schumacher(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.0

    #When Kurt Schumacher is hired when Germany has completed focus Re-establish free elections
    germany.complete_focus("Reestablish_free_elections")
    germany.add_political_power(150)

    germany.hire_advisor("Kurt_schumacher", 0)

    assert germany.get_political_power() == 0

    #Then Kurt Schumacher has the following bonuses
    kurt_schumacher = germany.find_modifier_by_id("Kurt_schumacher")

    assert kurt_schumacher.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.10

    #and the full bonuses should be the following since Kurt Schumacher is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.10

def test_kurt_schumacher_without_fulfilling_having_completed_focus_reestablish_free_elections(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.0

    #When Kurt Schumacher is hired when Germany has not completed focus Re-establish free elections
    germany.add_political_power(150)

    germany.hire_advisor("Kurt_schumacher", 0)

    assert germany.get_political_power() == 150

    #Then Kurt Schumacher has the following bonuses
    kurt_schumacher = germany.find_modifier_by_id("Kurt_schumacher")

    assert kurt_schumacher.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.10

    #but the full bonuses should be the same since Kurt Schumacher is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.0

def test_theodor_heuss(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.0

    #When Theodor Heuss is hired when Germany has completed focus Monarchist sentiment
    germany.complete_focus("Monarchist_sentiment")
    germany.add_political_power(150)

    germany.hire_advisor("Theodor_heuss", 0)

    assert germany.get_political_power() == 0

    #Then Theodor Heuss has the following bonuses
    theodor_heuss = germany.find_modifier_by_id("Theodor_heuss")

    assert theodor_heuss.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert theodor_heuss.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.05

    #and the full bonuses should be the following since Theodor Heuss is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.05

def test_theodor_heuss_without_fulfilling_having_completed_focus_monarchist_sentiment(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.0

    #When Theodor Heuss is hired when Germany has not completed focus Monarchist sentiment
    germany.add_political_power(150)

    germany.hire_advisor("Theodor_heuss", 0)

    assert germany.get_political_power() == 150

    #Then Theodor Heuss has the following bonuses
    theodor_heuss = germany.find_modifier_by_id("Theodor_heuss")

    assert theodor_heuss.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert theodor_heuss.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.05

    #but the full bonuses should be the samr since Theodor Heuss is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT] == 0.0

def test_hans_luther(germany, new_game):
    #Given a normal Germany game
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

    #When Hans Luther is hired when Germany is not fascist
    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)
    germany.add_political_power(150)

    germany.hire_advisor("Hans_luther", 0)

    assert germany.get_political_power() == 0

    #Then Hans Luther has the following bonuses
    hans_luther = germany.find_modifier_by_id("Hans_luther")

    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

    #and the full bonuses should be the following since Hans Luther is hired
    #25 * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.124
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

def test_hans_luther_without_fulfilling_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

    #When Hans Luther is hired when Germany is fascist
    germany.add_political_power(150)

    germany.hire_advisor("Hans_luther", 0)

    assert germany.get_political_power() == 150

    #Then Hans Luther has the following bonuses
    hans_luther = germany.find_modifier_by_id("Hans_luther")

    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

    #but the full bonuses should be the same since Hans Luther is not hired
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

def test_ludwig_erhard(germany, new_game):
    #Given a normal Germany game
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.0

    #When Ludwig Erhard is hired when Germany has completed focus Prioritize economic growth and Walther Funk is not hired
    germany.complete_focus("Prioritize_economic_growth")
    germany.add_political_power(150)

    germany.hire_advisor("Ludwig_erhard", 0)

    assert germany.get_political_power() == 0

    #Then Ludwig Erhard has the following bonuses
    ludwig_erhard = germany.find_modifier_by_id("Ludwig_erhard")

    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.15
    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.33
    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.33

    #and the full bonuses should be the following since Ludwig Erhard is hired
    #25% * ((1+10%)*(1-12.4%)*(1-15%)) = 0.204765
    assert germany.get_consumer_goods() == 0.204765
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.33
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.33

def test_ludwig_erhard_without_fulfilling_having_completed_focus_prioritize_economic_growth(germany, new_game):
    #Given a normal Germany game
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.0

    #When Ludwig Erhard is hired when Germany has not completed focus Prioritize economic growth and Walther Funk is hired
    germany.add_political_power(300)
    germany.hire_advisor("Walther_funk", 0)

    germany.hire_advisor("Ludwig_erhard", 0)

    assert germany.get_political_power() == 150

    #Then Ludwig Erhard has the following bonuses
    ludwig_erhard = germany.find_modifier_by_id("Ludwig_erhard")

    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.15
    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.33
    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.33

    #but the full bonuses should be the same since Ludwig Erhard is not hired(except consumer goods, since -10% is gotten from Walther Funk)
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.124
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.0

def test_ludwig_erhard_without_fulfilling_having_hired_walther_funk(germany, new_game):
    #Given a normal Germany game
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.0

    #When Ludwig Erhard is hired when Germany has completed focus Prioritize economic growth but not hired Walther Funk
    germany.add_political_power(150)
    germany.hire_advisor("Ludwig_erhard", 0)

    assert germany.get_political_power() == 150

    #Then Ludwig Erhard has the following bonuses
    ludwig_erhard = germany.find_modifier_by_id("Ludwig_erhard")

    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.15
    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == -0.33
    assert ludwig_erhard.get_modifier_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == -0.33

    #but the full bonuses should be the same since Ludwig Erhard is not hired
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST] == 0.0

def test_hermann_ehrhardt(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.0

    #When Hermann Ehrhardt is hired when Germany his non-aligned and has completed focus Reestablish the freikorps
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)
    germany.complete_focus("Reestablish_the_freikorps")
    germany.add_political_power(150)

    germany.hire_advisor("Hermann_ehrhardt", 0)

    assert germany.get_political_power() == 0

    #Then Hermann Ehrhardt has the following bonuses
    hermann_ehrhardt = germany.find_modifier_by_id("Hermann_ehrhardt")

    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.03
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.05
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.05
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.05

    #and the full bonuses should be the following since Hermann Ehrhardt is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.05

def test_hermann_ehrhardt_without_fulfilling_being_non_aligned(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.0

    #When Hermann Ehrhardt is hired when Germany his not non-aligned and has completed focus Reestablish the freikorps
    germany.complete_focus("Reestablish_the_freikorps")
    germany.add_political_power(150)

    germany.hire_advisor("Hermann_ehrhardt", 0)

    assert germany.get_political_power() == 150

    #Then Hermann Ehrhardt has the following bonuses
    hermann_ehrhardt = germany.find_modifier_by_id("Hermann_ehrhardt")

    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.03
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.05
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.05
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.05

    #but the full bonuses should be the same since Hermann Ehrhardt is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.0

def test_hermann_ehrhardt_without_fulfilling_having_completed_focus_reestablish_the_freikorps(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.0

    #When Hermann Ehrhardt is hired when Germany is non-aligned but has not completed focus Reestablish the freikorps
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)
    germany.add_political_power(150)

    germany.hire_advisor("Hermann_ehrhardt", 0)

    assert germany.get_political_power() == 150

    #Then Hermann Ehrhardt has the following bonuses
    hermann_ehrhardt = germany.find_modifier_by_id("Hermann_ehrhardt")

    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.03
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.15
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.05
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.05
    assert hermann_ehrhardt.get_modifier_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.05

    #but the full bonuses should be the same since Hermann Ehrhardt is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ATTACK] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_DEFENSE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MILITIA_ORGANIZATION] == 0.0

def test_adolf_friedrich_of_mecklenburg_while_fulfilling_being_non_aligned(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == 0.0

    #When Adolf Friedrich is hired when Germany is non aligned
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)
    germany.add_political_power(150)

    germany.hire_advisor("Adolf_friedrich_of_mecklenburg", 0)

    assert germany.get_political_power() == 0

    #Then Adolf Friedrich has the following bonuses
    adolf_friedrich_of_mecklenburg = germany.find_modifier_by_id("Adolf_friedrich_of_mecklenburg")

    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.02
    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == -0.10

    #and the full bonuses should be the following since Adolf Freidrich is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == -0.10

def test_adolf_friedrich_of_mecklenburg_while_fulfilling_being_democratic(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == 0.0

    #When Adolf Friedrich is hired when Germany is democratic
    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)
    germany.add_political_power(150)

    germany.hire_advisor("Adolf_friedrich_of_mecklenburg", 0)

    assert germany.get_political_power() == 0

    #Then Adolf Friedrich has the following bonuses
    adolf_friedrich_of_mecklenburg = germany.find_modifier_by_id("Adolf_friedrich_of_mecklenburg")

    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.02
    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == -0.10

    #and the full bonuses should be the following since Adolf Freidrich is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == -0.10

def test_adolf_friedrich_of_mecklenburg_without_fulfilling_being_non_aligned_or_democratic(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == 0.0

    #When Adolf Friedrich is hired when Germany is neither non-aligned or democratic
    germany.add_political_power(150)

    germany.hire_advisor("Adolf_friedrich_of_mecklenburg", 0)

    assert germany.get_political_power() == 150

    #Then Adolf Friedrich has the following bonuses
    adolf_friedrich_of_mecklenburg = germany.find_modifier_by_id("Adolf_friedrich_of_mecklenburg")

    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.02
    assert adolf_friedrich_of_mecklenburg.get_modifier_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == -0.10

    #but the full bonuses should be the same since Adolf Freidrich is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_CORE_MANPOWER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE] == 0.0

def test_wilhelm_von_gayl(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0

    #When Vilhelm von Gayl is hired when Germany has completed focus Monarchist sentiment
    germany.complete_focus("Monarchist_sentiment")
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_von_gayl", 0)

    assert germany.get_political_power() == 0

    #Then Vilhelm von Gayl has the following bonuses
    vilhelm_von_gayl = germany.find_modifier_by_id("Wilhelm_von_gayl")

    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0010
 
    #and the full bonuses should be the following since Vilhelm von Gayl is hired
    #0.01 extra from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.122)
    assert germany.get_full_stability() == 0.86
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0010

def test_wilhelm_von_gayl_without_fulfilling_having_completed_focus_monarchist_sentiment(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0

    #When Vilhelm von Gayl is hired when Germany has not completed focus Monarchist sentiment
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_von_gayl", 0)

    assert germany.get_political_power() == 150

    #Then Vilhelm von Gayl has the following bonuses
    vilhelm_von_gayl = germany.find_modifier_by_id("Wilhelm_von_gayl")

    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.05
    assert vilhelm_von_gayl.get_modifier_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0010
 
    #but the full bonuses should be the samr since Vilhelm von Gayl is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_stability() == pytest.approx(0.81)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES] == 0.0

def test_andreas_hermes(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MONTHLY_POPULATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174

    #When Andreas Hermes is hired when Germany has completed focus Monarchist sentiment
    germany.complete_focus("Monarchist_sentiment")
    germany.add_political_power(150)

    germany.hire_advisor("Andreas_hermes", 0)

    assert germany.get_political_power() == 0

    #Then Andreas Hermes has the following bonuses
    andreas_hermes = germany.find_modifier_by_id("Andreas_hermes")

    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.MONTHLY_POPULATION] == 0.10
    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES] == -0.10
    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.05
    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.05
 
    #and the full bonuses should be the following since Andreas Hermes is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MONTHLY_POPULATION] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.224)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.224)

def test_andreas_hermes_without_fulfilling_having_completed_focus_monarchist_sentiment(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MONTHLY_POPULATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174

    #When Andreas Hermes is hired when Germany has not completed focus Monarchist sentiment
    germany.add_political_power(150)

    germany.hire_advisor("Andreas_hermes", 0)

    assert germany.get_political_power() == 150

    #Then Andreas Hermes has the following bonuses
    andreas_hermes = germany.find_modifier_by_id("Andreas_hermes")

    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.MONTHLY_POPULATION] == 0.10
    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES] == -0.10
    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.05
    assert andreas_hermes.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.05
 
    #but the full bonuses should be the same since Andreas Hermes is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MONTHLY_POPULATION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174

def test_dietrich_bonhoeffer_while_fulfilling_being_non_aligned(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0

    #When Dietrich Bonhoeffer is hired when Germany is non-aligned
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)
    germany.add_political_power(150)

    germany.hire_advisor("Dietrich_bonhoeffer", 0)

    assert germany.get_political_power() == 0

    #Then Dietrich Bonhoeffer has the following bonuses
    dietrich_bonhoeffer = germany.find_modifier_by_id("Dietrich_bonhoeffer")

    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.03
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == -0.03
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -25
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50
 
    #and the full bonuses should be the following since Dietrich Bonhoeffer is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == -0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50


def test_dietrich_bonhoeffer_while_fulfilling_being_democratic(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0

    #When Dietrich Bonhoeffer is hired when Germany is democratic
    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)
    germany.add_political_power(150)

    germany.hire_advisor("Dietrich_bonhoeffer", 0)

    assert germany.get_political_power() == 0

    #Then Dietrich Bonhoeffer has the following bonuses
    dietrich_bonhoeffer = germany.find_modifier_by_id("Dietrich_bonhoeffer")

    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.03
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == -0.03
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -25
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50
 
    #and the full bonuses should be the following since Dietrich Bonhoeffer is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == -0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50

def test_dietrich_bonhoeffer_without_fulfilling_being_non_aligned_or_democratic(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0

    #When Dietrich Bonhoeffer is hired when Germany not non_aligned or democratic
    germany.add_political_power(150)

    germany.hire_advisor("Dietrich_bonhoeffer", 0)

    assert germany.get_political_power() == 150

    #Then Dietrich Bonhoeffer has the following bonuses
    dietrich_bonhoeffer = germany.find_modifier_by_id("Dietrich_bonhoeffer")

    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.10
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == -0.03
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == -0.03
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == -25
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == -0.05
    assert dietrich_bonhoeffer.get_modifier_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY] == -50
 
    #but the full bonuses should be the same since Dietrich Bonhoeffer is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY] == 0

def test_ernst_thälmann(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Ernst Thälmann is hired when Ernst Thällmann has been freed from prison and is not the leader of Germany
    germany.activate_event("Ernst_thalmann_has_been_freed_from_prison")
    germany.add_political_power(150)

    germany.hire_advisor("Ernst_thalmann_a", 0)

    assert germany.get_political_power() == 0

    #Then Ernst Thälmann has the following bonuses
    ernst_thalmann = germany.find_modifier_by_id("Ernst_thalmann_a")

    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10

    #and the full bonuses should be the following since Ernst Thälmann is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10

def test_ernst_thälmann_without_fulfilling_having_been_free_from_prison(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Ernst Thälmann is hired when Ernst Thällmann has not been freed from prison and is not the leader of Germany
    germany.add_political_power(150)

    germany.hire_advisor("Ernst_thalmann_a", 0)

    assert germany.get_political_power() == 150

    #Then Ernst Thälmann has the following bonuses
    ernst_thalmann = germany.find_modifier_by_id("Ernst_thalmann_a")

    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10

    #and the full bonuses should be the same since Ernst Thälmann is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

def test_ernst_thälmann_without_fulfilling_not_having_ernst_as_country_leader(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Ernst Thälmann is hired when Ernst Thällmann has been freed from prison and is the leader of Germany
    germany.activate_event("Ernst_thalmann_has_been_freed_from_prison")
    germany.switch_leader("Ernst_thalmann_l")
    germany.add_political_power(150)

    germany.hire_advisor("Ernst_thalmann_a", 0)

    assert germany.get_political_power() == 150

    #Then Ernst Thälmann has the following bonuses
    ernst_thalmann = germany.find_modifier_by_id("Ernst_thalmann_a")

    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10

    #and the full bonuses should be the same since Ernst Thälmann is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

def test_walter_ulbricht(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Walter Ulbricht is hired when Walter Ulbricht is not country leader, is communist, has completed focus Start the proletarian revolution and has not completed focus Revive the kaiserreich
    germany.complete_focus("Start_the_proletarian_revolution")
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(150)

    germany.hire_advisor("Walter_ulbricht_a", 0)

    assert germany.get_political_power() == 0

    #Then Walter Ulbricht has the following bonuses
    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_a")

    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

    #and the full bonuses should be the following since Walter Ulbricht is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

def test_walter_ulbricht_without_fulfilling_walter_not_being_country_leader(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Walter Ulbricht is hired when he is country leader
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.switch_leader("Walter_ulbricht_l")
    germany.add_political_power(150)

    germany.hire_advisor("Walter_ulbricht_a", 0)

    assert germany.get_political_power() == 150

    #Then Walter Ulbricht has the following bonuses
    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_a")

    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

    #but the full bonuses should be the samr since Walter Ulbricht is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

def test_walter_ulbricht_without_fulfilling_having_completed_focus_start_the_proletarian_revolution_and_being_communist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Walter Ulbricht is hired when Germany is not communist and has not completed focus Start the proletarian revolution
    germany.add_political_power(150)

    germany.hire_advisor("Walter_ulbricht_a", 0)

    assert germany.get_political_power() == 150

    #Then Walter Ulbricht has the following bonuses
    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_a")

    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

    #but the full bonuses should be the samr since Walter Ulbricht is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

def test_walter_ulbricht_without_fulfilling_having_not_completed_focus_revive_the_kaiserreich(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Walter Ulbricht is hired when Germany has completed focus Revive the kaiserreich
    germany.complete_focus("Revive_the_kaiserreich")
    germany.add_political_power(150)

    germany.hire_advisor("Walter_ulbricht_a", 0)

    assert germany.get_political_power() == 150

    #Then Walter Ulbricht has the following bonuses
    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_a")

    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

    #but the full bonuses should be the samr since Walter Ulbricht is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

def test_wilhelm_zaisser(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

    #When Wilhelm Zaisser is hired when Germany has completed focus Formalize the intelligence wing
    germany.complete_focus("Formalize_the_intelligence_wing")
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_zaisser", 0)

    assert germany.get_political_power() == 0

    #Then Wilhelm Zaisser has the following bonuses
    wilhelm_zaisser = germany.find_modifier_by_id("Wilhelm_zaisser")

    assert wilhelm_zaisser.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert wilhelm_zaisser.get_modifier_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

    #and the full bonuses should be the following since Wilhelm Zaisser is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

def test_wilhelm_zaisser_without_fulfilling_having_completed_focus_formalize_the_intelligence_wing(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

    #When Wilhelm Zaisser is hired when Germany has not completed focus Formalize the intelligence wing
    germany.add_political_power(150)

    germany.hire_advisor("Wilhelm_zaisser", 0)

    assert germany.get_political_power() == 150

    #Then Wilhelm Zaisser has the following bonuses
    wilhelm_zaisser = germany.find_modifier_by_id("Wilhelm_zaisser")

    assert wilhelm_zaisser.get_modifier_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 1
    assert wilhelm_zaisser.get_modifier_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == -0.20

    #but the full bonuses should be the same since Wilhelm Zaisser is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AGENCY_UPGRADE_TIME] == 0.0

def test_otto_rühle(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Otto Rühle is hired when Germany has completed focus Legacy of the spartacus league
    germany.complete_focus("Legacy_of_the_spartacus_league")
    germany.add_political_power(150)

    germany.hire_advisor("Otto_ruhle", 0)

    assert germany.get_political_power() == 0

    #Then Otto Rühle has the following bonuses
    otto_ruhle = germany.find_modifier_by_id("Otto_ruhle")

    assert otto_ruhle.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert otto_ruhle.get_modifier_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.05
    assert otto_ruhle.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

    #and the full bonuses should be the following since Otto Rühle is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == pytest.approx(0.06)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

def test_otto_rühle_without_fulfilling_having_completed_focus_legacy_of_the_spartacus_league(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Otto Rühle is hired when Germany has not completed focus Legacy of the spartacus league
    germany.add_political_power(150)

    germany.hire_advisor("Otto_ruhle", 0)

    assert germany.get_political_power() == 150

    #Then Otto Rühle has the following bonuses
    otto_ruhle = germany.find_modifier_by_id("Otto_ruhle")

    assert otto_ruhle.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert otto_ruhle.get_modifier_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.05
    assert otto_ruhle.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

    #but the full bonuses should be the same since Otto Rühle is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

def test_hermann_duncker(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN] == 0.0

    #When Hermann Duncker is hired when Germany is communist
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(150)

    germany.hire_advisor("Hermann_duncker", 0)

    assert germany.get_political_power() == 0

    #Then Hermann Duncker has the following bonuses
    hermann_duncker = germany.find_modifier_by_id("Hermann_duncker")

    assert hermann_duncker.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.05
    assert hermann_duncker.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.05
    assert hermann_duncker.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN] == 0.05

    #and the full bonuses should be the following since Hermann Duncker is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN] == 0.05

def test_hermann_duncker_without_fulfilling_being_communist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN] == 0.0

    #When Hermann Duncker is hired when Germany is not communist
    germany.add_political_power(150)

    germany.hire_advisor("Hermann_duncker", 0)

    assert germany.get_political_power() == 150

    #Then Hermann Duncker has the following bonuses
    hermann_duncker = germany.find_modifier_by_id("Hermann_duncker")

    assert hermann_duncker.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.05
    assert hermann_duncker.get_modifier_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.05
    assert hermann_duncker.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN] == 0.05

    #but the full bonuses should be the same since Hermann Duncker is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN] == 0.0
    
def test_august_thalheimer(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174

    #When August Thalheimer is hired when Germany is communist
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(150)

    germany.hire_advisor("August_thalheimer", 0)

    assert germany.get_political_power() == 0

    #Then August Thalheimer has the following bonuses
    august_thalheimer = germany.find_modifier_by_id("August_thalheimer")

    assert august_thalheimer.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert august_thalheimer.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert august_thalheimer.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.05

    #and the full bonuses should be the following since August Thalheimer is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.224)

def test_august_thalheimer_without_fulfilling_being_communist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174

    #When August Thalheimer is hired when Germany is not communist
    germany.add_political_power(150)

    germany.hire_advisor("August_thalheimer", 0)

    assert germany.get_political_power() == 150

    #Then August Thalheimer has the following bonuses
    august_thalheimer = germany.find_modifier_by_id("August_thalheimer")

    assert august_thalheimer.get_modifier_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.05
    assert august_thalheimer.get_modifier_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == -0.05
    assert august_thalheimer.get_modifier_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.05

    #but the full bonuses should be the samr since August Thalheimer is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174

def test_bernhard_bastlein(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0

    #When Bernhard Bästlein is hired when Germany has completed focus Start the proletarian revolution
    germany.complete_focus("Start_the_proletarian_revolution")
    germany.add_political_power(150)

    germany.hire_advisor("Bernhard_bastlein", 0)

    assert germany.get_political_power() == 0

    #Then Bernhard Bästlein has the following bonuses
    bernhard_bastlein = germany.find_modifier_by_id("Bernhard_bastlein")

    assert bernhard_bastlein.get_modifier_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.05
    assert bernhard_bastlein.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.05

    #and the full bonuses should be the following since Bernhard Bästlein is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.05

def test_bernhard_bastlein_without_fulfilling_having_completed_focus_start_the_proletarian_revolution(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0

    #When Bernhard Bästlein is hired when Germany has not completed focus Start the proletarian revolution
    germany.add_political_power(150)

    germany.hire_advisor("Bernhard_bastlein", 0)

    assert germany.get_political_power() == 150

    #Then Bernhard Bästlein has the following bonuses
    bernhard_bastlein = germany.find_modifier_by_id("Bernhard_bastlein")

    assert bernhard_bastlein.get_modifier_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.05
    assert bernhard_bastlein.get_modifier_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.05

    #but the full bonuses should be the samr since Bernhard Bästlein is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0

def test_having_three_advisors(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    germany.get_consumer_goods() == 0.2409
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

    #When Ernst Thälmann, Walter Ulbricht and Hans Luther are hired as advisors when Germany is communist and Ernst Thälmann has been freed from prison
    germany.activate_event("Ernst_thalmann_has_been_freed_from_prison")
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(450)

    germany.hire_advisor("Ernst_thalmann_a", 0)
    germany.hire_advisor("Walter_ulbricht_a", 1)
    germany.hire_advisor("Hans_luther", 2)

    ernst_thalmann = germany.find_modifier_by_id("Ernst_thalmann_a")
    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_a")
    hans_luther = germany.find_modifier_by_id("Hans_luther")

    germany.get_political_power() == 0

    #Then they have bonuses
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

    #and Germany has the following bonuses, since all 3 advisors are hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.212)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == pytest.approx(0.15)
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681
    germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.124
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

def test_replacing_an_advisor(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0

    #When Ernst Thälmann is hired while Germany is communist and Ernst has been freed from prison
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.activate_event("Ernst_thalmann_has_been_freed_from_prison")

    germany.add_political_power(300)

    germany.hire_advisor("Ernst_thalmann_a", 0)

    assert germany.get_political_power() == 150

    ernst_thalmann = germany.find_modifier_by_id("Ernst_thalmann_a")

    #Then Ernst Thälmann has the following bonuses
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10

    #and Germany has the following bonuses
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.112
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10

    #When Ernst Thälmann is swapped with Walter Ulbricht
    germany.hire_advisor("Walter_ulbricht_a", 0)

    assert germany.get_political_power() == 0

    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_a")

    #Then Walter Ulbricht has the following bonuses
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

    #and Germany has the following bonuses
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05

def test_replacing_an_advisor_while_having_three_advisors(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.0
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    germany.get_consumer_goods() == 0.2409
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Ernst Thälmann, Walter Ulbricht and Hans Luther are hired as advisors when Germany is communist and Ernst Thälmann has been freed from prison
    germany.activate_event("Ernst_thalmann_has_been_freed_from_prison")
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(600)

    germany.hire_advisor("Ernst_thalmann_a", 0)
    germany.hire_advisor("Walter_ulbricht_a", 1)
    germany.hire_advisor("Hans_luther", 2)

    ernst_thalmann = germany.find_modifier_by_id("Ernst_thalmann_a")
    walter_ulbricht = germany.find_modifier_by_id("Walter_ulbricht_a")
    hans_luther = germany.find_modifier_by_id("Hans_luther")

    germany.get_political_power() == 150

    #Then they have bonuses
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.05
    assert ernst_thalmann.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert walter_ulbricht.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == 0.05
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert hans_luther.get_modifier_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

    #and Germany has the following bonuses, since all 3 advisors are hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.212)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == pytest.approx(0.15)
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681
    germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.124
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Ernst Thälmann is replaced with Hjalmar Schacht when ideology is fascist
    germany.change_ideology(ideologies.Ideologies.FASCIST)
    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 75

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #and Germany has the following bonuses
    #25% * ((1+10%)*(1-12.4%)*(1-10%)*(1-10%)) = 0.195129
    assert germany.get_consumer_goods() == pytest.approx(0.195129)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.224
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.20

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.162)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT] == pytest.approx(0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.10

def test_one_cannot_hire_advisors_with_illegal_slot(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

    #When Hjalmar Schacht is hired in the fourth slot
    germany.add_political_power(150)

    germany.hire_advisor("Hjalmar_schacht", 3)

    assert germany.get_political_power() == 150

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #But Germany has the same bonuses as before, because the slot is illegal
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    germany.get_consumer_goods() == 0.2409
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

def test_another_country_cannot_hire_german_advisor(germany, new_game): 
    #Given a testing country that is not Germany
    testing_country = create_custom_country(new_game)

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == 0.0

    #When testing country hires Reinhard Heydrich while being fascist
    testing_country.add_political_power(150)

    testing_country.hire_advisor("Reinhard_heydrich", 0)

    #Then he should not be hired
    assert testing_country.get_political_power() == 150

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_GROWTH_SPEED] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.OPERATIVE_SLOTS] == 0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS] == 0.0








def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)

def get_advisor(country, name): 
    return country.get_possible_advisors()[name]
