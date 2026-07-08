from hoi_simulator import country, construction_line, construction_types, production_line, production, setup_countries, state, tile

import hoi_simulator as hoi

CIV_COST = 10800
MIL_COST = 7200
NAVAL_DOCKYARD_COST = 6400

CONSTRUCTION_FACTORIES = 15

day = 1
month = 1
year = 1936

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
        const_line = construction_line.Construction_line(
            state_name,
            country_name, 
            state_name.infrastructure_level, 
            construction_type.value, 
            self.calculate_assigned_civs(country_name), 
            1, 
            self.calculate_priority(), 
            self.calculate_time_left(),
            construction_type.name
        )
        country_name.construction.construction_lines.append(const_line)

    def finish_construction(self): 
        return None

    def stop_construction(self): 
        return None

    def day_has_passed(self): 
        return None

    def calculate_construction_speed(self): 
        return None

    def move_priority_level(self): 
        return None
    
    def calculate_assigned_civs(self, country_name): 
        return 1

    def increment_amount_of_constructions(self, building_type, state_name): 
        construction_line = self.find_construction_line(building_type, state_name)
        construction_line.set_amount_of_constructions()

    def calculate_priority(self): 
        return 0

    def calculate_time_left(self): 
        return 0

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
            if construction_line.get_construction_type() == construction_type.name and construction_line.get_state_name().get_name() == state_name.get_name(): 
                return True
        return False
    
    def find_construction_line(self, construction_type, state_name): 
        for construction_line in self.get_construction_line_list():
            if construction_line.get_construction_type() == construction_type.name and construction_line.get_state_name().get_name() == state_name.get_name(): 
                return construction_line
        return None



