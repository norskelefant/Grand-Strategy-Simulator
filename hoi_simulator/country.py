from hoi_simulator import construction_types

import math

class Country: 
    def __init__(self, name, states, tiles, resources, free_civs, civs_used_on_consumer_goods,  free_mils, free_dockyards, construction, ic, consumer_goods): 
        self.name = name
        self.states = states
        self.tiles = tiles
        self.resources = resources
        self.free_civs = free_civs
        self.civs_used_on_consumer_goods = civs_used_on_consumer_goods
        self.free_mils = free_mils
        self.free_dockyards = free_dockyards
        self.construction = construction
        self.ic = ic
        self.consumer_goods = consumer_goods

    def get_state_name(self):
        return self.name
    
    def get_states(self): 
        return self.states
    
    def get_tiles(self): 
        return self.tiles
    
    def get_resources(self): 
        return self.resources
    
    def get_total_civs(self): 
        amount = 0
        for state in self.states: 
            amount += self.states[state].get_civs()
        return amount
    
    def get_free_civs(self): 
        return self.free_civs
    
    def get_total_mils(self): 
        amount = 0
        for state in self.states: 
            amount += self.states[state].get_mils()
        return amount
    
    def get_civs_used_on_consumer_goods(self): 
        return self.civs_used_on_consumer_goods

    def get_free_mils(self): 
        return self.free_mils
    
    def get_total_dockyards(self): 
        amount = 0
        for state in self.states: 
            amount += self.states[state].get_dockyards()
        return amount
    
    def get_free_dockyards(self): 
        return self.free_dockyards

    def get_ic(self): 
        return self.ic
    
    def get_consumer_goods(self): 
        return self.consumer_goods
    
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

    def update_free_factories(self, construction_type):
        if construction_type == construction_types.Constructions.CIV: 
            print(self.get_total_civs() + self.get_total_mils())
            if self.find_amount_of_factories_needed_to_use_for_consumer_goods() > self.get_civs_used_on_consumer_goods(): 
                self.civs_used_on_consumer_goods += 1
            else: 
                self.free_civs += 1
                self.get_construction().calculate_moved_assigned_civs(self)
        #Since production has not been implemented yet, mil and dockyards counts are just added to free factories directly
        if construction_type == construction_types.Constructions.MIL: 
            if self.find_amount_of_factories_needed_to_use_for_consumer_goods() > self.get_civs_used_on_consumer_goods(): 
                self.civs_used_on_consumer_goods += 1
                self.remove_constructing_factory()
            self.free_mils += 1
        if construction_type == construction_types.Constructions.DOCKYARD: 
            self.free_dockyards += 1
    
    def calculate_free_civs_consumer_goods(self, amount): 
        return 
    
    def find_amount_of_factories_needed_to_use_for_consumer_goods(self): 
        return math.floor((self.get_total_civs() + self.get_total_mils()) * self.get_consumer_goods())
            
    def remove_constructing_factory(self): 
        if self.get_total_civs() <= 0: 
            return
        if self.get_free_civs() > 0: 
            self.free_civs -= 1
        else: 
            for construction_line in reversed(self.get_construction().get_construction_line_list()): 
                if construction_line.get_assigned_civs() > 0: 
                    construction_line.decrement_assigned_civs()
                    return

