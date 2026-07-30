from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements







def create_german_advisors(): 
    return {
            "Hjalmar_Schacht": modifier.Modifier(
            "Hjalmar_Schacht",
            "Hjalmar Schacht",
            75,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10,
                modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED: 0.10,
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.10,
            },
            lambda country: (
                requirements.is_not_communist(country)
                and requirements.has_mefo_bills(country)
                and requirements.has_not_hired_advisor("Walther_Funk") 
                and requirements.has_free_advisor_slots(country)
            ),
        ),

        "Walther_Funk": modifier.Modifier(
            "Walther_Funk",
            "Walther Funk",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.10,
                modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY: -0.05,
                modifier_types.Modifier_types.FREE_REPAIR: 0.15,
                modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED: 0.15
            },
            lambda country: (requirements.is_fascist(country) 
            and requirements.has_not_hired_advisor("Hjalmer_Schacht")
            and requirements.has_not_hired_advisor("Ludwog Erhard")
            ),

        ),

        "Franz_Seldte": modifier.Modifier(
            "Franz_Seldte",
            "Franz Seldte",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.STABILITY: -0.05,
                modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH: 0.025,
                modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE: 0.025,
                modifier_types.Modifier_types.FACTORY_OUTPUT: 0.025, 
                modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED: 0.025, 
                modifier_types.Modifier_types.RESITANCE_GROWTH_SPEED: 0.03, 
                modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED: -0.01
            },
            lambda country: (requirements.is_fascist(country) 
            #https://www.reddit.com/r/hoi4/comments/10mygfi/what_does_reinstated_nazi_leadership_mean/
            or requirements.event_has_happened("Reinstated_nazi_leadership")
            ),
        
        ),

        #Have come this far




        "Rudolf_Hess": modifier.Modifier(
            "Rudolf_Hess",
            "Rudolf Hess",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.15,
            },
            lambda country: (
                requirements.is_fascist(country)
                and requirements.is_at_peace(country)
            ),
        ),

        "Wilhelm_Canaris": modifier.Modifier(
            "Wilhelm_Canaris",
            "Wilhelm Canaris",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.OPERATIVE_SLOT: 1,
                modifier_types.Modifier_types.AGENCY_UPGRADE_TIME: -0.15,
                modifier_types.Modifier_types.ENEMY_OPERATIVE_CAPTURE_CHANCE: 0.10,
                modifier_types.Modifier_types.OWN_OPERATIVE_CAPTURE_CHANCE: -0.10,
            },
            lambda country: (
                not requirements.is_communist(country)
                and not requirements.has_removed_canaris(country)
            ),
        ),

        "Konstantin_von_Neurath": modifier.Modifier(
            "Konstantin_von_Neurath",
            "Konstantin von Neurath",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST: -0.25,
                modifier_types.Modifier_types.TRADE_OPINION_FACTOR: 0.10,
                modifier_types.Modifier_types.DIPLOMATIC_ACCEPTANCE: 10,
            },
            lambda country: (
                requirements.is_fascist(country)
                or requirements.is_non_aligned(country)
            ),
        ),

        "Joachim_von_Ribbentrop": modifier.Modifier(
            "Joachim_von_Ribbentrop",
            "Joachim von Ribbentrop",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME: -0.10,
                modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST: -0.15,
                modifier_types.Modifier_types.TRADE_OPINION_FACTOR: 0.10,
            },
            lambda country: requirements.is_fascist(country),
        ),

        "Gertrud_Scholtz_Klink": modifier.Modifier(
            "Gertrud_Scholtz_Klink",
            "Gertrud Scholtz-Klink",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR: 0.03,
                modifier_types.Modifier_types.FACTORY_OUTPUT: 0.05,
            },
            lambda country: (
                requirements.is_fascist(country)
                and requirements.is_at_war(country)
            ),
        ),

        "Alfred_Hugenberg": modifier.Modifier(
            "Alfred_Hugenberg",
            "Alfred Hugenberg",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.05,
                modifier_types.Modifier_types.FASCISM_DRIFT: 0.05,
            },
            lambda country: (
                requirements.is_fascist(country)
                or requirements.is_non_aligned(country)
            ),
        ),

        "Otto_Strasser": modifier.Modifier(
            "Otto_Strasser",
            "Otto Strasser",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.FASCISM_DRIFT: 0.12,
                modifier_types.Modifier_types.DEMOCRATIC_DRIFT: -0.05,
                modifier_types.Modifier_types.NON_ALIGNED_DRIFT: -0.05,
                modifier_types.Modifier_types.WAR_SUPPORT_FACTOR: 0.10,
                modifier_types.Modifier_types.FREE_REPAIR_FACTOR: 0.15,
            },
            lambda country: (
                requirements.is_fascist(country)
                and requirements.has_strasserist_government(country)
            ),
        ),

        "Gregor_Strasser": modifier.Modifier(
            "Gregor_Strasser",
            "Gregor Strasser",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.FASCISM_DRIFT: 0.10,
                modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR: 0.02,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.05,
            },
            lambda country: (
                requirements.is_fascist(country)
                and requirements.has_strasserist_government(country)
            ),
        ),

        "Theodor_Heuss": modifier.Modifier(
            "Theodor_Heuss",
            "Theodor Heuss",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.DEMOCRATIC_DRIFT: 0.10,
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.05,
            },
            lambda country: requirements.is_democratic(country),
        ),

        "Konrad_Adenauer": modifier.Modifier(
            "Konrad_Adenauer",
            "Konrad Adenauer",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.DEMOCRATIC_DRIFT: 0.10,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.10,
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
            },
            lambda country: requirements.is_democratic(country),
        ),

        "Kurt_Schumacher": modifier.Modifier(
            "Kurt_Schumacher",
            "Kurt Schumacher",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.DEMOCRATIC_DRIFT: 0.10,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.05,
                modifier_types.Modifier_types.FACTORY_OUTPUT: 0.05,
            },
            lambda country: requirements.is_democratic(country),
        ),

        "Carl_Friedrich_Goerdeler": modifier.Modifier(
            "Carl_Friedrich_Goerdeler",
            "Carl Friedrich Goerdeler",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: 0.10,
                modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED: 0.10,
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.05,
            },
            lambda country: (
                requirements.is_democratic(country)
                or requirements.is_non_aligned(country)
            ),
        ),

        "Franz_von_Papen": modifier.Modifier(
            "Franz_von_Papen",
            "Franz von Papen",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.NON_ALIGNED_DRIFT: 0.10,
                modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST: -0.15,
            },
            lambda country: requirements.is_non_aligned(country),
        ),

        "August_von_Mackensen": modifier.Modifier(
            "August_von_Mackensen",
            "August von Mackensen",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                # Imperial Figurehead
                modifier_types.Modifier_types.NON_ALIGNED_DRIFT: 0.10,
                modifier_types.Modifier_types.WAR_SUPPORT_FACTOR: 0.10,
                modifier_types.Modifier_types.ARMY_EXPERIENCE_GAIN_FACTOR: 0.05,
            },
            lambda country: requirements.is_non_aligned(country),
        ),

        "Crown_Prince_Wilhelm": modifier.Modifier(
            "Crown_Prince_Wilhelm",
            "Crown Prince Wilhelm",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.NON_ALIGNED_DRIFT: 0.10,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.05,
                modifier_types.Modifier_types.WAR_SUPPORT_FACTOR: 0.05,
            },
            lambda country: requirements.is_non_aligned(country),
        ),

        # ================================================================
        # COMMUNIST PATH
        # ================================================================

        "Ernst_Thaelmann": modifier.Modifier(
            "Ernst_Thaelmann",
            "Ernst Thälmann",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                # Communist Revolutionary
                modifier_types.Modifier_types.COMMUNISM_DRIFT: 0.10,
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR: 0.02,
            },
            lambda country: requirements.is_communist(country),
        ),

        "Wilhelm_Pieck": modifier.Modifier(
            "Wilhelm_Pieck",
            "Wilhelm Pieck",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.COMMUNISM_DRIFT: 0.10,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.05,
                modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENCE: 0.10,
            },
            lambda country: requirements.is_communist(country),
        ),

        "Walter_Ulbricht": modifier.Modifier(
            "Walter_Ulbricht",
            "Walter Ulbricht",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.COMMUNISM_DRIFT: 0.10,
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST: -0.15,
            },
            lambda country: requirements.is_communist(country),
        ),

        "Otto_Grotewohl": modifier.Modifier(
            "Otto_Grotewohl",
            "Otto Grotewohl",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.COMMUNISM_DRIFT: 0.05,
                modifier_types.Modifier_types.STABILITY_FACTOR: 0.10,
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.05,
            },
            lambda country: requirements.is_communist(country),
        ),

        "Ernst_Niekisch": modifier.Modifier(
            "Ernst_Niekisch",
            "Ernst Niekisch",
            150,
            modifier_classes.Modifier_classes.POLITICAL_ADVISOR,
            None,
            {
                modifier_types.Modifier_types.COMMUNISM_DRIFT: 0.10,
                modifier_types.Modifier_types.WAR_SUPPORT_FACTOR: 0.10,
                modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR: 0.02,
            },
            lambda country: (
                requirements.is_communist(country)
                or requirements.has_strasserist_government(country)
            ),
        ),


    }