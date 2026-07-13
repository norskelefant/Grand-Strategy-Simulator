from hoi_simulator import country, construction_line, construction_types, production_line, production, setup_countries, state, tile

import hoi_simulator as hoi

import math

CIV_COST = 10800
MIL_COST = 7200
NAVAL_DOCKYARD_COST = 6400

CONSTRUCTION_FACTORIES = 15

civ_ic_production = 4

class Construction: 
    def __init__(self):
        self.construction_lines = []

    def start_construction(self, construction_type, state_name, country_name): 
        check = self.check_if_construction_is_valid(construction_type, state_name, country_name)
        if check != True: 
            return
        if self.check_for_existing_construction_line(construction_type, state_name) == True and len(self.get_construction_line_list()) != 0: 
            self.increment_amount_of_constructions(construction_type, state_name)
            return
        self.create_construction_line(construction_type, state_name, country_name)

    def create_construction_line(self, construction_type, state_name, country_name): 
        assigned_civs = self.calculate_assigned_civs(construction_type, state_name, country_name)
        const_line = construction_line.Construction_line(
            state_name,
            country_name, 
            state_name.infrastructure_level, 
            construction_type.value, 
            assigned_civs, 
            1, 
            self.calculate_default_priority(), 
            self.default_time_left(construction_type, assigned_civs, state_name, country_name),
            construction_type
        )
        country_name.construction.construction_lines.append(const_line)

    def finish_construction(self, construction_line): 
        country = construction_line.get_country_name()
        construction_type = construction_line.get_construction_type()
        if construction_line.get_amount_of_constructions() == 1: 
            self.delete_construction_line(construction_line, country)
        elif construction_line.get_amount_of_constructions() > 1: 
            construction_line.decrement_amount_of_constructions()
            construction_line.reset_construction_cost(construction_type)
        country.increment_building_type(construction_type)

    #def day_has_passed(self, date): 
    #    self.calculate_remaining_time()
    
    def calculate_remaining_time(self, construction_line): 
        return None
        #construction_line.set_amount_of_time_left()

    def calculate_construction_speed(self): 
        return None

    def move_priority_level(self, construction_line, new_priority_level, country): 
        check = self.check_if_priority_level_legal(new_priority_level)
        if check == False: 
            return
        old_construction_line = self.get_construction_line_list().pop(construction_line.get_priority())
        self.get_construction_line_list().insert(new_priority_level, old_construction_line)
        self.set_new_priority_levels()
        self.calculate_moved_assigned_civs(country)

    def delete_construction_line(self, construction_line, country): 
        priority = construction_line.get_priority()
        civs_back_in_pool = construction_line.get_assigned_civs()
        country.update_free_civs(civs_back_in_pool)
        del self.construction_lines[priority]
        self.set_new_priority_levels()
        self.calculate_moved_assigned_civs(country)

    def remove_building_from_construction_line(self, construction_line): 
        construction_line.decrement_amount_of_constructions()

    def set_new_priority_levels(self): 
        for index, construction_line in enumerate(self.get_construction_line_list()): 
            construction_line.set_priority_level(index)

    def check_if_priority_level_legal(self, new_priority_level): 
        if new_priority_level < 0 or new_priority_level > self.get_construction_line_size() - 1: 
            return False
        return True

    def calculate_assigned_civs(self, construction_type, state_name, country_name): 
        amount = min(country_name.get_free_civs(), CONSTRUCTION_FACTORIES)
        country_name.use_free_civs(amount)
        return amount
    
    def calculate_moved_assigned_civs(self, country): 
        amount = country.get_total_assigned_factories_for_country()
        free_civs = country.get_free_civs()
        country.update_free_civs(amount)
        amount += free_civs
        for construction_line in self.get_construction_line_list(): 
            picked_amount = min(amount, CONSTRUCTION_FACTORIES)
            construction_line.set_assigned_civs(picked_amount)
            country.use_free_civs(picked_amount)
            amount -= picked_amount
            construction_line.amount_of_time_left(country.get_ic())

    def increment_amount_of_constructions(self, building_type, state_name): 
        construction_line = self.find_construction_line(building_type, state_name)
        construction_line.set_amount_of_constructions()

    def calculate_default_priority(self): 
        return self.get_construction_line_size()

    def default_time_left(self, construction_type, assigned_civs, state, country): 
        ic = country.get_ic()
        cost = construction_type.value
        ic_production_each_day = ic * assigned_civs
        if ic_production_each_day == 0: 
            return math.inf
        construction_speed = 1
        #Use state for construction speed later, as well as country
        time_left = math.ceil(cost / (ic_production_each_day * construction_speed))
        return time_left

    def get_construction_line_list(self): 
        return self.construction_lines

    def get_construction_line_size(self): 
        return len(self.construction_lines) 
    
    def check_if_construction_is_valid(self, construction_type, state_name, country_name): 
        if self.building_dockyard_in_non_coastal_state(construction_type, state_name) == True: 
            return False
        if self.no_free_building_slots(state_name, country_name) == True: 
            return False
        return True

    def no_free_building_slots(self, state_name, country_name): 
        return state_name.get_free_construction_slots(country_name) <= 0

    def building_dockyard_in_non_coastal_state(self, construction_type, state_name): 
        return construction_type == construction_types.Constructions.DOCKYARD and state_name.get_is_coastal() == False
    
    def check_for_existing_construction_line(self, construction_type, state_name):
        if len(self.get_construction_line_list()) == 0: 
            return False
        for construction_line in self.get_construction_line_list(): 
            if construction_line.get_construction_type() == construction_type and construction_line.get_state_name().get_name() == state_name.get_name(): 
                return True
        return False
    
    def find_construction_line(self, construction_type, state_name): 
        for construction_line in self.get_construction_line_list():
            if construction_line.get_construction_type() == construction_type and construction_line.get_state_name().get_name() == state_name.get_name(): 
                return construction_line
        return None



