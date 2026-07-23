from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws

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
            return country.totals["conscription_law_cost"] * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.TRADE_LAW: 
            return country.totals["trade_law_cost"] * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.ECONOMY_LAW: 
            return country.totals["economy_law_cost"] * self.get_base_cost()
        if self.get_modifier_type() == modifier_classes.Modifier_classes.ADVISOR: 
            return country.totals["advisor_cost"] * self.get_base_cost()
