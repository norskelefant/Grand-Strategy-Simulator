import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, trade_laws, custom_country, conscription_laws

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_germany_has_limited_conscription_by_default(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025

    #When asking for the conscription law of germany
    conscription_law = germany.get_conscription_law()

    #Then the trade law should be limited export
    assert conscription_law.get_id() == "Limited_conscription"
    assert conscription_law.get_end_date() == None
    assert conscription_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == 0.025

    #and Germany gets these bonuses because the conscription law is Limited Conscription
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025

def test_can_switch_to_disarmed_nation(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025

    #When Germany switches to Disarmed Nation with enough political power
    germany.add_political_power(300)

    germany.switch_conscription_law(conscription_laws.Conscription_laws.DISARMED_NATION)

    assert germany.calculate_conscription_law_cost("Limited_conscription", "Disarmed_nation") == 300

    assert germany.get_political_power() == 0

    #When asking for the conscription law of germany
    conscription_law = germany.get_conscription_law()

    #Then the conscription law should be Disarmed nation
    assert conscription_law.get_id() == "Disarmed_nation"
    assert conscription_law.get_end_date() == None
    assert conscription_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == 0.01

    #and Germany gets these bonuses because the new conscription law is Disarmed Nation
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.01

def test_can_switch_to_volunteer_only(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025

    #When Germany switches to Volunteer Only with enough political power
    germany.add_political_power(150)

    germany.switch_conscription_law(conscription_laws.Conscription_laws.VOLUNTEER_ONLY)

    assert germany.calculate_conscription_law_cost("Limited_conscription", "Volunteer_only") == 150

    assert germany.get_political_power() == 0

    #When asking for the conscription law of germany
    conscription_law = germany.get_conscription_law()

    #Then the conscription law should be Volunteer Only
    assert conscription_law.get_id() == "Volunteer_only"
    assert conscription_law.get_end_date() == None
    assert conscription_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == 0.015

    #and Germany gets these bonuses because the new conscription law is Volunteer Only
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.015

def test_can_switch_to_limited_conscription_if_more_than_10_percent_war_support(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025

    #When Germany switches to Limited Conscription with more than 10 percent war support
    germany.add_political_power(300)

    assert germany.get_full_war_support() == 0.35

    germany.switch_conscription_law(conscription_laws.Conscription_laws.VOLUNTEER_ONLY)
    germany.switch_conscription_law(conscription_laws.Conscription_laws.LIMITED_CONSCRIPTION)

    assert germany.get_political_power() == 0

    conscription_law = germany.get_conscription_law()

    #Then the conscription law should be Limited conscription
    assert conscription_law.get_id() == "Limited_conscription"
    assert conscription_law.get_end_date() == None
    assert conscription_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == 0.025

    #and Germany gets these bonuses because the new conscription law is Limited Conscription
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025

def test_cannot_switch_to_limited_conscription_if_less_than_10_percent_war_support(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.025

    #When Germany switches to Limited Conscription with less than 10 percent war support
    germany.add_base_war_support(-0.30)
    germany.add_political_power(300)

    assert germany.get_full_war_support() == 0.05

    germany.switch_conscription_law(conscription_laws.Conscription_laws.VOLUNTEER_ONLY)
    germany.switch_conscription_law(conscription_laws.Conscription_laws.LIMITED_CONSCRIPTION)

    assert germany.get_political_power() == 150

    conscription_law = germany.get_conscription_law()

    #Then the conscription law should be Volunteer Only,
    assert conscription_law.get_id() == "Volunteer_only"
    assert conscription_law.get_end_date() == None
    assert conscription_law.get_modifier_bonuses().get(modifier_types.Modifier_types.RECRUITABLE_POPULATION) == 0.015

    #but Germany gets these bonuses because Germany does not get Limited Conscription
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RECRUITABLE_POPULATION] == 0.015
def test_can_switch_to_extensive_conscription_if_more_than_20_percent_war_support_and_being_fascist(germany, new_game): 
    assert True == False

def test_can_switch_to_extensive_conscription_if_more_than_20_percent_war_support_and_being_communist(germany, new_game): 
    assert True == False

def test_can_switch_to_extensive_conscription_if_more_than_20_percent_war_support_and_being_at_war_and_enemy_having_an_army_strength_ratio_of_50_percent_or_more(germany, new_game): 
    assert True == False

def test_cannot_switch_to_extensive_conscription_if_less_than_20_percent_war_support_and_being_fascist(germany, new_game): 
    assert True == False

def test_cannot_switch_to_extensive_conscription_if_less_than_20_percent_war_support_and_being_communist(germany, new_game): 
    assert True == False

def test_cannot_switch_to_extensive_conscription_if_less_than_20_percent_war_support_and_enemies_have_an_army_strength_of_50_percent_or_more(germany, new_game): 
    assert True == False

def test_cannot_switch_to_extensive_conscription_if_more_than_20_percent_war_support_and_at_war_and_enemies_have_an_army_strength_of_less_than_50_percent(germany, new_game): 
    assert True == False

def test_can_switch_to_service_by_requirement_if_country_is_fascist_and_has_more_than_60_percent_war_support(germany, new_game): 
    assert True == False

def test_can_switch_to_service_by_requirement_if_country_is_communist_and_has_more_than_60_percent_war_support(germany, new_game): 
    assert True == False

def test_can_switch_to_service_by_requirement_if_country_is_at_war_with_enemies_that_have_an_army_strength_of_60_or_more_percent_and_has_a_war_support_of_more_than_60_percent(germany, new_game): 
    assert True == False

def test_can_switch_to_service_by_requirement_if_country_is_fascist_and_has_more_than_0_percent_surrender_progress(germany, new_game): 
    assert True == False

def test_can_switch_to_service_by_requirement_if_country_is_communist_and_has_more_than_0_percent_surrender_progress(germany, new_game): 
    assert True == False

def test_can_switch_to_service_by_requirement_if_country_is_at_war_with_enemies_that_have_an_army_strength_of_60_or_more_percent_and_has_a_surrender_progress_of_more_than_0_percent(germany, new_game): 
    assert True == False

def test_cannot_switch_to_service_by_requirement_if_country_has_less_than_60_percent_war_support(germany, new_game): 
    assert True == False

def test_cannot_switch_to_service_by_requirement_if_country_has_0_percent_surrender_progress(germany, new_game): 
    assert True == False

def test_cannot_switch_to_service_by_requirement_if_country_is_not_communist_or_fascist(germany, new_game): 
    assert True == False

def test_cannot_switch_to_service_by_requirement_if_country_is_not_at_war(germany, new_game): 
    assert True == False

def test_cannot_switch_to_service_by_requirement_if_country_is_at_war_and_enemies_army_strength_is_less_than_60_percent_of_country(germany, new_game): 
    assert True == False

def test_can_switch_to_all_adults_serve_if_country_is_at_war_with_enemies_having_more_than_70_percent_army_strength_ratio_and_country_has_more_than_70_percent_war_support(germany, new_game): 
    assert True == False

def test_can_switch_to_all_adults_serve_if_country_is_at_war_with_enemies_having_more_than_70_percent_army_strength_ratio_and_country_has_more_than_0_percent_surrender_progress(germany, new_game): 
    assert True == False

def test_cannot_switch_to_all_adults_serve_if_country_is_at_war_with_enemies_having_more_than_70_percent_army_strength_ratio_and_country_does_not_fulfill_having_enough_war_support_or_surrender_progress(germany, new_game): 
    assert True == False

def test_cannot_switch_to_all_adults_serve_if_country_is_not_at_war(germany, new_game): 
    assert True == False

def test_cannot_switch_to_all_adults_serve_if_country_is_at_war_but_enemies_army_strength_is_not_more_than_70_compared_to_country(germany, new_game): 
    assert True == False

def test_can_switch_to_scraping_the_barrel_if_enemies_army_have_more_than_100_percent_strength_ratio_and_country_has_more_than_85_percent_war_support(germany, new_game): 
    assert True == False

def test_can_switch_to_scraping_the_barrel_if_enemies_army_have_more_than_100_percent_strength_ratio_and_country_has_more_than_25_percent_surrender_progress(germany, new_game): 
    assert True == False

def test_cannot_switch_to_scraping_the_barrel_if_enemies_army_have_more_than_100_percent_strength_ratio_but_country_does_not_fulfill_war_support_or_surrender_progress_criteria(germany, new_game): 
    assert True == False

def test_cannot_switch_to_scraping_the_barrel_if_not_at_war(germany, new_game): 
    assert True == False

def test_cannot_switch_to_scraping_the_barrel_if_at_war_but_enemies_army_strength_ratio_is_lower_than_100_percent(germany, new_game): 
    assert True == False

    

def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)