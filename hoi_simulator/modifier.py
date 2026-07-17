class modifier: 
    def __init__(self, name, modifier_type, end_date, modifier_source, modifier_bonus): 
        self.name = name
        self.modifier_type = modifier_type
        self.end_date = end_date
        self.modifier_source = modifier_source
        self.modifier_bonus = modifier_bonus

    def get_name(self): 
        return self.name

    def get_modifier_type(self): 
        return self.modifier_type
    
    def get_end_date(self): 
        return self.end_date
    
    def get_modifier_source(self): 
        return self.modifier_source
    
    def get_modifier_bonus(self): 
        return self.modifier_bonus