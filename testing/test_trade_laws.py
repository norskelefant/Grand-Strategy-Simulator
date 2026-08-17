import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, trade_laws, custom_country, requirements

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_germany_has_limited_exports_by_default(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When asking for the trade law of germany
    trade_law = germany.get_trade_law()

    #Then the trade law should be limited export
    assert trade_law.get_id() == "Limited_exports"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.25
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.01
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.05

    #and Germany has the following bonuses because it has trade law Limited Exports
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

def test_can_switch_to_free_trade(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When switching the trade law to free trade
    germany.add_political_power(150)

    assert germany.get_political_power() == 150
    assert requirements.can_switch_to_free_trade(germany) == True

    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    trade_law = germany.get_trade_law()

    #Then the trade law should be free trade
    assert trade_law.get_id() == "Free_trade"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.80
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.15
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.15
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.15
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.40
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.20
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER) == 0.05

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because Free Trade is the trade law
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.80
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.274)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.274)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == pytest.approx(0.15)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER] == 0.05

def test_can_switch_to_export_focus(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When switching the trade law to export focus
    germany.add_political_power(150)

    assert germany.get_political_power() == 150
    assert requirements.can_switch_to_export_focus(germany) == True
     
    germany.switch_trade_law(trade_laws.Trade_laws.EXPORT_FOCUS)

    trade_law = germany.get_trade_law()

    #Then the trade law should be export focus
    assert trade_law.get_id() == "Export_focus"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.50
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.20
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER) == 0.10

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the trade law is Export Focus
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.224)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.224)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER] == 0.10

def test_can_switch_to_limited_exports_if_germany_is_fascist_and_has_partial_mobilization_as_the_economy_law(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When switching the trade law to limited exports while being fascist and having partial mobilization as the economy law
    germany.add_political_power(300)

    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    assert germany.get_political_power() == 150
    assert germany.get_economy_law().get_id() == "Partial_mobilization"
    assert germany.get_ideology() == ideologies.Ideologies.FASCIST
    assert requirements.can_switch_to_limited_exports(germany) == True 
     
    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should be limited exports
    assert trade_law.get_id() == "Limited_exports"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.25
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.01
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.05

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the trade law is Limited Exports
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

def test_can_switch_to_closed_economy_if_germany_is_at_war_and_is_fascist_and_has_economy_law_war_economy(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When switching the trade law to closed economy while prerequisites are fulfilled
    germany.add_political_power(300)

    testing_country = create_custom_country(new_game)

    germany.declare_war(testing_country)

    germany.add_base_war_support(0.16)

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    assert germany.get_full_war_support() == pytest.approx(0.51)
    assert germany.get_is_at_war() == True
    assert germany.get_ideology() == ideologies.Ideologies.FASCIST
    assert economy_law.get_id() == "War_economy"
    assert germany.get_political_power() == 150

    assert requirements.can_switch_to_closed_economy(germany) == True

    germany.switch_trade_law(trade_laws.Trade_laws.CLOSED_ECONOMY)
     
    trade_law = germany.get_trade_law()

    #Then the trade law should be Closed Economy
    assert trade_law.get_id() == "Closed_economy"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.0
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.10

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the trade law is Closed Economy
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.124)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.124)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.10

def test_can_switch_to_limited_exports_if_germany_is_democratic_and_at_war_and_enemy_country_has_20_percent_of_germanys_factories(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When switching the trade law to limited exports
    germany.add_political_power(300)

    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    assert germany.get_political_power() == 150

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    assert requirements.can_switch_to_limited_exports(germany) == False

    #Quick extra test for not being able to switch to limited export while being democratic and not being at war: 
    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    assert trade_law.get_id() == "Free_trade"
    assert germany.get_political_power() == 150

    testing_country = create_custom_country(new_game)

    germany.declare_war(testing_country)

    assert germany.get_is_at_war() == True
    assert testing_country.get_total_factories() > (0.20 * germany.get_total_factories())
    assert requirements.can_switch_to_limited_exports(germany) == True

    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should be limited exports
    assert trade_law.get_id() == "Limited_exports"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.25
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.01
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.05

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the trade law is Limited Exports
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

def test_cannot_switch_trade_law_if_not_enough_political_power(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    assert requirements.can_switch_to_free_trade(germany) == True

    #When switching trade law without political power
    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    #When asking for the trade law of germany
    trade_law = germany.get_trade_law()

    #Then the trade law should remain limited exports
    assert trade_law.get_id() == "Limited_exports"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.25
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.01
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.05

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the trade law is Limited Exports
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

def test_cannot_switch_to_limited_exports_if_germany_is_fascist_and_has_economy_law_civilian_economy(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When switching trade law to limited exports without fulfilling the requirements(which is not having partial mobilization)
    germany.add_political_power(450)

    germany.switch_economy_law(economy_laws.Economy_laws.CIVILIAN_ECONOMY)

    assert germany.get_political_power() == 300

    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    assert germany.get_political_power() == 150

    assert requirements.can_switch_to_limited_exports(germany) == False

    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should remain free trade
    assert trade_law.get_id() == "Free_trade"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.80
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.15
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.15
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.15
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.40
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.20
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER) == 0.05

    assert germany.get_political_power() == 150

    #and Germany has the following bonuses since the trade law is Free Trade
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.80
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.274)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.274)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == pytest.approx(0.15)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER] == 0.05

def test_cannot_switch_to_closed_economy_if_germany_is_not_at_war(germany, new_game):
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When switching trade law to closed economy without fulfilling the criteria
    germany.add_political_power(150)

    assert requirements.can_switch_to_closed_economy(germany) == False

    germany.switch_trade_law(trade_laws.Trade_laws.CLOSED_ECONOMY)

    assert germany.get_political_power() == 150

    trade_law = germany.get_trade_law()

    #Then the trade law should remain limited exports
    assert trade_law.get_id() == "Limited_exports"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.25
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.01
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.05

    assert germany.get_political_power() == 150

    #and Germany should have the following bonuses because Limited Exports is the trade law
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

def test_germany_will_keep_limited_exports_even_if_criteria_is_no_longer_fulfilled(germany, new_game): 
    #Given Germany start
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    #When Germany no longer has the criteria for switching to limited exports
    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    germany.add_political_power(150)

    assert requirements.can_switch_to_limited_exports(germany) == False

    #Then when switching to limited exports
    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should remain limited exports
    assert trade_law.get_id() == "Limited_exports"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.25
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.01
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.05

    assert germany.get_political_power() == 150

    #and Germany has the following bonuses because the trade law is Limited Exports
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05
























def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)