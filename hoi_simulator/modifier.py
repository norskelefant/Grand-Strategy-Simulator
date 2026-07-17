class Modifier: 
    def __init__(self, name, modifier_type, end_date, modifier_bonuses): 
        self.name = name
        self.modifier_type = modifier_type
        self.end_date = end_date
        self.modifier_bonuses = modifier_bonuses

    def get_name(self): 
        return self.name

    def get_modifier_type(self): 
        return self.modifier_type
    
    def get_end_date(self): 
        return self.end_date
    
    def get_modifier_bonuses(self): 
        return self.modifier_bonuses