from enum import Enum

class Trade_laws(Enum): 
    #There are many rules and requirements for trade laws, which can be read from the wiki here: https://hoi4.paradoxwikis.com/Ideas#Trade_laws

    #Normal trade laws
    FREE_TRADE = "Free_trade"
    EXPORT_FOCUS = "Export_focus"
    LIMITED_EXPORTS = "Limited_exports"
    CLOSED_ECONOMY = "Closed_economy"
    
    #Special trade laws
    EMBARGOED_ECONOMY = "Embargoed_economy"
    AUTARKY = "Autarky"
    SPECIAL_ECONOMIC_ZONES = "Special_economic_zones"