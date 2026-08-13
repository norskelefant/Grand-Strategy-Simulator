import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, trade_laws, custom_country

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_total_modifier_bonus_for_custom_country_and_germany_is_correct(germany, new_game): 
    #Given a custom country
    testing_country = create_custom_country(new_game)

    #When asking for the total modifiers

    #Then they should be the following from the modifiers
    assert len(testing_country.get_modifiers()) == 2
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.35

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05

def test_total_modifier_works_when_switching_economy_law(germany, new_game): 
    #Given Germany

    #Then the full added bonuses should be the following according to the economy law
    germany.add_political_power(150)

    assert germany.get_base_consumer_goods() == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05

    #When the economy law is switched to early mobilization
    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    #Then the new full added bonuses should be applied and the old ones removed
    assert germany.get_base_consumer_goods() == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == -0.10
    germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.15 

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05

def test_total_modifier_works_when_switching_trade_law(germany, new_game): 

    #Given Germany

    #Then the full added bonuses should be the following according to the trade law
    germany.add_political_power(150)

    assert germany.get_full_stability() == pytest.approx(0.81)
    print(germany.get_stability_modifier().modifier_bonuses[modifier_types.Modifier_types.FACTORY_OUTPUT])

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.01
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST] == -0.05

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05

    #When the trade law is switched to free trade
    germany.switch_trade_law(trade_laws.Trade_laws.FREE_TRADE)
    print(germany.get_trade_law().name)

    #Then the new full added bonuses should be applied and the old ones removed
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.80
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.274)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.274)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == pytest.approx(0.15)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER] == 0.05

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05

def test_total_modifier_updates_stability_and_war_support_modifier(germany, new_game): 
    #Given Germany

    print(germany.get_leader().id)

    #When an extra war support and stability modifier is given

    new_modifier = modifier.Modifier("testing_modifier", 
                                     "Testing modifier", 
                                     0, 
                                     modifier_classes.Modifier_classes.BASE, 
                                     None, 
                                     {modifier_types.Modifier_types.STABILITY: 0.05, 
                                      modifier_types.Modifier_types.WAR_SUPPORT: 0.10}, 
                                     True)

    germany.modifiers.append(new_modifier)
    germany.add_to_full_added_bonuses(new_modifier)

    #Then the stability and war support modifiers should be updated
    assert germany.get_base_stability() == 0.7
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.16
    assert germany.get_full_stability() == 0.86
    assert germany.get_base_war_support() == 0.3
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == pytest.approx(0.15)
    assert germany.get_full_war_support() == 0.45

    #25% * ((1+10%)*(1-14.4%)) = 0.2354
    assert germany.get_consumer_goods() == pytest.approx(0.2354)
    #10% - 14.4% = 4.4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.044)
    #14.4% added, also have 5% as default, meaning the total is 19.4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.194
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.194
    #No extra political power gain at the beginning(when leaders are implemented later, this will change)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.072)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.028
















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 

    testing_country = custom_country.create_custom_country(game)

    testing_modifier_1 = modifier.Modifier("Testing_modifier_1", "Testing modifier 1", 0, modifier_classes.Modifier_classes.BASE, None, {modifier_types.Modifier_types.STABILITY: 0.10, modifier_types.Modifier_types.WAR_SUPPORT: 0.10, modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.10}, True)

    testing_modifier_2 = modifier.Modifier("Testing_modifier_2", "Testing modifier 2", 0, modifier_classes.Modifier_classes.BASE, None, {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.25}, True)

    testing_country.modifiers.append(testing_modifier_1)
    testing_country.add_to_full_added_bonuses(testing_modifier_1)

    testing_country.modifiers.append(testing_modifier_2)
    testing_country.add_to_full_added_bonuses(testing_modifier_2)


    return testing_country