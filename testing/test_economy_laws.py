import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_partial_mobilization_is_default_economy_law_for_germany(germany, new_game): 
    #Given Germany start

    #When asking for the economy law of germany
    economy_law = germany.get_economy_law()

    #Then the economy law should be Partial_mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10

def test_can_switch_economy_law_to_civilian_economy_if_prerequisites_are_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the economy law to civilian economy when fulfilling prerequisites
    germany.add_political_power(150)

    assert germany.get_political_power() == 150
     
    germany.switch_economy_law(economy_laws.Economy_laws.CIVILIAN_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should be civilian economy
    assert economy_law.get_id() == "Civilian_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.35
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.30

    assert germany.get_political_power() == 0

def test_can_switch_economy_law_to_early_mobilization(germany, new_game): 
    #Given Germany start

    #When switching the economy law to early mobilization when fulfilling prerequisites
    germany.add_political_power(150)
    assert germany.get_base_war_support() == 0.3
    assert germany.get_full_war_support() == 0.40

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10

    assert germany.get_political_power() == 0

def test_can_switch_economy_law_to_war_economy_one(germany, new_game): 
    #Given Germany start

    #When switching the economy law to war economy when fulfilling ideology and war support
    germany.add_base_war_support(0.16)
    germany.add_political_power(150)

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    assert germany.get_full_war_support() == pytest.approx(0.56)
    assert germany.get_ideology() == ideologies.Ideologies.FASCIST

    #Then the economy law should be war economy
    assert economy_law.get_id() == "War_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.20

    assert germany.get_political_power() == 0


def test_can_switch_economy_law_to_war_economy_two(germany, new_game): 
    #Given Germany start

    #When switching the economy law to war economy when fulfilling being at war, largest country having at least 40% of Germany's factories, and war support being >50%
    germany.add_political_power(150)

    germany.add_base_war_support(0.16)

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    testing_country = create_custom_country()

    germany.declare_war(testing_country)

    assert germany.get_is_at_war() == True
    assert germany.get_total_factories() * 0.40 < testing_country.get_total_factories()
    assert germany.is_fascist_or_communist() == False

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should be war economy
    assert economy_law.get_id() == "War_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.20

    assert germany.get_political_power() == 0

def test_can_switch_economy_law_to_total_mobilization(germany, new_game): 
    #Given Germany start

    #When switching the economy law to total mobilization when fulfiling being at war, largest country having at least 50% of Germany's factories, and war support being >80%
    germany.add_political_power(150)

    germany.add_base_war_support(0.46)

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    testing_country = create_custom_country()

    germany.declare_war(testing_country)

    assert germany.get_is_at_war() == True
    assert germany.get_total_factories() * 0.40 < testing_country.get_total_factories()
    assert germany.is_fascist_or_communist() == False

    germany.switch_economy_law(economy_laws.Economy_laws.TOTAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be total mobilization
    assert economy_law.get_id() == "Total_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.15
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.30

    assert germany.get_political_power() == 0

def test_switching_economy_law_with_the_same_economy_law_has_no_effect(germany, new_game): 
    #Given Germany start

    #When switching the economy law to partial mobilization when already being on it
    germany.add_political_power(150)

    germany.switch_economy_law(economy_laws.Economy_laws.PARTIAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be total mobilization, and no political power should have been used
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10

    assert germany.get_political_power() == 150

def test_can_switch_to_early_mobilization_and_it_will_accept_if_switched_to_it_again_even_if_criterias_are_no_longer_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the economy law to early mobilization when criterias are fulfilled
    germany.add_political_power(300)

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10

    assert germany.get_political_power() == 150

    #When war support falls to 15%, since the full war support is 0.40 at the beginning, a -25% in base leaves 5% base and 15% as full
    germany.add_base_war_support(-0.25)

    #Then it will not fulfill the criterias for switching, but will still be kept on early mobilization
    assert germany.get_base_war_support() == pytest.approx(0.05)
    assert germany.get_full_war_support() == pytest.approx(0.15)

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10

    assert germany.get_political_power() == 150

def test_cannot_switch_economy_law_if_one_does_not_have_enough_political_power(germany, new_game): 
    #Given Germany start

    #When switching the economy law to early mobilization when all criteria except for the political power criteria is fulfilled
    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should still be partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10

    assert germany.get_political_power() == 0

def test_cannot_switch_to_early_mobilization_if_criteria_is_not_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the economy law to early mobilization when the war support of 15% criteria is not fulfilled
    germany.add_political_power(150)

    germany.add_base_war_support(-0.25)

    assert germany.get_base_war_support() == pytest.approx(0.05)
    assert germany.get_full_war_support() == pytest.approx(0.15)

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should still be partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10

    assert germany.get_political_power() == 150

def test_cannot_switch_to_partial_mobilization_if_criteria_is_not_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the economy law to early mobilization when the war support criteria is fulfilled
    germany.add_political_power(300)

    germany.add_base_war_support(-0.15)

    assert germany.get_base_war_support() == 0.15
    assert germany.get_full_war_support() == 0.25

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10

    assert germany.get_political_power() == 150

    #When trying to switch back to partial mobilization when not fulfilling the war support requirement of larger than 25%(since it is 25%)   
    germany.switch_economy_law(economy_laws.Economy_laws.PARTIAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should remain early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10

    assert germany.get_political_power() == 150

def test_cannot_switch_to_war_economy_if_criteria_is_not_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the economy law to war economy while factory count of enemy country is not fulfilled
    germany.add_political_power(150)

    germany.add_base_war_support(0.11)
    germany.set_at_war(True)

    testing_country = create_custom_country()

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    assert germany.get_full_war_support() == 0.51
    assert germany.get_is_at_war() == True
    assert germany.get_number_of_factories_enemy_country_with_most_factories_has() == 0
    assert len(germany.get_countries_at_war_with()) == 0

    #germany.declare_war(testing_country)

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should remain partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10

    assert germany.get_political_power() == 150

def test_cannot_switch_to_total_mobilization_if_criteria_is_not_fulfilled(germany, new_game): 
    #Given Germany start

    #When switching the economy law to total mobilization while factory count of enemy country is not fulfilled
    germany.add_political_power(150)

    germany.add_base_war_support(0.41)
    germany.set_at_war(True)

    testing_country = create_custom_country()

    assert germany.get_full_war_support() == pytest.approx(0.81)
    assert germany.get_is_at_war() == True
    assert germany.get_number_of_factories_enemy_country_with_most_factories_has() == 0
    assert len(germany.get_countries_at_war_with()) == 0

    #germany.declare_war(testing_country)

    germany.switch_economy_law(economy_laws.Economy_laws.TOTAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should remain partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10

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
                       base_stability=0.7, 
                       economy_law=modifier.Modifier("Partial_mobilization", "Partial Mobilization", 0, modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, True), 
                       base_war_support=0.3, 
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
                       full_added_bonuses={})
    
    custom_country.states["Custom_state"].set_country(custom_country)

    return custom_country

