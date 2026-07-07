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
construction_lines = []

germany = setup_countries.create_germany()

def start_construction(building_type, state_name, country_name): 
    construction_line = create_construction_line(building_type, state_name, country_name)

    return construction_line

def finish_construction(): 
    return None

def stop_construction(): 
    return None

def day_has_passed(): 
    return None

def calculate_construction_speed(): 
    return None

def move_priority_level(): 
    return None

def create_construction_line(construction_type, state_name, country_name): 
    #construction_already_exists = check_for_construction()
    const_line = construction_line.Construction_line(
        state_name,
        country_name, 
        state_name.infrastructure_level, 
        construction_type.value, 
        calculate_assigned_civs(country_name), 
        calculate_amount_of_constructions(), 
        calculate_priority(), 
        calculate_time_left()
    )
    construction_lines.append(const_line)

    return const_line

def calculate_assigned_civs(country_name): 
    return 1

def calculate_amount_of_constructions(): 
    return 1

def calculate_priority(): 
    return 0

def calculate_time_left(): 
    return 0

def get_construction_line_list(): 
    return construction_lines

def get_construction_line_size(): 
    return len(construction_lines) 




