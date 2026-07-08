class State: 
    def __init__(self, name, total_construction_slots, civs, mils, dockyards, infrastructure_level, is_coastal): 
        self.name = name
        self.total_construction_slots = total_construction_slots
        self.civs = civs
        self.mils = mils
        self.dockyards = dockyards
        self.infrastructure_level = infrastructure_level
        self.is_coastal = is_coastal

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

    def get_free_construction_slots(self, country_name): 
        return self.total_construction_slots - self.civs - self.mils - self.dockyards - country_name.get_constructions_being_done_in_state()
