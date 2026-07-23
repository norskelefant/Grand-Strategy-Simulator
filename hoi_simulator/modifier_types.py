from enum import Enum

class Modifier_types(Enum): 
    #Consumer goods
    BASE_CONSUMER_GOODS = "base_consumer_goods"
    CONSUMER_GOODS_FACTOR = "consumer_goods_factor"

    #Construction
    CIV_CONSTRUCTION_SPEED = "civ_construction_speed"
    MIL_CONSTRUCTION_SPEED = "mil_construction_speed"
    DOCKYARD_CONSTRUCTION_SPEED = "dockyard_construction_speed"
    CONSTRUCTION_SPEED = "construction_speed"
    SUPPLY_HUB_CONSTRUCTION_SPEED = "supply_hub_construction_speed"
    BASE_CONSTRUCTION_LINE_SPEED_BOOST = "base_construction_line_speed_boost"

    #Conversion
    MIL_TO_CIV_CONVERSION_COST = "mil_to_civ_conversion_cost"
    CIV_TO_MIL_CONVERSION_COST = "civ_to_mil_conversion_cost"

    #Production
    FACTORY_OUTPUT = "factory_output"
    PRODUCTION_EFFICIENCY_GROWTH = "production_efficiency_growth"
    PRODUCTION_EFFICIENCY_BASE = "production_efficiency_base"
    DOCKYARD_OUTPUT = "dockyard_output"

    #Manpower
    RECRUITABLE_POPULATION = "recruitable_population"

    #Research
    RESEARCH_SPEED = "research_speed"

    #Resources
    RESOURCES_TO_MARKET = "resources_to_market"
    LACK_OF_RESOURCES_PENALTY = "lack_of_resources_penalty"

    #Repair
    FREE_REPAIR = "free_repair"

    #Fuel
    FUEL_GAIN_PER_OIL = "fuel_gain_per_oil"
    FUEL_CAPACITY = "fuel_capacity"

    #Coal
    FACTORY_ENERGY_CONSUMPTION = "factory_energy_consumption"

    #Stability
    STABILITY = "stability"
    OFFENSIVE_WAR_STABILITY_MODIFIER = "offensive_war_stability_modifier"
    DEFENSIVE_WAR_STABILITY_MODIFIER = "defensive_war_stability_modifier"
    WEEKLY_STABILITY = "weekly_stability"
    PARTY_POPULARITY_STABILITY_MODIFIER = "party_popularity_stability_modifier"

    #War support
    WAR_SUPPORT = "war_support"
    WEEKLY_WAR_SUPPORT = "weekly_war_support"
    #Add other weekly war support modifiers later
    WEEKLY_WAR_SUPPORT_ENEMY_BOMBING = "weekly_war_support_enemy_bombing"

    #Party popularity
    DAILY_DEMOCRACY_SUPPORT = "daily_democracy_support"
    DAILY_NON_ALIGNED_SUPPORT = "daily_non_aligned_support"
    DAILY_COMMUNIST_SUPPORT = "daily_communist_support"
    DAILY_FASCISM_SUPPORT = "daily_fascism_support"
    IDEOLOGY_DRIFT_DEFENCE = "ideology_drift_defence"

    #Spies
    OPERATIVE_SLOTS = "operative_slots"
    AGENCY_UPGRADE_TIME = "agency_upgrade_time"
    CIVILIAN_INTELLIGENCE_TO_OTHERS = "civilian_intelligence_to_others"
    ARMY_INTELLIGENCE_TO_OTHERS = "army_intelligence_to_others"    
    NAVY_INTELLIGENCE_TO_OTHERS = "navy_intelligence_to_others"


    #Foreign meddling
    FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY = "foreign_subversive_activities_efficiency"
    SUBVERSIVE_ACTIVITIES_COST = "subversive_activities_cost"
    IMPROVE_RELATIONS_MAINTAIN_COST = "improve_relations_maintain_cost"
    TRADE_DEAL_OPINION_FACTOR = "trade_deal_opinion_factor"
    FACTION_TRADE_DEAL_OPINION_FACTOR = "faction_trade_deal_opinion_factor"
    SAME_IDEOLOGY_MONTHLY_OPINION = "same_ideology_monthly_opinion"

    #Subjects
    SUBJECT_AUTONOMY_GAIN = "subject_autonomy_gain"

    #Resistance and compliance
    COMPLIANCE_GROWTH_SPEED = "compliance_growth_speed"
    RESITANCE_GROWTH_SPEED = "resistance_growth_speed"

    #War goals
    JUSTIFY_WAR_GOAL_TIME = "justify_war_goal_time"

    #Political power
    POLITICAL_POWER_GAIN = "political_power_gain"
    CONSCRIPTION_LAW_COST = "conscription_law_cost"
    TRADE_LAW_COST = "trade_law_cost"
    ECONOMY_LAW_COST = "economy_law_cost"
    POLITICAL_ADVISOR_COST = "political_advisor_cost"

    #Lend lease
    LEND_LEASE_TENSION_LIMIT = "lend_lease_tension_limit"

    #International market
    MARKET_CONSTRUCTION_BOOST_MULTIPLIER = "market_construction_boost_multiplier"
    CAN_ACCESS_INTERNATIONAL_MARKET = "can_access_international_market"

    #Add many more later....
