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
    INFRASTRUCTURE_CONSTRUCTION_SPEED = "infrastructure_construction_speed"
    RAILWAY_CONSTRUCTION_SPEED = "railway_construction_speed"

    #Conversion
    MIL_TO_CIV_CONVERSION_COST = "mil_to_civ_conversion_cost"
    CIV_TO_MIL_CONVERSION_COST = "civ_to_mil_conversion_cost"

    #Production
    FACTORY_OUTPUT = "factory_output"
    PRODUCTION_EFFICIENCY_GROWTH = "production_efficiency_growth"
    PRODUCTION_EFFICIENCY_BASE = "production_efficiency_base"
    DOCKYARD_OUTPUT = "dockyard_output"
    PRODUCTION_EFFICIENCY_RETENTION = "production_efficiency_retention"

    #Manpower
    RECRUITABLE_POPULATION = "recruitable_population"
    RECRUITABLE_POPULATION_FACTOR = "recruitable_population_factor"
    NON_CORE_MANPOWER = "non_core_manpower"
    MONTHLY_POPULATION = "monthly_population"

    #Research
    RESEARCH_SPEED = "research_speed"
    INDUSTRIAL_RESEARCH_SPEED = "industrial_research_speed"
    SYNTHETIC_RESOURCES_RESEARCH_SPEED = "synthetic_resources_research_speed"
    ELECTRONICS_RESEARCH_SPEED = "electronics_research_speed"
    EXCAVATION_TECHNOLOGY_RESEARCH_SPEED = "excavation_technology_research_speed"
    TRAINS_AND_RAILWAYS_RESEARCH_SPEED = "trains_and_railways_research_speed"
    NUCLEAR_RESEARCH_SPEED = "nuclear_research_speed"

    #Special projects
    AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED = "aerodynamics_and_avionics_special_projects_speed"
    LAND_WARFARE_SPECIAL_PROJECTS_SPEED = "land_warfare_special_projects_speed"

    #Resources
    RESOURCES_TO_MARKET = "resources_to_market"
    LACK_OF_RESOURCES_PENALTY = "lack_of_resources_penalty"
    RESOURCE_GAIN_EFFICIENCY = "resource_gain_efficiency"
    COAL = "coal"
    COAL_GAIN_EFFICIENCY = "coal_gain_efficiency"

    #Repair
    FREE_REPAIR = "free_repair"

    #Fuel
    FUEL_GAIN_PER_OIL = "fuel_gain_per_oil"
    FUEL_CAPACITY = "fuel_capacity"

    #Coal
    FACTORY_ENERGY_CONSUMPTION = "factory_energy_consumption"

    #Stability
    BASE_STABILITY = "base_stability"
    STABILITY = "stability"
    OFFENSIVE_WAR_STABILITY_MODIFIER = "offensive_war_stability_modifier"
    DEFENSIVE_WAR_STABILITY_MODIFIER = "defensive_war_stability_modifier"
    WEEKLY_STABILITY = "weekly_stability"
    PARTY_POPULARITY_STABILITY_MODIFIER = "party_popularity_stability_modifier"

    #War support
    BASE_WAR_SUPPORT = "base_war_support"
    WAR_SUPPORT = "war_support"
    WEEKLY_WAR_SUPPORT = "weekly_war_support"
    #Add other weekly war support modifiers later
    WEEKLY_WAR_SUPPORT_ENEMY_BOMBING = "weekly_war_support_enemy_bombing"
    WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES = "weekly_war_support_combat_casualties"

    NON_COMBAT_OUT_OF_SUPPLY_PENALTIES = "non_combat_out_of_supply_penalties"

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
    AIR_FORCE_INTELLIGENCE_TO_OTHERS = "air_force_intelligence_to_others"


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
    DAILY_COMPLIANCE_GAIN = "daily_compliance_gain"

    #War goals
    JUSTIFY_WAR_GOAL_TIME = "justify_war_goal_time"

    #Political power
    POLITICAL_POWER_GAIN = "political_power_gain"
    CONSCRIPTION_LAW_COST = "conscription_law_cost"
    TRADE_LAW_COST = "trade_law_cost"
    ECONOMY_LAW_COST = "economy_law_cost"
    POLITICAL_ADVISOR_COST = "political_advisor_cost"
    THEORIST_COST = "theorist_cost"
    INDUSTRIAL_CONCERN_COST = "industrial_concern_cost"
    CHIEF_OF_ARMY_COST = "chief_of_army_cost"
    CHIEF_OF_NAVY_COST = "chief_of_navy_cost"
    CHIEF_OF_AIR_FORCE_COST = "chief_of_air_force_cost"
    HIGH_COMMANDER_COST = "high_commander_cost"

    #Lend lease
    LEND_LEASE_TENSION_LIMIT = "lend_lease_tension_limit"

    #International market
    MARKET_CONSTRUCTION_BOOST_MULTIPLIER = "market_construction_boost_multiplier"
    CAN_ACCESS_INTERNATIONAL_MARKET = "can_access_international_market"

    #Militia
    MILITIA_ATTACK = "militia_attack"
    MILITIA_DEFENCE = "militia_defence"
    MILITIA_ORGANIZATION = "militia_organization"

    #Garrison
    GARRISON_PENETRATION_CHANCE = "garrison_penetration_chance"

    #Diplomacy
    ACCEPTANCE_OF_COMMUNIST_DIPLOMACY = "acceptance_of_cummunist_diplomacy"
    ACCEPTANCE_OF_FASCIST_DIPLOMACY = "acceptance_of_fascist_diplomacy"

    #Divisions
    DIVISION_DEFENCE_ON_CORE_TERRITORY = "division_defence_on_core_territory"
    DIVISION_ORGANIZATION = "division_organization"
    DIVISION_TRAINING_TIME = "division_training_time"
    DIVISION_ATTACK = "division_attack"
    DIVISION_SPEED = "division_speed"
    DIVISION_RECOVERY_RATE = "division_recovery_rate"
    DIVISION_ATTRITION = "division_attrition"

    #Equipment
    EQUIPMENT_CONVERSION_SPEED = "equipment_conversion_speed"
    EQUIPMENT_CAPTURE_RATIO_FACTOR = "equipment_capture_ratio_factor"
    #Trains
    TRAIN_PRODUCTION_COST = "train_production_cost"
    TRAIN_ARMOR = "train_armor"
    #Infantry
    INFANTRY_EQUIPMENT_PRODUCTION_COST = "infantry_equipment_production_cost"
    INFANTRY_DIVISION_ATTACK = "infantry_division_attack"
    INFANTRY_DIVISION_DEFENSE = "infantry_division_defense"
    #Support artillery
    SUPPORT_ARTILLERY_PRODUCTION_COST = "support_artillery_production_cost"
    #Armor technology
    ARMOR_TECHNOLOGY_MAX_SPEED = "armor_technology_max_speed"
    ARMOR_DIVISION_ATTACK = "armor_division_attack"
    ARMOR_DIVISION_DEFENSE = "armor_division_defense"
    #Artillery
    ARITLLERY_ATTACK = "artillery_attack"
    ARTILLERY_DEFENSE = "artillery_defense"
    #Paradropping
    ORGANIZATION_AFTER_PARADROPPING = "organization_after_paradropping"
    PARATROOPER_ANTI_AIR_DEFENSE = "paratrooper_anti_air_defense"

    #Planes
    #Close air support
    CLOSE_AIR_SUPPORT_GROUND_ATTACK = "close_air_support_ground_attack"
    #Fighter
    FIGHTER_PRODUCTION_COST = "fighter_production_cost"
    #Tactical bomber
    TACTICAL_BOMBER_PRODUCTION_COST = "tactical_bomber_production_cost"
    #Strategic bomber
    STRATEGIC_BOMBER_PRODUCTION_COST = "strategic_bomber_production_cost"

    AIR_SUPERIORITY = "air_superiority"
    BAD_WEATHER_PENALTY = "bad_weather_penalty"
    INTERCEPTION_MISSION_EFFICIENCY = "interception_mission_efficiency"
    AIR_SUPPORT_MISSION_EFFICIENCY = "air_support_mission_efficiency"
    GROUND_ATTACK_FACTOR = "ground_attack_factor"
    GROUND_SUPPORT = "ground_support"
    STRATEGIC_BOMBING = "strategic_bombing"
    BOMBER_DEFENSE = "bomber_defense"

    #Ships
    CAPITAL_SHIP_ATTACK = "capital_ship_attack"
    CAPITAL_SHIP_ARMOR = "capital_ship_armor"
    SCREEN_ATTACK = "screen_attack"
    SCREEN_DEFENSE = "screen_defense"
    CONVOY_RAIDING_EFFICIENCY = "convoy_raiding_efficiency"
    NAVAL_SPEED = "naval_speed"
    NAVAL_MAX_RANGE_FACTOR = "naval_max_range_factor"
    NAVAL_AA_ATTACK = "naval_aa_attack"
    SUBMARINE_ATTACK = "submarine_attack"
    SUBMARINE_DEFENSE = "submarine_defense"

    #Planning
    MAX_PLANNING_FACTOR = "max_planning_factor"

    #Experience
    DAILY_ARMY_EXPERIENCE_GAIN = "daily_army_experience_gain"
    DAILY_NAVAL_EXPERIENCE_GAIN = "daily_naval_experience_gain"
    DAILY_AIR_EXPERIENCE_GAIN = "daily_air_experience_gain"
    AIR_EXPERIENCE_GAIN = "air_experience_gain"

    #Command power
    MAX_COMMAND_POWER_INCREASE = "max_command_power_increase"

    #Doctrines
    GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN = "grand_battle_plan_doctrine_mastery_gain"
    MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN = "mobile_warfare_doctrine_mastery_gain"
    BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN = "battlefield_support_doctrine_mastery_gain"
    AIR_DOCTRINE_COST = "air_doctrine_cost"
    NAVAL_DOCTRINE_COST = "naval_doctrine_cost"
    TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN = "trade_interdiction_doctrine_mastery_gain"

    WAR_PENALTY_STABILITY_MODIFIER = "war_penalty_stability_modifier"

    #Add many more later....
