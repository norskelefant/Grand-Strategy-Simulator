from hoi_simulator import construction_types, modifier_types, modifier_classes, economy_laws, modifier, ideologies, trade_laws, requirements

import math

#For this dictionary, the idea is later to add special economy laws to them, which includes country specific ones. Of course special requirements still need to be done
POSSIBLE_ECONOMY_LAWS = {"Civilian_economy": modifier.Modifier("Civilian_economy", 
                            "Civilian Economy", 
                            150,
                            modifier_classes. Modifier_classes.ECONOMY_LAW, 
                            None, 
                            {modifier_types.Modifier_types.BASE_CONSUMER_GOODS: 0.35, modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST: 0.30, modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST: 0.30, modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION: -0.30, modifier_types.Modifier_types.FUEL_GAIN_PER_OIL: -0.40, modifier_types.Modifier_types.FUEL_CAPACITY: -0.25, modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: -0.30, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: -0.30}, 
                            lambda country: country.can_switch_to_civilian_economy()), 
                         "Early_mobilization": modifier.Modifier("Early_mobilization", 
                            "Early Mobilization",
                            150,
                            modifier_classes.Modifier_classes.ECONOMY_LAW, 
                            None, 
                            {modifier_types.Modifier_types.BASE_CONSUMER_GOODS: 0.30, modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION: -0.15, modifier_types.Modifier_types.FUEL_GAIN_PER_OIL: -0.25, modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: -0.10, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: -0.10},
                            lambda country: country.can_switch_to_early_mobilization()), 
                         "Partial_mobilization": modifier.Modifier("Partial_mobilization",
                            "Partial Mobilization", 
                            150,
                            modifier_classes.Modifier_classes.ECONOMY_LAW, 
                            None, 
                            {modifier_types.Modifier_types.BASE_CONSUMER_GOODS: 0.25, modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST: -0.10, modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST: -0.10, modifier_types.Modifier_types.FUEL_GAIN_PER_OIL: -0.10, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, 
                            lambda country: country.can_switch_to_partial_mobilization()), 
                         "War_economy": modifier.Modifier("War_economy", 
                            "War Economy", 
                            150,
                            modifier_classes.Modifier_classes.ECONOMY_LAW, 
                            None, 
                            {modifier_types.Modifier_types.BASE_CONSUMER_GOODS: 0.20, modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST: -0.20, modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST: -0.20, modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.20}, 
                            lambda country: country.can_switch_to_war_economy()), 
                         "Total_mobilization": modifier.Modifier("Total_mobilization", 
                            "Total Mobilization",
                            150,
                            modifier_classes.Modifier_classes.ECONOMY_LAW, 
                            None, 
                            {modifier_types.Modifier_types.RECRUITABLE_POPULATION: -3, modifier_types.Modifier_types.BASE_CONSUMER_GOODS: 0.15, modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST: -0.30, modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST: -0.30, modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION: 0.50, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.30},
                            lambda country: country.can_switch_to_total_mobilization())
                         }

POSSIBLE_TRADE_LAWS = {"Free_trade": modifier.Modifier("Free_trade", 
                            "Free Trade",
                            150,
                            modifier_classes.Modifier_classes.TRADE_LAW, 
                            None, 
                            {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.15, modifier_types.Modifier_types.RESEARCH_SPEED: 0.10, modifier_types.Modifier_types.FACTORY_OUTPUT: 0.15, modifier_types.Modifier_types.DOCKYARD_OUTPUT: 0.15, modifier_types.Modifier_types.RESOURCES_TO_MARKET: 0.80, modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS: 0.40, modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS: 0.20, modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER: 0.05}, 
                            lambda country: country.can_switch_to_free_trade()), 
                         "Export_focus": modifier.Modifier("Export_focus", 
                            "Export Focus", 
                            150,
                            modifier_classes.Modifier_classes.TRADE_LAW, 
                            None, 
                            {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.10, modifier_types.Modifier_types.RESEARCH_SPEED: 0.05, modifier_types.Modifier_types.FACTORY_OUTPUT: 0.10, modifier_types.Modifier_types.DOCKYARD_OUTPUT: 0.10, modifier_types.Modifier_types.RESOURCES_TO_MARKET: 0.50, modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS: 0.20, modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS: 0.10, modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER: 0.10}, 
                            lambda country: country.can_switch_to_export_focus()), 
                         "Limited_exports": modifier.Modifier("Limited_exports", 
                            "Limited Exports", 
                            150,
                            modifier_classes.Modifier_classes.TRADE_LAW, 
                            None, 
                            {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.05, modifier_types.Modifier_types.RESEARCH_SPEED: 0.01, modifier_types.Modifier_types.FACTORY_OUTPUT: 0.05, modifier_types.Modifier_types.DOCKYARD_OUTPUT: 0.05, modifier_types.Modifier_types.RESOURCES_TO_MARKET: 0.25, modifier_types.Modifier_types.LEND_LEASE_TENSION_LIMIT: 0.20,
                            modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS: 0.10, modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS: 0.05, modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST: -0.05}, 
                            lambda country: country.can_switch_to_limited_exports()),
                         "Closed_economy": modifier.Modifier("Closed_economy", 
                            "Closed Economy",
                            150,
                            modifier_classes.Modifier_classes.TRADE_LAW, 
                            None, 
                            {modifier_types.Modifier_types.RESOURCES_TO_MARKET: 0.00, modifier_types.Modifier_types.LEND_LEASE_TENSION_LIMIT: 0.40, modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST: -0.10, modifier_types.Modifier_types.CAN_ACCESS_INTERNATIONAL_MARKET: False}, 
                            lambda country: country.can_switch_to_closed_economy())
                         }

POSSIBLE_CONSCRIPTION_LAWS = None

class Country: 
    def __init__(self, name, states, tiles, resources, free_civs, civs_used_on_consumer_goods,  free_mils, free_dockyards, construction, base_ic, base_stability, economy_law, base_war_support, political_power, population, fuel, command_power, convoys, army_exp, navy_exp, air_exp, ideology, democratic_support, non_aligned_support, communist_support, fascist_support, at_war, countries_at_war_with, research_slots, has_researched, can_research, trade_law, conscription_law, advisors, possible_advisors, industrial_concern, possible_industrial_concerns, theorist, possible_theorists, chief_of_army, possible_chiefs_of_army, chief_of_navy, possible_chiefs_of_navy, chief_of_air_force, possible_chiefs_of_air_force, high_commanders, possible_high_commanders, leader, possible_leaders, focus_tree, focuses_done, focuses_that_can_be_done, national_spirits, modifiers, full_added_bonuses): 
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
        self.can_research = can_research
        self.trade_law = trade_law
        self.conscription_law = conscription_law
        self.advisors = advisors
        self.possible_advisors = possible_advisors
        self.industrial_concern = industrial_concern
        self.possible_industrial_concerns = possible_industrial_concerns
        self.theorist = theorist
        self.possible_theorists = possible_theorists
        self.chief_of_army = chief_of_army
        self.possible_chiefs_of_army = possible_chiefs_of_army
        self.chief_of_navy = chief_of_navy
        self.possible_chiefs_of_navy = possible_chiefs_of_navy
        self.chief_of_air_force = chief_of_air_force
        self.possible_chiefs_of_air_force = possible_chiefs_of_air_force
        self.high_commanders = high_commanders
        self.possible_high_commanders = possible_high_commanders
        self.leader = leader
        self.possible_leaders = possible_leaders
        self.focus_tree = focus_tree
        self.focuses_done = focuses_done
        self.focuses_that_can_be_done = focuses_that_can_be_done
        self.national_spirits = national_spirits
        self.modifiers = modifiers

        #Variable that has a simple count of all added bonuses. This is calculated by going through all modifiers and adding together
        self.full_added_bonuses = full_added_bonuses

    #Getter methods
    def get_name(self):
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

    def get_full_added_bonuses(self): 
        return self.full_added_bonuses

    def get_national_spirits(self): 
        return self.national_spirits

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
    
    def get_construction_speed_bonuses(self, construction_type): 
        bonus = 1 + self.get_full_added_bonuses().get(
        modifier_types.Modifier_types.CONSTRUCTION_SPEED,
        0.0,
        )
        bonus += self.get_full_added_bonuses().get(construction_type, 0.0)
        return bonus
    
    def is_of_modifier_type(self, modifier_type): 
        if modifier_type == modifier_types.Modifier_types.CONSTRUCTION_SPEED: 
            return True
        return False
        
    def get_base_consumer_goods(self): 
        return self.get_consumer_goods_from_economy_law()
    
    def get_consumer_goods_from_economy_law(self): 
        if modifier_types.Modifier_types.BASE_CONSUMER_GOODS in self.economy_law.get_modifier_bonuses(): 
            return self.economy_law.get_modifier_bonuses().get(modifier_types.Modifier_types.BASE_CONSUMER_GOODS, 0)
    
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
        has_switched = False
        cost = POSSIBLE_ECONOMY_LAWS[new_law.value].get_full_cost(self)
        if new_law.value == self.get_economy_law().id: 
            return
        if self.get_political_power() < cost: 
            return
        if new_law == economy_laws.Economy_laws.CIVILIAN_ECONOMY and POSSIBLE_ECONOMY_LAWS["Civilian_economy"].requirements_met(self) == True: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Civilian_economy"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.EARLY_MOBILIZATION and POSSIBLE_ECONOMY_LAWS["Early_mobilization"].requirements_met(self) == True:
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Early_mobilization"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.PARTIAL_MOBILIZATION and POSSIBLE_ECONOMY_LAWS["Partial_mobilization"].requirements_met(self) == True: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Partial_mobilization"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.WAR_ECONOMY and POSSIBLE_ECONOMY_LAWS["War_economy"].requirements_met(self) == True: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["War_economy"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.TOTAL_MOBILIZATION and POSSIBLE_ECONOMY_LAWS["Total_mobilization"].requirements_met(self) == True: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Total_mobilization"]
            has_switched = True
        if has_switched == True: 
            self.remove_political_power(cost)

    def can_switch_to_civilian_economy(self): 
        return True

    def can_switch_to_early_mobilization(self): 
        if self.get_name() == "Hungary": 
            return self.get_full_war_support() > 15 and self.has_national_spirit("hun_treaty_of_trianon")
        #Turkey(more research needed to understand)
        return self.get_full_war_support() > 0.15 + 1e-12

    #From ChatGPT
    def can_switch_to_partial_mobilization(self): 
        return self.get_full_war_support() > 0.25 + 1e-12
    
    def can_switch_to_war_economy(self): 
        if self.get_full_war_support() <= 0.50 + 1e-12: 
            return False
        if self.is_fascist_or_communist() == True: 
            return True
        elif self.get_is_at_war() == True and self.get_number_of_factories_enemy_country_with_most_factories_has() > (0.40 * self.get_total_factories()): 
            return True
        return False
    
    def is_fascist_or_communist(self): 
        if self.get_ideology() == ideologies.Ideologies.FASCIST or self.get_ideology() == ideologies.Ideologies.COMMUNIST: 
            return True
        return False
    
    def can_switch_to_total_mobilization(self): 
        return self.get_is_at_war() and self.get_full_war_support() > 0.8 + 1e-12 and self.get_number_of_factories_enemy_country_with_most_factories_has() > (0.50 * self.get_total_factories())
    
    def get_number_of_factories_enemy_country_with_most_factories_has(self): 
        number_of_factories_list = []
        for country in self.get_countries_at_war_with(): 
            number_of_factories_list.append(country.get_total_factories())
        if len(number_of_factories_list) == 0: 
            return 0
        else: 
            return max(number_of_factories_list)
    
    def get_total_factories(self): 
        return self.get_total_civs() + self.get_total_mils() + self.get_total_dockyards()
    
    #Only used when creating country
    def set_economy_law(self, new_law): 
        if new_law == economy_laws.Economy_laws.CIVILIAN_ECONOMY:
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Civilian_economy"]
        elif new_law == economy_laws.Economy_laws.EARLY_MOBILIZATION:
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Early_mobilization"]
        elif new_law == economy_laws.Economy_laws.PARTIAL_MOBILIZATION: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Partial_mobilization"]
        elif new_law == economy_laws.Economy_laws.WAR_ECONOMY: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["War_economy"]
        elif new_law == economy_laws.Economy_laws.TOTAL_MOBILIZATION: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Total_mobilization"]

    def add_political_power(self, amount): 
        self.political_power += amount

    def remove_political_power(self, amount): 
        self.political_power -= amount

    def get_full_war_support(self): 
        base_war_support = self.get_base_war_support()
        other_war_support = self.get_full_added_bonuses()[modifier_types.Modifier_types.WAR_SUPPORT]
        if base_war_support + other_war_support + 1e-12 > 1.0: 
            return 1.0
        else: 
            return base_war_support + other_war_support
        
    def get_full_stability(self): 
        base_stability = self.get_base_stability()
        other_stability = self.get_full_added_bonuses()[modifier_types.Modifier_types.STABILITY]
        if base_stability + other_stability + 1e-12 > 1.0: 
            return 1.0
        else: 
            return base_stability + other_stability

    def add_base_war_support(self, amount): 
        self.base_war_support += amount
        if self.get_base_war_support() > 1.0 + 1e-12: 
            self.base_war_support = 1.0

    def add_base_stability(self, amount): 
        self.base_stability += amount
        if self.get_base_stability() > 1.0 + 1e-12: 
            self.base_stability = 1.0
        
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

    def switch_trade_law(self, new_law): 
        has_switched = False
        cost = POSSIBLE_TRADE_LAWS["Free_trade"].get_full_cost(self)
        if new_law.value == self.get_trade_law().name: 
            return
        if self.get_political_power() < cost: 
            return
        if new_law == trade_laws.Trade_laws.FREE_TRADE and POSSIBLE_TRADE_LAWS["Free_trade"].requirements_met(self) == True:
            self.trade_law = POSSIBLE_TRADE_LAWS["Free_trade"]
            has_switched = True
        elif new_law == trade_laws.Trade_laws.EXPORT_FOCUS and POSSIBLE_TRADE_LAWS["Export_focus"].requirements_met(self) == True:
            self.trade_law = POSSIBLE_TRADE_LAWS["Export_focus"]
            has_switched = True
        elif new_law == trade_laws.Trade_laws.LIMITED_EXPORTS and POSSIBLE_TRADE_LAWS["Limited_exports"].requirements_met(self) == True: 
            self.trade_law = POSSIBLE_TRADE_LAWS["Limited_exports"]
            has_switched = True
        elif new_law == trade_laws.Trade_laws.CLOSED_ECONOMY and POSSIBLE_TRADE_LAWS["Closed_economy"].requirements_met(self) == True: 
            self.trade_law = POSSIBLE_TRADE_LAWS["Closed_economy"]
            has_switched = True
        if has_switched == True: 
            self.remove_political_power(cost)

    def can_switch_to_free_trade(self): 
        return True

    def can_switch_to_export_focus(self): 
        return True
    
    def can_switch_to_limited_exports(self): 
        if self.get_ideology() == ideologies.Ideologies.DEMOCRATIC: 
            if self.get_is_at_war() == True and self.get_number_of_factories_enemy_country_with_most_factories_has() > (0.20 * self.get_total_factories()): 
                return True
            return False
        else: 
            if self.get_economy_law().id == "Partial_mobilization" or self.get_economy_law().id == "War_economy" or self.get_economy_law().id == "Total_mobilization": 
                return True
            return False

    def can_switch_to_closed_economy(self): 
        if self.get_is_at_war() == True and (self.get_ideology() == ideologies.Ideologies.FASCIST or self.get_ideology() == ideologies.Ideologies.COMMUNIST): 
            if self.get_economy_law().id == "War_economy" or self.get_economy_law().id == "Total_mobilization": 
                return True
        return False

    #Only used when creating country
    def set_trade_law(self, new_law): 
        if new_law == trade_laws.Trade_laws.FREE_TRADE:
            self.economy_law = POSSIBLE_TRADE_LAWS["Free_trade"]
        elif new_law == trade_laws.Trade_laws.EXPORT_FOCUS:
            self.economy_law = POSSIBLE_TRADE_LAWS["Export_focus"]
        elif new_law == trade_laws.Trade_laws.LIMITED_EXPORTS: 
            self.economy_law = POSSIBLE_TRADE_LAWS["Limited_exports"]
        elif new_law == trade_laws.Trade_laws.CLOSED_ECONOMY: 
            self.economy_law = POSSIBLE_TRADE_LAWS["Closed_economy"]

    #Wait with conscription laws till later
    def switch_conscription_law(self, new_law): 
        has_switched = False
        if new_law.value == self.get_economy_law().name: 
            return
        if self.get_political_power() < 150: 
            return
        if new_law == economy_laws.Economy_laws.CIVILIAN_ECONOMY and self.can_switch_to_civilian_economy() == True:
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Civilian_economy"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.EARLY_MOBILIZATION and self.can_switch_to_early_mobilization() == True:
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Early_mobilization"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.PARTIAL_MOBILIZATION and self.can_switch_to_partial_mobilization() == True: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Partial_mobilization"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.WAR_ECONOMY and self.can_switch_to_war_economy() == True: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["War_economy"]
            has_switched = True
        elif new_law == economy_laws.Economy_laws.TOTAL_MOBILIZATION and self.can_switch_to_total_mobilization() == True: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Total_mobilization"]
            has_switched = True        
        if has_switched == True: 
            self.remove_political_power(150)

    #Only used when creating country
    def set_conscription_law(self, new_law): 
        if new_law == economy_laws.Economy_laws.CIVILIAN_ECONOMY:
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Civilian_economy"]
        elif new_law == economy_laws.Economy_laws.EARLY_MOBILIZATION:
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Early_mobilization"]
        elif new_law == economy_laws.Economy_laws.PARTIAL_MOBILIZATION: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Partial_mobilization"]
        elif new_law == economy_laws.Economy_laws.WAR_ECONOMY: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["War_economy"]
        elif new_law == economy_laws.Economy_laws.TOTAL_MOBILIZATION: 
            self.economy_law = POSSIBLE_ECONOMY_LAWS["Total_mobilization"]

    def has_national_spirit(self): 
        return True
    
    def has_completed_focus(self): 
        return True

    def get_modifiers(self): 
        return self.modifiers

    def add_to_full_added_bonuses(self, modifier): 
        #Goes through both keys and values in get_modifier_bonuses() dictionary
        for modifier_type, modifier_value in modifier.get_modifier_bonuses().items(): 
            if modifier_type in self.get_full_added_bonuses(): 
                if modifier_type == modifier_types.Modifier_types.BASE_STABILITY: 
                    self.add_base_stability(modifier_value)
                if modifier_type == modifier_types.Modifier_types.BASE_WAR_SUPPORT: 
                    self.add_base_war_support(modifier_value)
                self.full_added_bonuses[modifier_type] += modifier_value

    def remove_from_full_added_bonuses(self, modifier): 
        for modifier_type, modifier_value in modifier.get_modifier_bonuses().items(): 
            if modifier_type in self.get_full_added_bonuses(): 
                self.full_added_bonuses[modifier_type] -= modifier_value
                #Converts numbers very close to 0 to 0
                if math.isclose(self.full_added_bonuses[modifier_type], 0.0, abs_tol=1e-12): 
                    self.full_added_bonuses[modifier_type] = 0

    def create_default_bonuses_map(self):
        defaults = {
            modifier_types.Modifier_types.CIV_CONSTRUCTION_SPEED: 0.0,
            modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.0,
            modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED: 0.0,
            modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.0,
            modifier_types.Modifier_types.SUPPLY_HUB_CONSTRUCTION_SPEED: 0.0,
            modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST: 0.0,
            modifier_types.Modifier_types.INFRASTRUCTURE_CONSTRUCTION_SPEED: 0.0,
            modifier_types.Modifier_types.RAILWAY_CONSTRUCTION_SPEED: 0.0,
        
            modifier_types.Modifier_types.MIL_TO_CIV_CONVERSION_COST: 0.0,
            modifier_types.Modifier_types.CIV_TO_MIL_CONVERSION_COST: 0.0,

            modifier_types.Modifier_types.FACTORY_OUTPUT: 0.0,
            modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_GROWTH: 0.0,
            modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_BASE: 0.0,
            modifier_types.Modifier_types.DOCKYARD_OUTPUT: 0.0,
            modifier_types.Modifier_types.PRODUCTION_EFFICIENCY_RETENTION: 0.0,
        
            modifier_types.Modifier_types.RECRUITABLE_POPULATION: 0.0,
            modifier_types.Modifier_types.RECRUITABLE_POPULATION_FACTOR: 0.0,
            modifier_types.Modifier_types.NON_CORE_MANPOWER: 0.0,
            modifier_types.Modifier_types.MONTHLY_POPULATION: 0.0,

            modifier_types.Modifier_types.RESEARCH_SPEED: 0.0,
            modifier_types.Modifier_types.INDUSTRIAL_RESEARCH_SPEED: 0.0,
            modifier_types.Modifier_types.SYNTHETIC_RESOURCES_RESEARCH_SPEED: 0.0,
            modifier_types.Modifier_types.ELECTRONICS_RESEARCH_SPEED: 0.0,
            modifier_types.Modifier_types.EXCAVATION_TECHNOLOGY_RESEARCH_SPEED: 0.0,
            modifier_types.Modifier_types.TRAINS_AND_RAILWAYS_RESEARCH_SPEED: 0.0,
            modifier_types.Modifier_types.NUCLEAR_RESEARCH_SPEED: 0.0,

            modifier_types.Modifier_types.AERODYNAMICS_AND_AVIONICS_SPECIAL_PROJECTS_SPEED: 0.0,
            modifier_types.Modifier_types.LAND_WARFARE_SPECIAL_PROJECTS_SPEED: 0.0,

            modifier_types.Modifier_types.RESOURCES_TO_MARKET: 0.0,
            modifier_types.Modifier_types.LACK_OF_RESOURCES_PENALTY: 0.0,
            modifier_types.Modifier_types.RESOURCE_GAIN_EFFICIENCY: 0.0,
            modifier_types.Modifier_types.COAL: 0.0,
            modifier_types.Modifier_types.COAL_GAIN_EFFICIENCY: 0.0,

            modifier_types.Modifier_types.FREE_REPAIR: 0.0,

            modifier_types.Modifier_types.FUEL_GAIN_PER_OIL: 0.0,
            modifier_types.Modifier_types.FUEL_CAPACITY: 0.0,

            modifier_types.Modifier_types.FACTORY_ENERGY_CONSUMPTION: 0.0,

            modifier_types.Modifier_types.BASE_STABILITY: 0.0,
            modifier_types.Modifier_types.STABILITY: 0.0,
            modifier_types.Modifier_types.OFFENSIVE_WAR_STABILITY_MODIFIER: 0.0,
            modifier_types.Modifier_types.DEFENSIVE_WAR_STABILITY_MODIFIER: 0.0,
            modifier_types.Modifier_types.WEEKLY_STABILITY: 0.0,
            modifier_types.Modifier_types.PARTY_POPULARITY_STABILITY_MODIFIER: 0.0,

            modifier_types.Modifier_types.BASE_WAR_SUPPORT: 0.0,
            modifier_types.Modifier_types.WAR_SUPPORT: 0.0,
            modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT: 0.0,
            modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_ENEMY_BOMBING: 0.0,
            modifier_types.Modifier_types.WEEKLY_WAR_SUPPORT_COMBAT_CASUALTIES: 0.0,
            modifier_types.Modifier_types.NON_COMBAT_OUT_OF_SUPPLY_PENALTIES: 0.0,

            modifier_types.Modifier_types.DAILY_DEMOCRACY_SUPPORT: 0.0,
            modifier_types.Modifier_types.DAILY_NON_ALIGNED_SUPPORT: 0.0,
            modifier_types.Modifier_types.DAILY_COMMUNIST_SUPPORT: 0.0,
            modifier_types.Modifier_types.DAILY_FASCISM_SUPPORT: 0.0,
            modifier_types.Modifier_types.IDEOLOGY_DRIFT_DEFENCE: 0.0,

            modifier_types.Modifier_types.OPERATIVE_SLOTS: 0,
            modifier_types.Modifier_types.AGENCY_UPGRADE_TIME: 0.0,
            modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS: 0.0,
            modifier_types.Modifier_types.ARMY_INTELLIGENCE_TO_OTHERS: 0.0,
            modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS: 0.0,

            modifier_types.Modifier_types.FOREIGN_SUBVERSIVE_ACTIVITIES_EFFICIENCY: 0.0,
            modifier_types.Modifier_types.SUBVERSIVE_ACTIVITIES_COST: 0.0,
            modifier_types.Modifier_types.IMPROVE_RELATIONS_MAINTAIN_COST: 0.0,
            modifier_types.Modifier_types.TRADE_DEAL_OPINION_FACTOR: 0.0,
            modifier_types.Modifier_types.FACTION_TRADE_DEAL_OPINION_FACTOR: 0.0,
            modifier_types.Modifier_types.SAME_IDEOLOGY_MONTHLY_OPINION: 0.0,

            modifier_types.Modifier_types.SUBJECT_AUTONOMY_GAIN: 0.0,

            modifier_types.Modifier_types.COMPLIANCE_GROWTH_SPEED: 0.0,
            modifier_types.Modifier_types.RESITANCE_GROWTH_SPEED: 0.0,
            modifier_types.Modifier_types.DAILY_COMPLIANCE_GAIN: 0.0,

            modifier_types.Modifier_types.JUSTIFY_WAR_GOAL_TIME: 0.0,

            modifier_types.Modifier_types.POLITICAL_POWER_GAIN: 0.0,
            modifier_types.Modifier_types.CONSCRIPTION_LAW_COST: 0.0,
            modifier_types.Modifier_types.TRADE_LAW_COST: 0.0,
            modifier_types.Modifier_types.ECONOMY_LAW_COST: 0.0,
            modifier_types.Modifier_types.POLITICAL_ADVISOR_COST: 0.0,

            modifier_types.Modifier_types.LEND_LEASE_TENSION_LIMIT: 0.0,

            modifier_types.Modifier_types.MARKET_CONSTRUCTION_BOOST_MULTIPLIER: 0.0,
            modifier_types.Modifier_types.CAN_ACCESS_INTERNATIONAL_MARKET: False,

            modifier_types.Modifier_types.MILITIA_ATTACK: 0.0,
            modifier_types.Modifier_types.MILITIA_DEFENCE: 0.0,
            modifier_types.Modifier_types.MILITIA_ORGANIZATION: 0.0,

            modifier_types.Modifier_types.GARRISON_PENETRATION_CHANCE: 0.0,

            modifier_types.Modifier_types.ACCEPTANCE_OF_COMMUNIST_DIPLOMACY: 0.0,
            modifier_types.Modifier_types.ACCEPTANCE_OF_FASCIST_DIPLOMACY: 0.0,

            modifier_types.Modifier_types.DIVISION_DEFENCE_ON_CORE_TERRITORY: 0.0,
            modifier_types.Modifier_types.DIVISION_ORGANIZATION: 0.0,
            modifier_types.Modifier_types.DIVISION_TRAINING_TIME: 0.0,
            modifier_types.Modifier_types.DIVISION_ATTACK: 0.0,
            modifier_types.Modifier_types.DIVISION_SPEED: 0.0,
            modifier_types.Modifier_types.DIVISION_RECOVERY_RATE: 0.0,
            modifier_types.Modifier_types.DIVISION_ATTRITION: 0.0,

            modifier_types.Modifier_types.EQUIPMENT_CONVERSION_SPEED: 0.0,
            modifier_types.Modifier_types.EQUIPMENT_CAPTURE_RATIO_FACTOR: 0.0,

            modifier_types.Modifier_types.TRAIN_PRODUCTION_COST: 0.0,
            modifier_types.Modifier_types.TRAIN_ARMOR: 0.0,

            modifier_types.Modifier_types.INFANTRY_EQUIPMENT_PRODUCTION_COST: 0.0,
            modifier_types.Modifier_types.INFANTRY_DIVISION_ATTACK: 0.0,
            modifier_types.Modifier_types.INFANTRY_DIVISION_DEFENSE: 0.0,

            modifier_types.Modifier_types.SUPPORT_ARTILLERY_PRODUCTION_COST: 0.0,

            modifier_types.Modifier_types.ARMOR_TECHNOLOGY_MAX_SPEED: 0.0,
            modifier_types.Modifier_types.ARMOR_DIVISION_ATTACK: 0.0,
            modifier_types.Modifier_types.ARMOR_DIVISION_DEFENSE: 0.0,

            modifier_types.Modifier_types.ARITLLERY_ATTACK: 0.0,
            modifier_types.Modifier_types.ARTILLERY_DEFENSE: 0.0,

            modifier_types.Modifier_types.ORGANIZATION_AFTER_PARADROPPING: 0.0,
            modifier_types.Modifier_types.PARATROOPER_ANTI_AIR_DEFENSE: 0.0,

            modifier_types.Modifier_types.CLOSE_AIR_SUPPORT_GROUND_ATTACK: 0.0,

            modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST: 0.0,

            modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST: 0.0,

            modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST: 0.0,

            modifier_types.Modifier_types.AIR_SUPERIORITY: 0.0,
            modifier_types.Modifier_types.BAD_WEATHER_PENALTY: 0.0,
            modifier_types.Modifier_types.INTERCEPTION_MISSION_EFFICIENCY: 0.0,
            modifier_types.Modifier_types.AIR_SUPPORT_MISSION_EFFICIENCY: 0.0,
            modifier_types.Modifier_types.GROUND_ATTACK_FACTOR: 0.0,
            modifier_types.Modifier_types.GROUND_SUPPORT: 0.0,
            modifier_types.Modifier_types.STRATEGIC_BOMBING: 0.0,
            modifier_types.Modifier_types.BOMBER_DEFENSE: 0.0,

            modifier_types.Modifier_types.CAPITAL_SHIP_ATTACK: 0.0,
            modifier_types.Modifier_types.CAPITAL_SHIP_ARMOR: 0.0,
            modifier_types.Modifier_types.SCREEN_ATTACK: 0.0,
            modifier_types.Modifier_types.SCREEN_DEFENSE: 0.0,
            modifier_types.Modifier_types.CONVOY_RAIDING_EFFICIENCY: 0.0,
            modifier_types.Modifier_types.NAVAL_SPEED: 0.0,
            modifier_types.Modifier_types.NAVAL_MAX_RANGE_FACTOR: 0.0,
            modifier_types.Modifier_types.NAVAL_AA_ATTACK: 0.0,
            modifier_types.Modifier_types.SUBMARINE_ATTACK: 0.0,
            modifier_types.Modifier_types.SUBMARINE_DEFENSE: 0.0,

            modifier_types.Modifier_types.MAX_PLANNING_FACTOR: 0.0,

            modifier_types.Modifier_types.DAILY_ARMY_EXPERIENCE_GAIN: 0.0,
            modifier_types.Modifier_types.DAILY_NAVAL_EXPERIENCE_GAIN: 0.0,
            modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN: 0.0,
            modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN: 0.0,

            modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE: 0.0,

            modifier_types.Modifier_types.GRAND_BATTLE_PLAN_DOCTRINE_MASTERY_GAIN: 0.0,
            modifier_types.Modifier_types.MOBILE_WARFARE_DOCTRINE_MASTERY_GAIN: 0.0,
            modifier_types.Modifier_types.BATTLEFIELD_SUPPORT_DOCTRINE_MASTERY_GAIN: 0.0,
            modifier_types.Modifier_types.AIR_DOCTRINE_COST: 0.0,
            modifier_types.Modifier_types.NAVAL_DOCTRINE_COST: 0.0,
            modifier_types.Modifier_types.TRADE_INTERDICTION_DOCTRINE_MASTERY_GAIN: 0.0,

            modifier_types.Modifier_types.WAR_PENALTY_STABILITY_MODIFIER: 0.0
        }

        return defaults

    def day_has_passed(self, game): 
        for modifier in self.get_modifiers().copy(): 
            if modifier.get_end_date() is None: 
                return
            if self.is_modifier_end_date_same_as_correct_date(modifier, game) == True: 
                self.remove_from_full_added_bonuses(modifier)
                self.get_modifiers().remove(modifier)
        for national_spirit in self.get_national_spirits().copy(): 
            if national_spirit.get_end_date() is None: 
                return
            if self.is_modifier_end_date_same_as_correct_date(national_spirit, game) == True:
                self.remove_from_full_added_bonuses(national_spirit) 
                self.get_national_spirits().remove(national_spirit)

    def is_modifier_end_date_same_as_correct_date(self, modifier, game): 
        if modifier.get_end_date().get_day() == game.get_date().get_day() and modifier.get_end_date().get_month() == game.get_date().get_month() and modifier.get_end_date().get_year() == game.get_date().get_year(): 
            return True
        return False

    def check_ideology(self, ideology_to_check): 
        if self.get_ideology() is ideology_to_check: 
            return True
        return False