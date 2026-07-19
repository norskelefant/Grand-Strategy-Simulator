from enum import Enum

class Conscription_laws(Enum): 
    #There are many rules and requirements for conscription laws, which can be read from the wiki here: https://hoi4.paradoxwikis.com/Ideas#Conscription_laws

    #Normal conscription laws
    DISARMED_NATION = "Disarmed_nation"
    VOLUNTEER_ONLY = "Volunteer_only"
    LIMITED_CONSCRIPTION = "Limited_conscription"
    EXTENSIVE_CONSCRIPTION = "Extensive_conscription"
    SERVICE_BY_REQUIREMENT = "Service_by_requirement"
    ALL_ADULTS_SERVE = "All_adults_serve"
    SCRAPING_THE_BARREL = "Scraping_the_barrel"

    #Special conscription laws
    THE_CHITET = "The_chitet"
    SWISS_CITIZEN_MILITIAS = "Swiss_citizen_militias"
    EXPANDED_SWISS_CITIZEN_MILITIAS = "Expanded_swiss_citizen_militias"
