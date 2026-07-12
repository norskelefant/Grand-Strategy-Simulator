class Country: 
    def __init__(self, name, states, tiles, resources, total_civs, free_civs, total_mils, free_mils, construction): 
        self.name = name
        self.states = states
        self.tiles = tiles
        self.resources = resources
        self.total_civs = total_civs
        self.free_civs = free_civs
        self.total_mils = total_mils
        self.free_mils = free_mils
        self.construction = construction

    def get_state_name(self):
        return self.name
    
    def get_states(self): 
        return self.states
    
    def get_tiles(self): 
        return self.tiles
    
    def get_resources(self): 
        return self.resources
    
    def get_total_civs(self): 
        return self.total_civs
    
    def get_free_civs(self): 
        return self.free_civs
    
    def get_total_mils(self): 
        return self.total_mils
    
    def get_free_mils(self): 
        return self.free_mils
    
    def get_total_dockyards(self): 
        amount = 0
        for state in self.states: 
            amount += state.get_dockyards()
    
    #Construction object, which has list of constructions for the country
    def get_construction(self): 
        return self.construction

    def get_constructions_being_done_in_state(self, state_name): 
        amount = 0
        for single_construction in self.get_construction().get_construction_line_list(): 
            if single_construction.get_state_name() == state_name: 
                amount += single_construction.get_amount_of_constructions()
        return amount
    
    def use_free_civs(self, amount): 
        self.free_civs -= amount

    def get_total_assigned_factories_for_country(self): 
        amount = 0
        for construction_line in self.get_construction().get_construction_line_list(): 
            amount += construction_line.get_assigned_civs()
        #amount += self.get_free_civs()
        return amount
    
    def update_free_civs(self, amount): 
        self.free_civs += amount

    def get_ic(self): 
        return 4
    
    def increment_building_type(self, building_type): 
        return None


