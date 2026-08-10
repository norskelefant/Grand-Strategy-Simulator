from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

#Implement later
def create_german_leaders(): 
    return {
        "Adolf_hitler": modifier.Modifier(
            "Adolf_hitler",
            "Adolf Hitler",
            0,
            modifier_classes.Modifier_classes.LEADER,
            None,
            {
                #Just for tests working at the moment
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.0
            },
            lambda country: (
                True
            ),
        ),  
        "Ernst_thalmann_l": modifier.Modifier(
            "Ernst_thalmann_l",
            "Ernst Thälmann",
            0,
            modifier_classes.Modifier_classes.LEADER,
            None,
            {
                #Just for tests working at the moment
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.0

            },
            lambda country: (
                True
            ),
        ), 
        "Walter_ulbricht_l": modifier.Modifier(
            "Walter_ulbricht_l",
            "Walter Ulbricht",
            0,
            modifier_classes.Modifier_classes.LEADER,
            None,
            {
                #Just for tests working at the moment
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.0

            },
            lambda country: (
                True
            ),
        ),

        "Erich_raeder_l": modifier.Modifier(
            "Erich_raeder_l",
            "Erich Raeder",
            0,
            modifier_classes.Modifier_classes.LEADER,
            None,
            {
                #Just for tests working at the moment
                modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.0

            },
            lambda country: (
                True
            ),
        )

        






        
    }