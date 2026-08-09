from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

class Modifier: 
    def __init__(self, id, name, base_cost, modifier_type, end_date, modifier_bonuses, requirements): 
        self.id = id
        self.name = name
        self.base_cost = base_cost
        self.modifier_type = modifier_type
        self.end_date = end_date
        self.modifier_bonuses = modifier_bonuses
        self.requirements = requirements

    def get_id(self): 
        return self.id

    def get_name(self): 
        return self.name

    def get_base_cost(self): 
        return self.base_cost

    def get_modifier_type(self): 
        return self.modifier_type
    
    def get_end_date(self): 
        return self.end_date
    
    def get_modifier_bonuses(self): 
        return self.modifier_bonuses

    def get_requirements(self): 
        return self.requirements

    def get_full_cost(self, country): 
        if self.get_modifier_type() == modifier_classes.Modifier_classes.CONSCRIPTION_LAW: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.CONSCRIPTION_LAW_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.TRADE_LAW: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.TRADE_LAW_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.ECONOMY_LAW: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.ECONOMY_LAW_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.ADVISOR: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_ADVISOR_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.THEORIST: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.THEORIST_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.INDUSTRIAL_CONCERN: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.INDUSTRIAL_CONCERN_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.CHIEF_OF_ARMY: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_ARMY_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.CHIEF_OF_NAVY: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_NAVY_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.CHIEF_OF_AIR_FORCE: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.CHIEF_OF_AIR_FORCE_COST]) * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.HIGH_COMMANDER: 
            return (1 + country.get_full_added_bonuses()[modifier_types.Modifier_types.HIGH_COMMANDER_COST]) * self.get_base_cost()
    

    def requirements_met(self, country): 
        return self.requirements(country)

