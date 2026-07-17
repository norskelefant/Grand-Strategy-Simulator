from hoi_simulator import construction_types, modifier_types

import math

class Country: 
    def __init__(self, name, states, tiles, resources, free_civs, civs_used_on_consumer_goods,  free_mils, free_dockyards, construction, base_ic, base_consumer_goods, modifiers): 
        self.name = name
        self.states = states
        self.tiles = tiles
        self.resources = resources
        self.free_civs = free_civs
        self.civs_used_on_consumer_goods = civs_used_on_consumer_goods
        self.free_mils = free_mils
        self.free_dockyards = free_dockyards
        self.construction = construction
        self.base_ic = base_ic
        self.base_consumer_goods = base_consumer_goods
        self.modifiers = modifiers


        #self.stability = stability
        #self.war_support = war_support
        #self.political_power = political_power
        #self.manpower = manpower
        #self.fuel = fuel
        #self.command_power = command_power
        #self.convoys = convoys
        #self.army_exp = army_exp
        #self.navy_exp = navy_exp
        #self.air_exp = air_exp
        
  

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

    def get_base_ic(self): 
        return self.base_ic

    #Construction speed is calculated as follows
    #construction_per_civ_with_respect_to_coal * (1 + sum(modifiers)) * infrastructure_construction
    #Also note that coal at maximum can reduce ic to 4 for any factory, but it also gives a construction speed debuff in general
    #This function does not implement coal yet
    def get_construction_speed_bonuses(self): 
        bonus = 1
        for modifier in self.get_modifiers():
            if self.is_of_modifier_type(modifier_types.Modifier_types.CONSTRUCTION_SPEED) == True: 
                bonus += modifier.get_modifier_bonus()
        return bonus
    
    def is_of_modifier_type(self, modifier_type): 
        if modifier_type == modifier_types.Modifier_types.CONSTRUCTION_SPEED: 
            return True
        return False
        
    def get_base_consumer_goods(self): 
        return self.base_consumer_goods
    
    def get_floor_consumer_goods(self): 
        bonus = 1
        for modifier in self.get_modifiers(): 
            if self.is_of_modifier_type(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR) == True: 
                bonus *= 1 - modifier.get_modifier_bonus()
        return bonus
    
    #25% * floor((1-(-10%))*(1-12.4%) * 100) / 100 = 0.24

    def get_consumer_goods(self): 
        return self.get_base_consumer_goods() * math.floor(self.get_floor_consumer_goods() * 100) / 100
    
    def get_modifiers(self): 
        return self.modifiers
    
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
                
    def add_constructing_factory(self): 
        self.free_civs += 1
        for construction_line in reversed(self.get_construction().get_construction_line_list()): 
            if construction_line.get_assigned_civs() > 15: 
                construction_line.increment_assigned_civs()
                return
        
    def update_free_factories_after_deletion(self, construction_type): 
        if construction_type == construction_types.Constructions.CIV: 
            if self.find_amount_of_factories_needed_to_use_for_consumer_goods() < self.get_civs_used_on_consumer_goods() or self.find_amount_of_factories_needed_to_use_for_consumer_goods() > self.get_total_civs(): 
                self.civs_used_on_consumer_goods -= 1
            else: 
                if self.get_free_civs() > 0: 
                    self.free_civs -= 1
                else: 
                    self.remove_constructing_factory()
                    self.get_construction().calculate_moved_assigned_civs(self)
        #Since production has not been implemented yet, mil and dockyards counts are just removed from free factories directly
        if construction_type == construction_types.Constructions.MIL: 
            if self.find_amount_of_factories_needed_to_use_for_consumer_goods() < self.get_civs_used_on_consumer_goods(): 
                self.civs_used_on_consumer_goods -= 1
                self.free_civs += 1
                #self.add_constructing_factory()
            self.free_mils -= 1
        if construction_type == construction_types.Constructions.DOCKYARD: 
            self.free_dockyards -= 1



