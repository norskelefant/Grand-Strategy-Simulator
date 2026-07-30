from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

def create_german_chief_of_air_forces(): 
    return {
        "Albert_kesselring": modifier.Modifier(
            "Albert_kesselring",
            "Albert Kesselring",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_AIR_FORCE,
            None,
            {
                modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN: 0.10,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_free_chief_of_air_slot(country)
            ),
        ),  

        "Hermann_goring": modifier.Modifier(
            "Hermann_goring",
            "Hermann Göring",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_AIR_FORCE,
            None,
            {
                modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN: 0.20, 
                modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST: -0.025,
                modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST: -0.025, 
                modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST: -0.025, 
                modifier_types.Modifier_types.AIR_SUPERIORITY: 0.05, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 10
            },
            lambda country: (
                (requirements.is_fascist(country) or requirements.event_has_happened(country, "Reinstated_nazi_leadership"))
                and requirements.has_free_chief_of_air_slot(country)
            ),
        ),  

        "Ritter_von_greim": modifier.Modifier(
            "Ritter_von_greim",
            "Ritter von Greim",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_AIR_FORCE,
            None,
            {
                modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.BAD_WEATHER_PENALTY: -0.20,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "expanding_the_luftwaffe")
                and requirements.has_free_chief_of_air_slot(country)
            ),
        ),  

        "Helmuth_wilberg": modifier.Modifier(
            "Helmuth_wilberg",
            "Helmuth Wilberg",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_AIR_FORCE,
            None,
            {
                modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN: 0.40, 
                modifier_types.Modifier_types.AIR_SUPERIORITY: 0.15,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 30
            },
            lambda country: (
                requirements.is_not_fascist(country)
                and requirements.has_completed_focus(country, "Reorganize_the_luftwaffe")
                and requirements.has_free_chief_of_air_slot(country)
            ),
        ),  



    }

