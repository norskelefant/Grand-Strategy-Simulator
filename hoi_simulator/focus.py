class Focus: 
    def __init__(self, id, name, duration, prerequisite_focuses, mutually_exclusive_focuses, requirements, effects): 
        self.id = id
        self.name = name
        self.duration = duration
        self.prerequisite_focuses = prerequisite_focuses
        self.mutually_exclusive = mutually_exclusive_focuses
        self.requirements = requirements
        self.effects = effects

    def get_id(self): 
        return self.id

    def get_name(self): 
        return self.name

    def get_duration(self): 
        return self.duration

    def get_prerequisite_focuses(self): 
        return self.prerequisite_focuses

    def get_mutually_exclusive_focuses(self): 
        return self.mutually_exclusive_focuses

    def get_requirements(self): 
        return self.requirements

    def get_effects(self): 
        return self.effects