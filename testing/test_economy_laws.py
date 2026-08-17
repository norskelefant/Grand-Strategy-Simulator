import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, custom_country, requirements

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
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When asking for the economy law of germany
    economy_law = germany.get_economy_law()

    #Then the economy law should be Partial_mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == None

    #and Germany should have the following bonuses since the economy law is Partial Mobilization
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

def test_can_switch_economy_law_to_civilian_economy(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to civilian economy when fulfilling prerequisites
    germany.add_political_power(150)

    assert germany.get_political_power() == 150
    assert requirements.can_switch_to_civilian_economy(germany) == True
     
    germany.switch_economy_law(economy_laws.Economy_laws.CIVILIAN_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should be civilian economy
    assert economy_law.get_id() == "Civilian_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.35
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.40
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == -0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == -0.30

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because Civilian Economy is the economy law
    assert germany.get_base_consumer_goods() == 0.35
    #35% * ((1+10%)*(1-12.4%)) = 0.33726
    assert germany.get_consumer_goods() == 0.33726
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == -0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(-0.20)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.40
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.30

def test_can_switch_economy_law_to_early_mobilization(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to early mobilization when fulfilling prerequisites
    germany.add_political_power(150)
    assert germany.get_base_war_support() == 0.3
    assert germany.get_full_war_support() == 0.35
    assert requirements.can_switch_to_early_mobilization(germany) == True

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == -0.15

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the economy law is Early Mobilization
    assert germany.get_base_consumer_goods() == 0.30
    #30% * ((1+10%)*(1-12.4%)) = 0.28908
    assert germany.get_consumer_goods() == 0.28908
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.15

def test_can_switch_economy_law_to_war_economy_when_germany_is_fascist_and_has_over_50_percent_war_support(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to war economy when fulfilling ideology and war support
    germany.add_base_war_support(0.21)
    germany.add_political_power(150)
    assert requirements.can_switch_to_war_economy(germany) == True

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    assert germany.get_full_war_support() == pytest.approx(0.56)
    assert germany.get_ideology() == ideologies.Ideologies.FASCIST

    #Then the economy law should be war economy
    assert economy_law.get_id() == "War_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == 0.25

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the economy law is War Economy
    assert germany.get_base_consumer_goods() == 0.20
    #20% * ((1+10%)*(1-12.4%)) = 0.19272
    assert germany.get_consumer_goods() == pytest.approx(0.19272)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.25

def test_can_switch_economy_law_to_war_economy_when_germany_is_democratic_and_is_at_war_with_enemy_that_has_at_least_40_percent_of_germanys_factories(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to war economy when fulfilling being at war, largest country having at least 40% of Germany's factories, and war support being >50%
    germany.add_political_power(150)

    germany.add_base_war_support(0.16)

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    testing_country = create_custom_country(new_game)

    germany.declare_war(testing_country)

    assert germany.get_is_at_war() == True
    assert germany.get_total_factories() * 0.40 < testing_country.get_total_factories()
    assert requirements.can_switch_to_war_economy(germany) == True

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should be war economy
    assert economy_law.get_id() == "War_economy"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.20
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == 0.25

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the economy law is War Economy
    assert germany.get_base_consumer_goods() == 0.20
    #20% * ((1+10%)*(1-12.4%)) = 0.19272
    assert germany.get_consumer_goods() == pytest.approx(0.19272)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.25

def test_can_switch_economy_law_to_total_mobilization_if_germany_is_at_war_with_country_that_has_at_least_50_percent_as_many_factories_as_germany_and_a_war_support_of_over_80_percent(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to total mobilization when fulfiling being at war, largest country having at least 50% of Germany's factories, and war support being >80%
    germany.add_political_power(150)

    germany.add_base_war_support(0.46)

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    testing_country = create_custom_country(new_game)

    germany.declare_war(testing_country)

    assert germany.get_is_at_war() == True
    assert germany.get_total_factories() * 0.40 < testing_country.get_total_factories()
    assert requirements.can_switch_to_total_mobilization(germany) == True

    germany.switch_economy_law(economy_laws.Economy_laws.TOTAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be total mobilization
    assert economy_law.get_id() == "Total_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.15
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == -0.03
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == 0.50

    assert germany.get_political_power() == 0

    assert germany.get_base_consumer_goods() == 0.15
    #15% * ((1+10%)*(1-12.4%)) = 0.14454
    assert germany.get_consumer_goods() == 0.14454
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.40
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == pytest.approx(-0.005)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.50

def test_switching_economy_law_with_the_same_economy_law_has_no_effect(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to partial mobilization when already being on it
    germany.add_political_power(150)
    assert requirements.can_switch_to_partial_mobilization(germany) == True

    germany.switch_economy_law(economy_laws.Economy_laws.PARTIAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be partial mobilization, and no political power should have been used
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == None

    assert germany.get_political_power() == 150

    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

def test_can_switch_to_early_mobilization_and_it_will_accept_if_switched_to_it_again_even_if_criterias_are_no_longer_fulfilled(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to early mobilization when criterias are fulfilled
    germany.add_political_power(300)

    assert requirements.can_switch_to_early_mobilization(germany) == True
    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == -0.15

    assert germany.get_political_power() == 150

    #When war support falls to 15%, since the full war support is 0.35 at the beginning, a -20% in base leaves 5% base and 15% as full
    germany.add_base_war_support(-0.20)

    #Then it will not fulfill the criterias for switching, but will still be kept on early mobilization
    assert germany.get_base_war_support() == pytest.approx(0.10)
    assert germany.get_full_war_support() == pytest.approx(0.15)
    assert requirements.can_switch_to_early_mobilization(germany) == False

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == -0.15

    assert germany.get_political_power() == 150

    #and Germany has the following bonuses because the economy law is Early Mobilization
    assert germany.get_base_consumer_goods() == 0.30
    #30% * ((1+10%)*(1-12.4%)) = 0.28908
    assert germany.get_consumer_goods() == 0.28908
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.15

def test_cannot_switch_economy_law_if_one_does_not_have_enough_political_power(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to early mobilization when all criteria except for the political power criteria is fulfilled
    assert requirements.can_switch_to_early_mobilization(germany) == True
    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should still be partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == None

    assert germany.get_political_power() == 0

    #and Germany has the following bonuses because the economy law is Partial Mobilization
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

def test_cannot_switch_to_early_mobilization_if_germany_does_not_have_more_than_15_percent_war_support(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to early mobilization when the war support of 15% criteria is not fulfilled
    germany.add_political_power(150)

    germany.add_base_war_support(-0.20)

    assert germany.get_base_war_support() == pytest.approx(0.10)
    assert germany.get_full_war_support() == pytest.approx(0.15)

    assert requirements.can_switch_to_early_mobilization(germany) == False

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should still be partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == None

    assert germany.get_political_power() == 150

    #and Germany has the following bonuses because the economy law is Partial Mobilization
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

def test_cannot_switch_to_partial_mobilization_if_germany_does_not_have_more_than_25_percent_war_support(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to early mobilization when the war support criteria is fulfilled
    germany.add_political_power(300)

    germany.add_base_war_support(-0.10)

    assert germany.get_base_war_support() == pytest.approx(0.20)
    assert germany.get_full_war_support() == 0.25
    assert requirements.can_switch_to_early_mobilization(germany) == True

    germany.switch_economy_law(economy_laws.Economy_laws.EARLY_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should be early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == -0.15

    assert germany.get_political_power() == 150

    #When trying to switch back to partial mobilization when not fulfilling the war support requirement of larger than 25%(since it is 25%)   
    assert requirements.can_switch_to_partial_mobilization(germany) == False

    germany.switch_economy_law(economy_laws.Economy_laws.PARTIAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should remain early mobilization
    assert economy_law.get_id() == "Early_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.30
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == -0.15

    assert germany.get_political_power() == 150

    #and Germany has the following bonuses because the economy law is Early Mobilization
    assert germany.get_base_consumer_goods() == 0.30
    #30% * ((1+10%)*(1-12.4%)) = 0.28908
    assert germany.get_consumer_goods() == 0.28908
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == -0.15

def test_cannot_switch_to_war_economy_if_germany_is_democratic_and_countries_germany_is_at_war_with_dont_have_40_percent_of_germanys_amount_of_factories(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to war economy while factory count of enemy country is not fulfilled
    germany.add_political_power(150)

    germany.add_base_war_support(0.16)
    germany.set_at_war(True)

    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)

    assert germany.get_full_war_support() == 0.51
    assert germany.get_is_at_war() == True
    assert germany.get_number_of_factories_enemy_country_with_most_factories_has() == 0
    assert len(germany.get_countries_at_war_with()) == 0
    assert requirements.can_switch_to_war_economy(germany) == False

    #germany.declare_war(testing_country)

    germany.switch_economy_law(economy_laws.Economy_laws.WAR_ECONOMY)

    economy_law = germany.get_economy_law()

    #Then the economy law should remain partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == None

    assert germany.get_political_power() == 150

    #and Germany has the following bonuses since the economy law is Partial Mobilization
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

def test_cannot_switch_to_total_mobilization_if_germany_is_at_war_but_enemies_dont_have_50_percent_of_germanys_factory_count(germany, new_game): 
    #Given Germany start
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0

    #When switching the economy law to total mobilization while factory count of enemy country is not fulfilled
    germany.add_political_power(150)

    germany.add_base_war_support(0.46)
    germany.set_at_war(True)

    assert germany.get_full_war_support() == pytest.approx(0.81)
    assert germany.get_is_at_war() == True
    assert germany.get_number_of_factories_enemy_country_with_most_factories_has() == 0
    assert len(germany.get_countries_at_war_with()) == 0
    assert requirements.can_switch_to_total_mobilization(germany) == False

    #germany.declare_war(testing_country)

    germany.switch_economy_law(economy_laws.Economy_laws.TOTAL_MOBILIZATION)

    economy_law = germany.get_economy_law()

    #Then the economy law should remain partial mobilization
    assert economy_law.get_id() == "Partial_mobilization"
    assert economy_law.get_end_date() == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS) == 0.25
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED) == 0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_GAIN_PER_OIL) == -0.10
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FUEL_CAPACITY) == None
    assert economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION) == None

    assert germany.get_political_power() == 150

    #and Germany has the following bonuses since the economy law is Partial Mobilization
    assert germany.get_base_consumer_goods() == 0.25
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_GAIN_PER_OIL] == -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FUEL_CAPACITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION] == 0.0





def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)

