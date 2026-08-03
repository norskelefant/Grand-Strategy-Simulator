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

def test_total_modifier_bonus_for_custom_country_and_germany_is_correct(germany, new_game): 
    #Given a custom country
    testing_country = create_custom_country()

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

    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESOURCES_TO_MARKET] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.05
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
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSTRUCTION_SPEED] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESEARCH_SPEED] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS] == pytest.approx(0.15)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER] == 0.05


    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY] == 0.11
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT] == 0.05
















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
                       base_stability=70, 
                       economy_law=modifier.Modifier("Partial_mobilization", "Partial Mobilization", 0, modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, True), 
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
                       can_research=[],
                       trade_law=None, 
                       conscription_law=None, 
                       advisors=[], 
                       possible_advisors={},
                       industrial_concern=None, 
                       possible_industrial_concerns={},
                       theorist=None, 
                       possible_theorists={},
                       chief_of_army=None, 
                       possible_chiefs_of_army={},
                       chief_of_navy=None, 
                       possible_chiefs_of_navy={},
                       chief_of_air_force=None, 
                       possible_chiefs_of_air_force={},
                       high_commanders=[], 
                       possible_high_commanders={},
                       leader=None, 
                       possible_leaders={},
                       focus_tree=[], 
                       focuses_done=[], 
                       focuses_that_can_be_done=[], 
                       national_spirits=[], 
                       modifiers=[], 
                        possible_events={}, 
                       events_gotten=[], 
                       intelligence_agency=None,
                       full_added_bonuses={})
    
    custom_country.states["Custom_state"].set_country(custom_country)

    custom_country.full_added_bonuses = custom_country.create_default_bonuses_map()

    testing_modifier_1 = modifier.Modifier("Testing_modifier_1", "Testing modifier 1", 0, modifier_classes.Modifier_classes.BASE, None, {modifier_types.Modifier_types.STABILITY: 0.10, modifier_types.Modifier_types.WAR_SUPPORT: 0.10, modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.10}, True)

    testing_modifier_2 = modifier.Modifier("Testing_modifier_2", "Testing modifier 2", 0, modifier_classes.Modifier_classes.BASE, None, {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.25}, True)

    custom_country.modifiers.append(testing_modifier_1)
    custom_country.add_to_full_added_bonuses(testing_modifier_1)

    custom_country.modifiers.append(testing_modifier_2)
    custom_country.add_to_full_added_bonuses(testing_modifier_2)


    return custom_country