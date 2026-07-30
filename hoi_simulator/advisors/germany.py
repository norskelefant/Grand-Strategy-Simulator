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
                and requirements.has_not_hired_advisor(country, "Walther_Funk") 
                and requirements.has_free_advisor_slot(country)
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
            and requirements.has_not_hired_advisor(country, "Hjalmer_Schacht")
            and requirements.has_not_hired_advisor(country, "Ludwog Erhard")
            and requirements.has_free_advisor_slot(country)
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
            lambda country: ((requirements.is_fascist(country) 
            #https://www.reddit.com/r/hoi4/comments/10mygfi/what_does_reinstated_nazi_leadership_mean/
            or requirements.event_has_happened(country, "Reinstated_nazi_leadership"))
            and requirements.has_free_advisor_slot(country)
            ),
        ),

        #Have come this far
        "Hanns_kerrl": modifier.Modifier(
            "Hanns_kerrl",
            "Hanns Kerrl",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER: 0.10,
                modifier_types.Modifier_types.RESEARCH_SPEED: -0.025,
                modifier_types.Modifier_types.RESITANCE_GROWTH_SPEED: -0.02, 
                modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING: 0.002
            },
            lambda country: ((requirements.is_fascist(country) 
                or requirements.event_has_happened(country, "Reinstated_nazi_leadership")
            )
            and requirements.has_not_completed_focus(country, "Hegemony_of_the_ss")
            and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Reinhard_heydrich": modifier.Modifier(
            "Reinhard_heydrich",
            "Reinhard Heydrich",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.RESITANCE_GROWTH_SPEED: -0.05,
                modifier_types.Modifier_types.OPERATIVE_SLOTS: 1, 
                modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS: -0.002, 
                modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS: -0.002
            },
            lambda country: (
                (requirements.is_fascist(country)
                or requirements.event_has_happened(country, "Reinstated_nazi_leadership"))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Joachim_von_ribbentrop": modifier.Modifier(
            "Joachim_von_ribbentrop",
            "Joachim von Ribbentrop",
            50,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST: -0.25,
                modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION: 5, 
                modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME: -0.15, 
                modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR: 0.10, 
                modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENCE: 0.25
            },
            lambda country: (
                (requirements.is_fascist(country) and requirements.has_completed_focus(country, "Reorganize_the_wermacht") or requirements.event_has_happened(country, "Reinstated_nazi_leadership"))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Konstantin_von_Neurath": modifier.Modifier(
            "Konstantin_von_Neurath",
            "Konstantin von Neurath",
            50,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY: -0.25,
                modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST: -0.50,
                modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR: 0.10,
                modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN: -0.001, 
                modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED: 0.01
            },
            lambda country: (
                requirements.is_not_communist(country)
                and requirements.has_completed_focus(country, "Heed_von_Neuraths_concerns")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Leni_riefenstahl": modifier.Modifier(
            "Leni_riefenstahl",
            "Leni Riefenstahl",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENCE: 0.15,
                modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER: 0.05,
                modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER: 0.05,
                modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES: 0.001
            },
            lambda country: (
                (requirements.event_has_happened(country, "Reinstated_nazi_leadership") or requirements.has_completed_focus(country, "Fund_the_fil_department"))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Wilhelm_canaris": modifier.Modifier(
            "Wilhelm_canaris",
            "Wilhelm Canaris",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.OPERATIVE_SLOTS: 1,
                modifier_types.Modifier_types.AGENCY_UPGRADE_TIME: -0.20
            },
            lambda country: (
                requirements.has_created_intelligence_agency(country) 
                and requirements.has_not_completed_focus(country, "Reorganize_secret_services")
                and requirements.has_not_completed_focus(country,"Start_the_proletarian_revolution")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Hans_oster": modifier.Modifier(
            "Hans_oster",
            "Hans Oster",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.STABILITY: 0.10,
                modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT: -0.05
            },
            lambda country: (
                requirements.has_completed_focus(country, "Rally_the_wehrmacht")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Alfred_hugenberg": modifier.Modifier(
            "Alfred_hugenberg",
            "Alfred Hugenberg",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER: 0.10,
                modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT: 0.10
            },
            lambda country: (
                (requirements.has_completed_focus(country, "Revive_the_kaiserreich") or requirements.has_completed_focus(country, "Invite_german_monarchists"))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Alfred_hugenberg": modifier.Modifier(
            "Alfred_hugenberg",
            "Alfred Hugenberg",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER: 0.10,
                modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT: 0.10
            },
            lambda country: (
                (requirements.has_completed_focus(country, "Revive_the_kaiserreich") or requirements.has_completed_focus(country, "Invite_german_monarchists"))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Carl_friedrich_goerdeler": modifier.Modifier(
            "Carl_friedrich_goerdeler",
            "Carl Friedrich Goerdeler",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY: 0.05,
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.05,
                modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY: -0.05, 
                modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR: 0.15
            },
            lambda country: (
                (requirements.has_completed_focus(country, "Revive_the_kaiserreich") or requirements.has_completed_focus(country, "Invite_german_monarchists") or requirements.has_completed_focus(country, "Strive_for_conservative_values"))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Carl_friedrich_goerdeler": modifier.Modifier(
            "Carl_friedrich_goerdeler",
            "Carl Friedrich Goerdeler",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY: 0.05,
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.05,
                modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY: -0.05, 
                modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR: 0.15
            },
            lambda country: (
                (requirements.has_completed_focus(country, "Revive_the_kaiserreich") or requirements.has_completed_focus(country, "Invite_german_monarchists") or requirements.has_completed_focus(country, "Strive_for_conservative_values"))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Julius_leber": modifier.Modifier(
            "Julius_leber",
            "Julius Leber",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.STABILITY: 0.05,
                modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENCE: 0.15            },
            lambda country: (
                requirements.has_completed_focus(country, "Re-establish_free_elections")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Kurt_Schumacher": modifier.Modifier(
            "Kurt_Schumacher",
            "Kurt Schumacher",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT: 0.10           },
            lambda country: (
                requirements.has_completed_focus(country, "Re-establish_free_elections")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Theodor_heuss": modifier.Modifier(
            "Theodor_heuss",
            "Theodor Heuss",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.10,
                modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT: 0.05           },
            lambda country: (
                requirements.has_completed_focus(country, "Monarchist_sentiment")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Theodor_heuss": modifier.Modifier(
            "Theodor_heuss",
            "Theodor Heuss",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.10,
                modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT: 0.05           },
            lambda country: (
                requirements.has_completed_focus(country, "Monarchist_sentiment")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Hans_luther": modifier.Modifier(
            "Hans_luther",
            "Hans Luther",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.10,
                modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED: 0.10,
                modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: 0.10
            },
            lambda country: (
                requirements.is_not_fascist(country)
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Ludwig_erhard": modifier.Modifier(
            "Ludwig_erhard",
            "Ludwig Erhard",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.15,
                modifier_types.Modifier_types.TRADE_LAW_COST: -0.33,
                modifier_types.Modifier_types.ECONOMY_LAW_COST: -0.33
            },
            lambda country: (
                requirements.has_completed_focus(country, "Prioritize_economic_growth")
                and requirements.has_not_hired_advisor(country, "Walther_funk")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Hermann_ehrhardt": modifier.Modifier(
            "Hermann_ehrhardt",
            "Hermann Ehrhardt",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR: 0.03,
                modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENCE: 0.15,
                modifier_types.Modifier_types.MILITIA_ATTACK: 0.05, 
                modifier_types.Modifier_types.MILITIA_DEFENCE: 0.05, 
                modifier_types.Modifier_types.MILITIA_ORGANIZATION: 0.05, 
            },
            lambda country: (
                requirements.is_non_aligned(country)
                and requirements.has_completed_focus(country, "Reestablish_the_freikorps")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Adolf_friedrich_of_mecklenburg": modifier.Modifier(
            "Adolf_friedrich_of_mecklenburg",
            "Adolf Friedrich of Mecklenburg",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.NON_CORE_MANPOWER: 0.02,
                modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE: -0.10
            },
            lambda country: (
                (requirements.is_non_aligned(country) or requirements.is_democratic(country))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Wilhelm_von_gayl": modifier.Modifier(
            "Wilhelm_von_gayl",
            "Wilhelm von Gayl",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.NON_CORE_MANPOWER: 0.02,
                modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE: -0.10
            },
            lambda country: (
                requirements.is_non_aligned(country)
                and requirements.has_completed_focus(country, "Reestablish_the_freikorps")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Andreas_hermes": modifier.Modifier(
            "Andreas_hermes",
            "Andreas Hermes",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.MONTHLY_POPULATION: 0.10,
                modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES: -0.10,
                modifier_types.Modifier_types.FACTORY_OUTPUT: 0.05, 
                modifier_types.Modifier_types.DOCKYARD_OUTPUT: 0.05
            },
            lambda country: (
                requirements.has_completed_focus(country, "Monarchist_sentiment")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Dietrich_bonhoeffer": modifier.Modifier(
            "Dietrich_bonhoeffer",
            "Dietrich Bonhoeffer",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER: 0.10,
                modifier_types.Modifier_types.RESITANCE_GROWTH_SPEED: -0.03, 
                modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT: -0.03, 
                modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY: -25,
                modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT: -0.05,
                modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY: -50
            },
            lambda country: (
                (requirements.is_non_aligned(country) or requirements.is_democratic(country))
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Ernst_thalmann": modifier.Modifier(
            "Ernst_thalmann",
            "Ernst Thälmann",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.05,
                modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT: 0.10
            },
            lambda country: (
                requirements.event_has_happened(country, "Ernst_thalman_has_been_freed_from_prison") 
                and requirements.is_not_country_leader(country, "Ernst_thalmann")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Walter_ulbricht": modifier.Modifier(
            "Walter_ulbricht",
            "Walter Ulbricht",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.10,
                modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT: 0.05
            },
            lambda country: (
                requirements.is_not_country_leader(country, "Ernst_thalmann")
                and (requirements.has_completed_focus(country, "Start_the_proletarian_revolution") or requirements.is_communist(country))
                and requirements.has_not_completed_focus(country, "Revive_the_kaiserreich")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Wilhelm_zaisser": modifier.Modifier(
            "Wilhelm_zaisser",
            "Wilhelm Zaisser",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.OPERATIVE_SLOTS: 1,
                modifier_types.Modifier_types.AGENCY_UPGRADE_TIME: 0.20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Formalize_the_intelligence_wing")
                and requirements.has_free_advisor_slot(country)
            ),
        ),

        "Otto_ruhle": modifier.Modifier(
            "Otto_ruhle",
            "Otto Rühle",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.10,
                modifier_types.Modifier_types.RESEARCH_SPEED: 0.05, 
                modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT: 0.05
            },
            lambda country: (
                requirements.has_completed_focus(country, "Legacy_of_the_spartacus_league")
                and requirements.has_free_advisor_slot(country)
            ),
        ), 

        "Hermann_duncker": modifier.Modifier(
            "Hermann_duncker",
            "Hermann Duncker",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION: 0.05,
                modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH: 0.05, 
                modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN: 0.05
            },
            lambda country: (
                requirements.is_communist(country)
                and requirements.has_free_advisor_slot(country)
            ),
        ), 

        "August_thalheimer": modifier.Modifier(
            "August_thalheimer",
            "August Thalheimer",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY: 0.05,
                modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY: -0.05, 
                modifier_types.Modifier_types.FACTORY_OUTPUT: 0.05
            },
            lambda country: (
                requirements.is_communist(country)
                and requirements.has_free_advisor_slot(country)
            ),
        ), 

        "Bernhard_bastlein": modifier.Modifier(
            "Bernhard_bastlein",
            "Bernhard Bästlein",
            150,
            modifier_classes.Modifier_classes.ADVISOR,
            None,
            {
                modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR: 0.05,
                modifier_types.Modifier_types.DIVISION_DEFENCE_ON_CORE_TERRITORY: 0.05, 
            },
            lambda country: (
                requirements.has_completed_focus(country, "Start_the_proletarian_revolution")
                and requirements.has_free_advisor_slot(country)
            ),
        ), 



    }