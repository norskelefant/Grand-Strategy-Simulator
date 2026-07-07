class Construction_line: 
    def __init__(self, state_name, country_name, infrastructure_level, construction_cost, assigned_civs, amount_of_constructions, priority, time_left): 
        self.state_name = state_name
        self.country_name = country_name
        self.infrastructure_level = infrastructure_level
        self.construction_cost = construction_cost
        self.assigned_civs = assigned_civs
        self.amount_of_constructions = amount_of_constructions
        self.priority = priority
        self.time_left = time_left

    def get_state_name(self): 
        return self.state_name
    
    def get_country_name(self): 
        return self.country_name
    
    def get_infrastructure_level(self): 
        return self.infrastructure_level
    
    def get_construction_cost(self): 
        return self.construction_cost
    
    def get_assigned_civs(self): 
        return self.assigned_civs
    
    def get_amount_of_constructions(self): 
        return self.amount_of_constructions
    
    def get_priority(self): 
        return self.priority
    
    def get_time_left(self): 
        return self.time_left
