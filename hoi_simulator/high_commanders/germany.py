from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

def create_german_high_commanders(): 
    return {
        "Gerd_von_rundstedt": modifier.Modifier(
            "Gerd_von_rundstedt",
            "Gerd von Rundstedt",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.DIVISION_RECOVERY_RATE: 0.08, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                True
            ),
        ),          

        "Werner_von_fritsch": modifier.Modifier(
            "Werner_von_fritsch",
            "Werner von Fritsch",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.DIVISION_ATTRITION: 0.08, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.is_not_already_hired_elsewhere(country, "Werner_von_fritsch")
                and requirements.has_not_completed_focus(country, "Reorganize_the_wehrmacht")
            ),
        ),  

        "Gunther_lutjens": modifier.Modifier(
            "Gunther_lutjens",
            "Günther Lütjens",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR: 0.10, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                True
            ),
        ),    

        "Ferdinand_schörner": modifier.Modifier(
            "Ferdinand_schörner",
            "Ferdinand Schörner",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK: 0.10, 
                modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE: 0.15,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                True
            ),
        ),           

        "Erich_bey": modifier.Modifier(
            "Erich_bey",
            "Erich Bey",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.NAVAL_AA_ATTACK: 0.15, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                True
            ),
        ),   

        "Viktor_schutze": modifier.Modifier(
            "Viktor_schutze",
            "Viktor Schütze",
            50,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.SUBMARINE_ATTACK: 0.10, 
                modifier_types.Modifier_types.SUBMARINE_DEFENSE: 0.05,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 10
            },
            lambda country: (
                True
            ),
        ), 

        "Josef_kammhuber": modifier.Modifier(
            "Josef_kammhuber",
            "Josef Kammhuber",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY: 0.10, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                True
            ),
        ),   

        "Erwin_rommel": modifier.Modifier(
            "Erwin_rommel",
            "Erwin Rommel",
            200,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK: 0.15, 
                modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE: 0.15,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 30
            },
            lambda country: (
                requirements.has_completed_focus(country, "Adopt_new_panzer_doctrine")
            ),
        ),  

        "Kurt_student": modifier.Modifier(
            "Kurt_student",
            "Kurt Student",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING: 1.80, 
                modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE: 0.15,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Falschirmjager")
            ),
        ),  

        "Hugo_sperrle": modifier.Modifier(
            "Hugo_sperrle",
            "Hugo Sperrle",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY: 0.10, 
                modifier_types.Modifier_types.GROUND_ATTACK_FACTOR: 0.05,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Dive_bombers")
            ),
        ),  

        "Erhard_milch": modifier.Modifier(
            "Erhard_milch",
            "Erhard Milch",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.GROUND_SUPPORT: 0.15, 
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Tactical_bombers")
            ),
        ),  

        "Robert_knauss": modifier.Modifier(
            "Robert_knauss",
            "Robert Knauss",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.STRATEGIC_BOMBING: 0.05, 
                modifier_types.Modifier_types.BOMBER_DEFENSE: 0.02,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Uralbomber_program")
            ),
        ), 

        "Alfred_becker": modifier.Modifier(
            "Alfred_becker",
            "Alfred Becker",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST: -0.15, 
                modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED: 0.10,
                modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR: 0.05,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                requirements.has_completed_focus(country, "Salvage_captured_equipment")
            ),
        ), 

        "Walter_dornberger": modifier.Modifier(
            "Walter_dornberger",
            "Walter Dornberger",
            100,
            modifier_classes.Modifier_classes.HIGH_COMMANDER,
            None,
            {
                modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED: 0.10, 
                modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED: 0.10,
                modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 20
            },
            lambda country: (
                (requirements.has_completed_focus(country, "Rocketry_innovations") or requirements.has_completed_focus(country, "Wonder_weapons") or requirements.has_completed_focus(country, "Glorious_mechanical_machinations"))
            ),
        )
    }