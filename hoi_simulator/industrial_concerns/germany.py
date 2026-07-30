from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

def create_german_industrial_concerns(): 
    return {
        "IG_farben": modifier.Modifier(
            "IG_farben",
            "IG Farben",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED: 0.05,
                modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED: 0.15
            },
            lambda country: (
                requirements.has_free_industrial_concern_slot(country)
            ),
        ),

        "Krupp": modifier.Modifier(
            "Krupp",
            "Krupp",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.COAL: 6,
                modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY: 0.05,
                modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED: 0.15
            },
            lambda country: (
                requirements.has_free_industrial_concern_slot(country)
            ),
        ),

        "Siemens": modifier.Modifier(
            "Siemens",
            "Siemens",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION: -0.10,
                modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED: 0.15
            },
            lambda country: (
                requirements.has_free_industrial_concern_slot(country)
            ),
        ),   

        "Vereinigte_stahlwerke": modifier.Modifier(
            "Vereinigte_stahlwerke",
            "Vereinigte Stahlwerke",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY: 0.10,
                modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY: -0.15, 
                modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED: 0.15
            },
            lambda country: (
                requirements.has_free_industrial_concern_slot(country)
            ),
        ),   

        "Deutsche_reichsbahn": modifier.Modifier(
            "Deutsche_reichsbahn",
            "Vereinigte Reichsbahn",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED: 0.15,
                modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED: 0.15, 
                modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED: 0.15, 
                modifier_types.Modifier_types.TRAIN_PRODUCTION_COST: -0.25, 
                modifier_types.Modifier_types.TRAIN_ARMOR: 0.15
            },
            lambda country: (
                requirements.has_free_industrial_concern_slot(country)
            ),
        ),  

        "Philipp_holzmann": modifier.Modifier(
            "Philipp_holzmann",
            "Philipp Holzmann",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED: 0.10,
                modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED: 0.10
            },
            lambda country: (
                requirements.has_free_industrial_concern_slot(country)
            ),
        ),  

        "RWE": modifier.Modifier(
            "RWE",
            "RWE",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.075,
                modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED: 0.05
            },
            lambda country: (
                requirements.has_free_industrial_concern_slot(country)
            ),
        ),  

        "Reichswerke": modifier.Modifier(
            "Reichswerke",
            "Reichswerke",
            150,
            modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN,
            None,
            {
                modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY: 0.05,
                modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.05, 
                modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY: -0.05, 
                modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED: 0.05, 
                modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED: 0.05, 
                modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST: -0.025, 
                modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST: -0.025
            },
            lambda country: (
                requirements.has_completed_focus(country, "Establish_the_reichswerke")
                and requirements.has_free_industrial_concern_slot(country)
            ),
        )















    }