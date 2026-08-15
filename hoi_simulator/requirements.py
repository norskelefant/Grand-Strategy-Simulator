from hoi_simulator import country, ideologies

def has_not_completed_focus(country, focus_name):
    return not country.has_completed_focus(focus_name)

def has_completed_focus(country, focus_name):
    return country.has_completed_focus(focus_name)

def has_free_theorist_slot(country):
    return country.has_free_theorist_slot()

def has_free_industrial_concern_slot(country):
    return country.has_free_industrial_concern_slot()

def has_free_high_commander_slot(country):
    return country.has_free_high_commander_slot()

def has_free_chief_of_navy_slot(country):
    return country.has_free_chief_of_navy_slot()

def has_free_chief_of_army_slot(country):
    return country.has_free_chief_of_army_slot()

def has_free_chief_of_air_slot(country):
    return country.has_free_chief_of_air_slot()

def has_free_advisor_slot(country):
    return country.has_free_advisor_slot()

def is_not_already_hired_elsewhere(country, advisor_name):
    return not country.is_already_hired_elsewhere(advisor_name)

def is_not_country_leader(country, leader_name):
    return not country.is_country_leader(leader_name)

def is_fascist(country):
    return country.check_ideology(ideologies.Ideologies.FASCIST)

def is_not_fascist(country):
    return not country.check_ideology(ideologies.Ideologies.FASCIST)

def is_communist(country):
    return country.check_ideology(ideologies.Ideologies.COMMUNIST)

def is_not_communist(country):
    return not country.check_ideology(ideologies.Ideologies.COMMUNIST)

def is_democratic(country):
    return country.check_ideology(ideologies.Ideologies.DEMOCRATIC)

def is_non_aligned(country):
    return country.check_ideology(ideologies.Ideologies.NON_ALIGNED)

def event_has_happened(country, event_name):
    return country.event_has_happened(event_name)

def has_mefo_bills(country):
    return country.has_mefo_bills()

def has_not_hired_advisor(country, advisor_name):
    return not country.has_hired_advisor(advisor_name)

def has_created_intelligence_agency(country):
    return country.has_created_intelligence_agency()

def can_switch_to_civilian_economy(country): 
    return True

def can_switch_to_early_mobilization(country): 
    return country.get_full_war_support() > 0.15 + 1e-12

def can_switch_to_partial_mobilization(country): 
    return country.get_full_war_support() > 0.25 + 1e-12
    
def can_switch_to_war_economy(country): 
    if country.get_full_war_support() <= 0.50 + 1e-12: 
        return False
    if is_communist(country) or is_fascist(country): 
        return True
    elif country.get_is_at_war() == True and country.get_number_of_factories_enemy_country_with_most_factories_has() > (0.40 * country.get_total_factories()): 
        return True
    return False
    
def can_switch_to_total_mobilization(country): 
    return country.get_is_at_war() and country.get_full_war_support() > 0.8 + 1e-12 and country.get_number_of_factories_enemy_country_with_most_factories_has() > (0.50 * country.get_total_factories())

def can_switch_to_free_trade(country): 
    return True

def can_switch_to_export_focus(country): 
    return True
    
def can_switch_to_limited_exports(country): 
    if country.get_ideology() == ideologies.Ideologies.DEMOCRATIC: 
        if country.get_is_at_war() == True and country.get_number_of_factories_enemy_country_with_most_factories_has() > (0.20 * country.get_total_factories()): 
            return True
        return False
    else: 
        if country.get_economy_law().get_id() == "Partial_mobilization" or country.get_economy_law().get_id() == "War_economy" or country.get_economy_law().get_id() == "Total_mobilization": 
            return True
        return False

def can_switch_to_closed_economy(country): 
    if country.get_is_at_war() == True and (is_fascist(country) or is_communist(country)): 
        if country.get_economy_law().get_id() == "War_economy" or country.get_economy_law().get_id() == "Total_mobilization": 
            return True
    return False



