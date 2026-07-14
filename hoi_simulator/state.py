from hoi_simulator import construction_types

import hoi_simulator as hoi

class State: 
    def __init__(self, name, total_construction_slots, civs, mils, dockyards, infrastructure_level, is_coastal, country): 
        self.name = name
        self.total_construction_slots = total_construction_slots
        self.civs = civs
        self.mils = mils
        self.dockyards = dockyards
        self.infrastructure_level = infrastructure_level
        self.is_coastal = is_coastal
        self.country = country

    def get_name(self):
        return self.name

    def get_total_construction_slots(self): 
        return self.total_construction_slots

    def get_civs(self): 
        return self.civs

    def get_mils(self): 
        return self.mils

    def get_dockyards(self): 
        return self.dockyards

    def get_infrastructure_level(self): 
        return self.infrastructure_level

    def get_is_coastal(self): 
        return self.is_coastal 
    
    def get_country(self): 
        return self.country
    
    def set_country(self, country_name):
        self.country = country_name

    def get_free_construction_slots(self): 
        return self.total_construction_slots - self.civs - self.mils - self.dockyards - self.get_country().get_constructions_being_done_in_state(self)
    
    def increment_building_type(self, building_type): 
        if building_type == construction_types.Constructions.CIV: 
            self.civs += 1
        if building_type == construction_types.Constructions.MIL:
            self.mils += 1
        if building_type == construction_types.Constructions.DOCKYARD:
            self.dockyards += 1

    def decrement_building_type(self, building_type): 
        if building_type == construction_types.Constructions.CIV: 
            self.civs -= 1
        if building_type == construction_types.Constructions.MIL:
            self.mils -= 1
        if building_type == construction_types.Constructions.DOCKYARD:
            self.dockyards -= 1

    def get_amount_of_building_type(self, building_type): 
        if building_type == construction_types.Constructions.CIV: 
            return self.get_civs()
        if building_type == construction_types.Constructions.MIL: 
            return self.get_mils()
        if building_type == construction_types.Constructions.DOCKYARD: 
            return self.get_dockyards()

    
