import math
from enum import Enum

class Construction_line: 
    def __init__(self, state_name, country_name, infrastructure_level, construction_cost, assigned_civs, amount_of_constructions, priority, time_left, construction_type): 
        self.state_name = state_name
        self.country_name = country_name
        self.infrastructure_level = infrastructure_level
        self.construction_cost = construction_cost
        self.assigned_civs = assigned_civs
        self.amount_of_constructions = amount_of_constructions
        self.priority = priority
        self.time_left = time_left
        self.construction_type = construction_type
    
    def __str__(self): 
        return self.state_name.get_name() + " " + self.construction_type

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
    
    def get_construction_type(self): 
        return self.construction_type
    
    def set_amount_of_constructions(self): 
        self.amount_of_constructions += 1

    def set_priority_level(self, index): 
        self.priority = index

    def set_assigned_civs(self, amount): 
        self.assigned_civs = amount
    
    def decrement_assigned_civs(self): 
        self.assigned_civs -= 1

    def increment_assigned_civs(self):
        self.assigned_civs += 1

    def decrement_amount_of_constructions(self): 
        self.amount_of_constructions -= 1

    def calculate_construction_cost(self, ic): 
        if self.construction_cost == 0: 
            self.construction_cost = 0 
        if self.get_assigned_civs() == 0: 
            self.construction_cost = self.construction_cost
        else: 
            self.construction_cost -= self.get_assigned_civs() * ic

    def reset_construction_cost(self, construction_type): 
        self.construction_cost = construction_type.value

    def amount_of_time_left(self, ic): 
        if self.get_assigned_civs() == 0: 
            self.time_left = math.inf
            return
        self.time_left = math.ceil(self.get_construction_cost() / (self.get_assigned_civs() * ic))

    def set_amount_of_time_left(self, time): 
        self.time_left = math.ceil(time)

    def day_has_passed(self, ic): 
        self.calculate_construction_cost(ic)
        self.amount_of_time_left(ic)

    def check_for_finished_buildings(self): 
        if self.get_construction_cost() <= 0: 
            construction_cost_left = self.get_construction_cost()
            self.get_country_name().get_construction().finish_construction(self)
            self.reduce_construction_cost(construction_cost_left)

    def pass_to_next_month(self, ic, days_to_pass): 
        for i in range(days_to_pass): 
            self.day_has_passed(ic)
            self.check_for_finished_buildings()

    def reduce_construction_cost(self, cost): 
        self.construction_cost += cost
