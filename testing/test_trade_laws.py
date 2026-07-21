import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, trade_laws

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

    #When asking for the trade law of germany
    trade_law = germany.get_trade_law()

    #Then the trade law should be limited export
    assert trade_law.get_name() == "Limited_exports"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.25
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.DOCKYARD_OUTPUT) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESEARCH_SPEED) == 0.01
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS) == 0.10
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS) == 0.05
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.05

def test_can_switch_to_free_trade(germany, new_game): 
    #Given Germany start

    #When switching the trade law to free trade
    germany.add_political_power(150)

    assert germany.get_political_power() == 150
     
    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    trade_law = germany.get_trade_law()

    #Then the trade law should be free trade
    assert trade_law.get_name() == "Free_trade"
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


def test_can_switch_to_export_focus(germany, new_game): 
    #Given Germany start

    #When switching the trade law to export focus
    germany.add_political_power(150)

    assert germany.get_political_power() == 150
     
    germany.switch_trade_law(trade_laws.Trade_laws.EXPORT_FOCUS)

    trade_law = germany.get_trade_law()

    #Then the trade law should be export focus
    assert trade_law.get_name() == "Export_focus"
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

def test_can_switch_to_limited_exports_if_requirements_are_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the trade law to limited exports(which Germany can do, as it it not democratic and starts with partial mobilization)
    germany.add_political_power(300)

    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    assert germany.get_political_power() == 150
     
    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should be limited exports
    assert trade_law.get_name() == "Limited_exports"
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

def test_can_switch_to_closed_economy_if_requirements_are_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the trade law to closed economy while prerequisites are fulfilled
    germany.add_political_power(300)

    testing_country = create_custom_country()

    germany.declare_war(testing_country)

    germany.add_base_war_support(16)

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    assert germany.get_political_power() == 150
    assert germany.get_is_at_war() == True
    assert germany.get_full_war_support() == 51

    germany.switch_trade_law(trade_laws.Trade_laws.CLOSED_ECONOMY)
     
    trade_law = germany.get_trade_law()

    #Then the trade law should be limited exports
    assert trade_law.get_name() == "Closed_economy"
    assert trade_law.get_end_date() == None
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RESOURCES_TO_MARKET) == 0.0
    assert trade_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST) == -0.10

    assert germany.get_political_power() == 0

def test_can_switch_to_limited_exports_if_requirements_are_fulfilled_two(germany, new_game): 
    #Given Germany start

    #When switching the trade law to limited exports
    germany.add_political_power(300)

    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    assert germany.get_political_power() == 150

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    #Quick extra test for not being able to switch to limited export while being democratic and not being at war: 
    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    assert trade_law.get_name() == "Free_trade"
    assert germany.get_political_power() == 150

     

    testing_country = create_custom_country()

    germany.set_at_war(True)

    germany.declare_war(testing_country)

    assert germany.get_is_at_war() == True
    assert testing_country.get_total_factories() > (0.20 * germany.get_total_factories())

    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should be limited exports
    assert trade_law.get_name() == "Limited_exports"
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

def test_cannot_switch_trade_law_if_not_enough_political_power(germany, new_game): 
    #Given Germany start

    #When switching trade law without political power
    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    #When asking for the trade law of germany
    trade_law = germany.get_trade_law()

    #Then the trade law should remain limited exports
    assert trade_law.get_name() == "Limited_exports"
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

def test_cannot_switch_to_limited_exports_if_requirements_are_not_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching trade law to limited exports without fulfilling the requirements(which is not having partial mobilization)
    germany.add_political_power(450)

    germany.switch_economy_law(economy_laws.Economy_laws.CIVILIAN_ECONOMY)

    assert germany.get_political_power() == 300

    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)

    assert germany.get_political_power() == 150

    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should remain free trade
    assert trade_law.get_name() == "Free_trade"
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

def test_cannot_switch_to_closed_economy_if_requirements_are_not_fulfilled(germany, new_game):
    #Given Germany start

    #When switching trade law to closed economy without fulfilling the criteria
    germany.add_political_power(150)

    germany.switch_trade_law(trade_laws.Trade_laws.CLOSED_ECONOMY)

    assert germany.get_political_power() == 150

    trade_law = germany.get_trade_law()

    #Then the trade law should remain limited exports
    assert trade_law.get_name() == "Limited_exports"
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

def test_germany_will_keep_limited_exports_even_if_criteria_is_no_longer_fulfilled(germany, new_game): 
    #Given Germany start

    #When Germany no longer has the criteria for switching to limited exports
    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    germany.add_political_power(150)

    #Then when switching to limited exports
    germany.switch_trade_law(trade_laws.Trade_laws.LIMITED_EXPORTS)

    trade_law = germany.get_trade_law()

    #Then the trade law should remain limited exports
    assert trade_law.get_name() == "Limited_exports"
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
























def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(): 

    custom_state = state.State("Custom_state", 50, 15, 15, 10, 3, True, None)

    custom_country = country.Country(name="Custom_country", 
                       states={"Custom_state": custom_state},
                       tiles=None, 
                       resources=None, 
                       free_civs=15, 
                       civs_used_on_consumer_goods=0, 
                       free_mils=15, 
                       free_dockyards=10, 
                       construction=construction.Construction(), 
                       base_ic=4, 
                       modifiers=[], 
                       base_stability=70, 
                       economy_law=modifier.Modifier("Partial_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}), 
                       base_war_support=30, 
                       political_power=0, 
                       population=0, 
                       fuel=0, 
                       command_power=0, 
                       convoys=0, 
                       army_exp=0, 
                       navy_exp=0, 
                       air_exp=0, 
                       ideology=ideologies.Ideologies.FASCIST, 
                       democratic_support=35, 
                       non_aligned_support=15, 
                       communist_support=10, 
                       fascist_support=40, 
                       at_war=False, 
                       countries_at_war_with=[], 
                       research_slots=4, 
                       has_researched=[], 
                       trade_law=None, 
                       conscription_law=None, 
                       advisors=[], 
                       industrial_concern=None, 
                       theorist=None, 
                       chief_of_army=None, 
                       chief_of_navy=None, 
                       chief_of_air_force=None, 
                       high_commanders=[])
    
    custom_country.states["Custom_state"].set_country(custom_country)

    return custom_country