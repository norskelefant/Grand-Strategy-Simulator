from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

def create_german_theorists(): 
    return {
        "Werner_von_blomberg": modifier.Modifier(
            "Werner_von_blomberg",
            "Werner von Blomberg",
            150,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN: 0.15
            },
            lambda country: (
                requirements.has_not_completed_focus(country, "Reorganize_the_wehrmacht")
                and requirements.has_free_theorist_slot(country)
            ),
        ),   

        "Erich_von_manstein": modifier.Modifier(
            "Erich_von_manstein",
            "Erich von Manstein",
            150,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN: 0.15
            },
            lambda country: (
                requirements.has_free_theorist_slot(country)
            ),
        ),   

        "W_von_richthofen": modifier.Modifier(
            "W_von_richthofen",
            "W. von Richthofen",
            150,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN: 0.15
            },
            lambda country: (
                requirements.has_free_theorist_slot(country)
            ),
        ),   

        "Walther_wever": modifier.Modifier(
            "Walther_wever",
            "Walther Wever",
            100,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.AIR_DOCTRINE_COST: -0.10
            },
            lambda country: (
                requirements.has_free_theorist_slot(country)
            ),
        ),   

        "Otto_ciliax": modifier.Modifier(
            "Otto_ciliax",
            "Otto Ciliax",
            100,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.NAVAL_DOCTRINE_COST: -0.10
            },
            lambda country: (
                requirements.has_free_theorist_slot(country)
            ),
        ),   

        "Heinz_guderian": modifier.Modifier(
            "Heinz_guderian",
            "Heinz Guderian",
            200,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED: 0.10, 
                modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN: 0.15
            },
            lambda country: (
                requirements.has_completed_focus(country, "Adopt_new_panzer_doctrine")
                and requirements.has_free_theorist_slot(country)
            ),
        ),   

        "Alfred_saalwachter": modifier.Modifier(
            "Alfred_saalwachter",
            "Alfred Saalwächter",
            150,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN: 0.15
            },
            lambda country: (
                requirements.has_completed_focus(country, "Wolfpack_tatics")
                and requirements.has_free_theorist_slot(country)
            ),
        ),   

        "Ernst_udet": modifier.Modifier(
            "Ernst_udet",
            "Ernst Udet",
            100,
            modifier_classes.Modifier_classes.THEORIST,
            None,
            {
                modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK: 0.10, 
                modifier_types.Modifier_types.AIR_DOCTRINE_COST: -0.10
            },
            lambda country: (
                requirements.has_completed_focus(country, "Dive_bombers")
                and requirements.has_free_theorist_slot(country)
            ),
        )










    }