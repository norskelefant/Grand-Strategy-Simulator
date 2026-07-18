from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies

import math

class Country: 
    def __init__(self, name, states, tiles, resources, free_civs, civs_used_on_consumer_goods,  free_mils, free_dockyards, construction, base_ic, modifiers, base_stability, economy_law, base_war_support, political_power, population, fuel, command_power, convoys, army_exp, navy_exp, air_exp, ideology, democratic_support, non_aligned_support, communist_support, fascist_support, at_war, countries_at_war_with, research_slots, has_researched, trade_law, conscription_law, advisors, industrial_concern, theorist, chief_of_army, chief_of_navy, chief_of_air_force, high_commanders): 
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
        self.modifiers = modifiers
        self.base_stability = base_stability
        self.economy_law = economy_law
        self.base_war_support = base_war_support
        self.political_power = political_power
        #manpower to be calculated later on using population and modifiers
        self.population = population
        self.fuel = fuel
        self.command_power = command_power
        self.convoys = convoys
        self.army_exp = army_exp
        self.navy_exp = navy_exp
        self.air_exp = air_exp
        self.ideology = ideology
        self.democratic_support = democratic_support
        self.non_aligned_support = non_aligned_support
        self.communist_support = communist_support
        self.fascist_support = fascist_support
        self.at_war = at_war
        self.countries_at_war_with = countries_at_war_with
        self.research_slots = research_slots
        self.has_researched = has_researched
        self.trade_law = trade_law
        self.conscription_law = conscription_law
        self.advisors = advisors
        self.industrial_concern = industrial_concern
        self.theorist = theorist
        self.chief_of_army = chief_of_army
        self.chief_of_navy = chief_of_navy
        self.chief_of_air_force = chief_of_air_force
        self.high_commanders = high_commanders

    #Getter methods
    def get_state_name(self):
        return self.name
    
    def get_states(self): 
        return self.states
    
    def get_tiles(self): 
        return self.tiles
    
    def get_resources(self): 
        return self.resources
    
    def get_free_civs(self): 
        return self.free_civs
    
    def get_civs_used_on_consumer_goods(self): 
        return self.civs_used_on_consumer_goods

    def get_free_mils(self): 
        return self.free_mils

    def get_free_dockyards(self): 
        return self.free_dockyards

    #Construction object, which has list of constructions for the country
    def get_construction(self): 
        return self.construction

    def get_base_ic(self): 
        return self.base_ic
    
    def get_modifiers(self): 
        return self.modifiers
    
    def get_base_stability(self): 
        return self.base_stability
    
    def get_economy_law(self): 
        return self.economy_law

    def get_base_war_support(self): 
        return self.base_war_support

    def get_political_power(self): 
        return self.political_power
    
    def get_population(self): 
        return self.population
    
    def get_fuel(self): 
        return self.fuel
    
    def get_command_power(self): 
        return self.command_power
    
    def get_convoys(self): 
        return self.convoys
    
    def get_army_exp(self): 
        return self.army_exp
    
    def get_navy_exp(self): 
        return self.navy_exp
    
    def get_air_exp(self): 
        return self.air_exp
    
    def get_ideology(self): 
        return self.ideology
    
    def get_democratic_support(self): 
        return self.democratic_support
    
    def get_non_aligned_support(self): 
        return self.non_aligned_support
    
    def get_communist_support(self): 
        return self.communist_support
    
    def get_fascist_support(self): 
        return self.fascist_support
    
    def get_is_at_war(self): 
        return self.at_war

    def get_countries_at_war_with(self): 
        return self.countries_at_war_with
    
    def get_research_slots(self): 
        return self.research_slots
    
    def get_has_researched(self): 
        return self.has_researched
    
    def get_trade_law(self): 
        return self.trade_law
    
    def get_concription_law(self): 
        return self.conscription_law
    
    def get_advisors(self): 
        return self.advisors
    
    def get_industrial_concern(self): 
        return self.industrial_concern
    
    def get_theorist(self): 
        return self.theorist
    
    def get_chief_of_army(self): 
        return self.chief_of_army
    
    def get_chief_of_navy(self): 
        return self.chief_of_navy
    
    def get_chief_of_air_force(self): 
        return self.chief_of_air_force
    
    def get_high_commanders(self): 
        return self.high_commanders

    #Construction speed is calculated as follows
    #construction_per_civ_with_respect_to_coal * (1 + sum(modifiers)) * infrastructure_construction
    #Also note that coal at maximum can reduce ic to 4 for any factory, but it also gives a construction speed debuff in general
    #This function does not implement coal yet
    def get_total_civs(self): 
        amount = 0
        for state in self.states: 
            amount += self.states[state].get_civs()
        return amount

    def get_total_mils(self): 
        amount = 0
        for state in self.states: 
            amount += self.states[state].get_mils()
        return amount
        
    def get_total_dockyards(self): 
        amount = 0
        for state in self.states: 
            amount += self.states[state].get_dockyards()
        return amount
    
    def get_construction_speed_bonuses(self): 
        bonus = 1
        for modifier in self.get_modifiers():
            if modifier_types.Modifier_types.CONSTRUCTION_SPEED in modifier.get_modifier_bonuses(): 
                bonus += modifier.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSTRUCTION_SPEED, 0)
        return bonus
    
    def is_of_modifier_type(self, modifier_type): 
        if modifier_type == modifier_types.Modifier_types.CONSTRUCTION_SPEED: 
            return True
        return False
        
    def get_base_consumer_goods(self): 
        return self.get_consumer_goods_from_economy_law()
    
    def get_consumer_goods_from_economy_law(self): 
        if modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR in self.economy_law.get_modifier_bonuses(): 
            return self.economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR, 0)
    
    def get_floor_consumer_goods(self): 
        bonus = 1
        for modifier in self.get_modifiers(): 
            if modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR in modifier.get_modifier_bonuses(): 
                bonus *= 1 - modifier.get_modifier_bonuses().get(modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR, 0)
        return bonus
    
    #25% * floor((1-(-10%))*(1-12.4%) * 100) / 100 = 0.24

    def get_consumer_goods(self): 
        return self.get_base_consumer_goods() * math.floor(self.get_floor_consumer_goods() * 100) / 100
    
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

    def get_full_stability(self): 
        bonus = self.get_base_stability()
        for modifier in self.get_modifiers():
            #The get method here is for dictionaries. Note that the second argument of 0 is for if nothing something is not a stability modifier
            bonus += modifier.get_modifier_bonuses().get(modifier_types.Modifier_types.STABILITY, 0)
        return bonus
    
    def switch_economy_law(self, new_law): 
        if new_law == self.get_economy_law(): 
            return
        #Re
        if self.get_political_power() < 150: 
            return
        if new_law == economy_laws.Economy_laws.CIVILIAN_ECONOMY and self.can_switch_to_civilian_economy() == True:
            self.economy_law = modifier.Modifier("Civilian_economy", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.35, modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: -0.30, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: -0.30})
        elif new_law == economy_laws.Economy_laws.EARLY_MOBILIZATION and self.can_switch_to_early_mobilization() == True:
            self.economy_law = modifier.Modifier("Early_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.30, modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: -0.10, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: -0.10})
        elif new_law == economy_laws.Economy_laws.PARTIAL_MOBILIZATION and self.can_switch_to_partial_mobilization() == True: 
            self.economy_law = modifier.Modifier("Partial_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10})
        elif new_law == economy_laws.Economy_laws.WAR_ECONOMY and self.can_switch_to_war_economy() == True: 
            self.economy_law = modifier.Modifier("War_economy", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.20, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.20})
        elif new_law == economy_laws.Economy_laws.TOTAL_MOBILIZATION and self.can_switch_to_total_mobilization() == True: 
            self.economy_law = modifier.Modifier("Total_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.15, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.30})
        self.remove_political_power(150)

    def can_switch_to_civilian_economy(self): 
        return True

    def can_switch_to_early_mobilization(self): 
        return self.get_full_war_support() > 15
    
    def can_switch_to_partial_mobilization(self): 
        return self.get_full_war_support() > 25
    
    def can_switch_to_war_economy(self): 
        if self.get_full_war_support() <= 50: 
            return False
        if self.is_fascist_or_communist() == True: 
            return True
        elif self.get_is_at_war() == True and self.get_number_of_factories_enemy_country_with_most_factories_has() > (0.40 * self.get_total_factories()): 
            return True
        return False
    
    def is_fascist_or_communist(self): 
        if self.get_ideology() == ideologies.Ideologies.FASCIST or self.get_ideology() == ideologies.Ideologies.FASCIST: 
            return True
        return False
    
    def can_switch_to_total_mobilization(self): 
        return self.get_is_at_war() and self.get_full_war_support() > 80 and self.get_number_of_factories_enemy_country_with_most_factories_has() > (0.50 * self.get_total_factories())
    
    def is_ideology_fascist_or_communist(self): 
        return self.get_ideology() == ideologies.Ideologies.FASCIST or self.get_ideology() == ideologies.Ideologies.COMMUNIST
    
    def get_number_of_factories_enemy_country_with_most_factories_has(self): 
        number_of_factories_list = []
        for country in self.get_countries_at_war_with(): 
            number_of_factories_list.append(country.get_total_factories())
        return max(number_of_factories_list)
    
    def get_total_factories(self): 
        return self.get_total_civs() + self.get_total_mils() + self.get_total_dockyards()
    
    #Only used when creating country
    def set_economy_law(self, new_law): 
        if new_law == economy_laws.Economy_laws.CIVILIAN_ECONOMY:
            self.economy_law = modifier.Modifier("Civilian_economy", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.35, modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: -0.30, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: -0.30})
        elif new_law == economy_laws.Economy_laws.EARLY_MOBILIZATION:
            self.economy_law = modifier.Modifier("Early_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.30, modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: -0.10, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: -0.10})
        elif new_law == economy_laws.Economy_laws.PARTIAL_MOBILIZATION: 
            self.economy_law = modifier.Modifier("Partial_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10})
        elif new_law == economy_laws.Economy_laws.WAR_ECONOMY: 
            self.economy_law = modifier.Modifier("War_economy", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.20, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.20})
        elif new_law == economy_laws.Economy_laws.TOTAL_MOBILIZATION: 
            self.economy_law = modifier.Modifier("Total_mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.15, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.30})

    def add_political_power(self, amount): 
        self.political_power += amount

    def remove_political_power(self, amount): 
        self.political_power -= amount

    def get_full_war_support(self): 
        full_war_support = self.get_base_war_support()
        for modifier in self.get_modifiers(): 
            full_war_support += modifier.get_modifier_bonuses().get(modifier_types.Modifier_types.WAR_SUPPORT, 0)
        return full_war_support

    def add_base_war_support(self, amount): 
        self.base_war_support += amount
        if self.get_base_war_support() > 100: 
            self.base_war_support = 100
        
    def change_ideology(self, new_ideology): 
        self.ideology = new_ideology

    def declare_war(self, country): 
        if self.get_is_at_war() == False: 
            self.set_at_war(True)
        self.add_country_to_countries_at_war(country)

    def set_at_war(self, arg): 
        self.at_war = arg

    def add_country_to_countries_at_war(self, country): 
        self.countries_at_war_with.append(country)