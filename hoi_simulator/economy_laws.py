from enum import Enum

class Economy_laws(Enum): 
    #There are many rules and requirements for economy laws, which can be read from the wiki here: https://hoi4.paradoxwikis.com/Ideas#Economy_laws

    #Normal economy laws
    CIVILIAN_ECONOMY = "Civilian_economy"
    EARLY_MOBILIZATION = "Early_mobilization"
    PARTIAL_MOBILIZATION = "Partial_mobilization"
    WAR_ECONOMY = "War_economy"
    TOTAL_MOBILIZATION = "Total_mobilization"
    
    #Special economy laws
    UNDISTURBED_ISOLATION = "Undisturbed_isolation"
    ISOLATION = "Isolation"
    COLLECTIVIZED_SOCIETY = "Collectivized_society"
    NEW_ECONOMIC_POLICY = "New_economic_policy"
    TOTALER_KRIEG = "Totaler_krieg"
    CAPITAL_INVESTMENT_MODEL = "Capital_investment_model"
    NATIONAL_DEFENSE_STATE = "National_defense_state"
    WAR_COMMUNISM = "War_communism"