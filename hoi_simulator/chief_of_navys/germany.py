from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

def create_chief_of_navys(): 
    return {
        "Erich_raeder": modifier.Modifier(
            "Erich_raeder",
            "Erich Raeder",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_NAVY,
            None,
            {
                modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK: 0.10, 
                modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR: 0.10, 
                modifier_types.Modifier_types.SCREEN_ATTACK: 0.10, 
                modifier_types.Modifier_types.SCREEN_DEFENSE: 0.10, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.is_not_current_country_leader(country, "Erich_raeder")
                and requirements.has_free_chief_of_navy_slot(country)
            ),
        ),  

        "Karl_donitz": modifier.Modifier(
            "Karl_donitz",
            "Karl Dönitz",
            200,
            modifier_classes.Modifier_classes.CHIEF_OF_NAVY,
            None,
            {
                modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN: 0.40, 
                modifier_types.Modifier_types.CONVOY_RAIDING_EFFICIENCY: 0.20, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 30
            },
            lambda country: (
                requirements.has_completed_focus(country, "Trade_interdiction")
                and requirements.has_free_chief_of_navy_slot(country)
            ),
        ),

        "Rolf_carls": modifier.Modifier(
            "Rolf_carls",
            "Rolf Carls",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_NAVY,
            None,
            {
                modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.NAVAL_SPEED: 0.10, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Re-establish_the_seekriegsleitung")
                and requirements.has_free_chief_of_navy_slot(country)
            ),
        ),




    }