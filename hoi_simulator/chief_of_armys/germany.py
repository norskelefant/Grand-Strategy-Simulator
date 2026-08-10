from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

def create_german_chief_of_armys(): 
    return {
        "Ludwig_beck": modifier.Modifier(
            "Ludwig_beck",
            "Ludwig Beck",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_ARMY,
            None,
            {
                modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.DIVISION_ORGANIZATION: 0.08, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                True
            ),
        ),   

        "Wilhelm_keitel": modifier.Modifier(
            "Wilhelm_keitel",
            "Wilhelm Keitel",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_ARMY,
            None,
            {
                modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.DIVISION_TRAINING_TIME: -0.10, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.is_fascist(country)
            ),
        ),   

        "Werner_von_fritsch_coa": modifier.Modifier(
            "Werner_von_fritsch_coa",
            "Werner von Fritsch",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_ARMY,
            None,
            {
                modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.ARITLLERY_ATTACK: 0.15, 
                modifier_types.Modifier_types.ARTILLERY_DEFENSE: 0.10, 
                modifier_types.Modifier_types.MAX_PLANNING_FACTOR: 0.10, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.is_not_already_hired_elsewhere(country, "Werner_von_fritsch_hc")
                and requirements.has_completed_focus(country, "Prussian_artillery_doctrine")
            ),
        ),   

        "Franz_halder": modifier.Modifier(
            "Franz_halder",
            "Franz Halder",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_ARMY,
            None,
            {
                modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN: 0.30, 
                modifier_types.Modifier_types.DIVISION_ATTACK: 0.10,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Instill_auftragstaktik")
            ),
        ),

        "W_von_brauchitsch": modifier.Modifier(
            "W_von_brauchitsch",
            "W. von Brauchitsch",
            100,
            modifier_classes.Modifier_classes.CHIEF_OF_ARMY,
            None,
            {
                modifier_types.Modifier_types.DIVISION_SPEED: 0.10, 
                modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN: 0.30,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Develop_modern_maneuver_warfare")
            ),
        ),    






    }