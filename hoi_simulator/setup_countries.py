from hoi_simulator import country, state, construction, modifier, modifier_types, modifier_classes, economy_laws, ideologies, advisors, chief_of_air_forces, chief_of_navys, chief_of_armys, industrial_concerns, leaders, theorists
from hoi_simulator.advisors import germany as germany_advisors
from hoi_simulator.chief_of_air_forces import germany as germany_chiefs_of_air_forces
from hoi_simulator.chief_of_armys import germany as germany_chiefs_of_armys
from hoi_simulator.chief_of_navys import germany as germany_chiefs_of_navys
from hoi_simulator.high_commanders import germany as germany_high_commanders
from hoi_simulator.industrial_concerns import germany as germany_industrial_concerns
from hoi_simulator.leaders import germany as germany_leaders
from hoi_simulator.theorists import germany as germany_theorists

#Explanation of scaled system: 
#To avoid floating point errors, the bonus system uses scaled integers. The scaled integers are 1000, so a 25% construction speed bonus is 25 and a 1% construction speed bonus is 1



def create_advanced_germany(): 
    baden = state.State("Baden", 8, 0, 2, 0, 3, False, None)
    brandenburg = state.State("Brandenburg", 12, 4, 5, 0, 4, False, None)
    ermland_masuren = state.State("Ermland-Masuren", 4, 0, 0, 0, 3, False, None)
    franken = state.State("Franken", 6, 2, 0, 0, 4, False, None)
    hannover = state.State("Hannover", 8, 1, 2, 2, 4, True, None)
    hessen = state.State("Hessen", 9, 2, 1, 0, 4, False, None)
    hinterpommern = state.State("Hinterpommern", 4, 1, 0, 0, 3, True, None)
    holstein = state.State("Holstein", 8, 0, 1, 6, 3, True, None)
    konigsberg = state.State("Königsberg", 6, 2, 0, 0, 3, True, None)
    mecklenburg = state.State("Mecklenburg", 4, 0, 3, 0, 3, True, None)
    moselland = state.State("Moselland", 10, 3, 0, 0, 4, False, None)
    niederbayern = state.State("Niederbayern", 6, 1, 0, 0, 3, False, None)
    niederschlesien = state.State("Niederschlesien", 8, 1, 0, 0, 3, False, None)
    oberbayern = state.State("Oberbayern", 6, 1, 2, 0, 4, False, None)
    oberschlesien = state.State("Oberschlesien", 6, 0, 0, 0, 3, False, None)
    ostmark = state.State("Ostmark", 6, 1, 0, 0, 3, False, None)
    rhineland = state.State("Rhineland", 12, 4, 3, 0, 4, False, None)
    sachsen = state.State("Sachsen", 10, 7, 2, 0, 4, False, None)
    schleswig = state.State("Schleswig", 2, 0, 1, 0, 3, True, None)
    thuringen = state.State("Thüringen", 8, 1, 0, 0, 3, False, None)
    vorpommern = state.State("Vorpommern", 4, 0, 0, 0, 3, True, None)
    weser_ems = state.State("Weser-Ems", 6, 2, 0, 2, 3, True, None)
    westfalen = state.State("Westfalen", 9, 1, 3, 0, 3, False, None)
    wurttemberg = state.State("Württemberg", 8, 1, 3, 0, 4, False, None)

    partial_mobilization = modifier.Modifier("Partial_mobilization", "Partial Mobilization", 0, modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, True)

    limited_exports = modifier.Modifier("Limited_exports", "Limited Exports", 0, modifier_classes. Modifier_classes.TRADE_LAW, None, {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.05, modifier_types.Modifier_types.RESEARCH_SPEED: 0.01, modifier_types.Modifier_types.FACTORY_OUTPUT: 0.05, modifier_types.Modifier_types.DOCKYARD_OUTPUT: 0.05, modifier_types.Modifier_types.RESOURCES_TO_MARKET: 0.25, modifier_types.Modifier_types.LEND_LEASE_TENSION_LIMIT: 0.20,
                       modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS: 0.10, modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS: 0.05, modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST: -0.05}, True)

    germany = country.Country(name="Germany", 
                       states={"baden": baden, "brandenburg": brandenburg, "ermland_masuren": ermland_masuren, "franken": franken, "hannover": hannover, "hessen": hessen, "hinterpommern": hinterpommern, "holstein": holstein, "konigsberg": konigsberg, "mecklenburg": mecklenburg, "moselland": moselland, "niederbayern": niederbayern, "niederschlesien": niederschlesien, "oberbayern": oberbayern, "oberschlesien": oberschlesien, "ostmark": ostmark, "rhineland": rhineland, "sachsen": sachsen, "schleswig": schleswig, "thuringen": thuringen, "vorpommern": vorpommern, "weser_ems": weser_ems, "westfalen": westfalen, "wurttemberg": wurttemberg},
                       tiles=None, 
                       resources=None, 
                       free_civs=0, 
                       civs_used_on_consumer_goods=0, 
                       free_mils=0, 
                       free_dockyards=0, 
                       construction=construction.Construction(), 
                       base_ic=4, 
                       base_stability=0.7, 
                       economy_law=partial_mobilization, 
                       base_war_support=0.3, 
                       political_power=0, 
                       population=0, 
                       fuel=0, 
                       command_power=0, 
                       convoys=0, 
                       army_exp=0, 
                       navy_exp=0, 
                       air_exp=0, 
                       ideology=ideologies.Ideologies.FASCIST, 
                       democratic_support=35, 
                       non_aligned_support=15, 
                       communist_support=10, 
                       fascist_support=40, 
                       at_war=False, 
                       countries_at_war_with=[], 
                       research_slots=4, 
                       has_researched=[], 
                       can_research=[],
                       trade_law=limited_exports,
                       conscription_law=None, 
                       advisors=[], 
                       possible_advisors=germany_advisors.create_german_advisors(),
                       industrial_concern=None, 
                       possible_industrial_concerns=germany_industrial_concerns.create_german_industrial_concerns(),
                       theorist=None, 
                       possible_theorists=germany_theorists.create_german_theorists(),
                       chief_of_army=None, 
                       possible_chiefs_of_army=germany_chiefs_of_armys.create_german_chief_of_armys(),
                       chief_of_navy=None, 
                       possible_chiefs_of_navy=germany_chiefs_of_navys.create_chief_of_navys(),
                       chief_of_air_force=None, 
                       possible_chiefs_of_air_force=germany_chiefs_of_air_forces.create_german_chief_of_air_forces(),
                       high_commanders=[], 
                       possible_high_commanders=germany_high_commanders.create_german_high_commanders(),
                       leader=None, 
                       possible_leaders=germany_leaders.create_german_leaders(),
                       focus_tree=[], 
                       focuses_done=[], 
                       focuses_that_can_be_done=[], 
                       national_spirits=[], 
                       modifiers=[], 
                       full_added_bonuses={}
                       )

    germany.full_added_bonuses = germany.create_default_bonuses_map()

    germany.add_to_full_added_bonuses(partial_mobilization)
    germany.add_to_full_added_bonuses(limited_exports)

    for each_state in germany.get_states(): 
        germany.states[each_state].set_country(germany)

    total_civs = germany.get_total_civs()
    total_mils = germany.get_total_mils()
    total_factories = total_civs + total_mils
    total_dockyards = germany.get_total_dockyards()

    germany.civs_used_on_consumer_goods = germany.find_amount_of_factories_needed_to_use_for_consumer_goods()
    germany.free_civs = total_civs - germany.civs_used_on_consumer_goods
    germany.free_mils = total_mils
    germany.free_dockyards = total_dockyards

    reichstag = modifier.Modifier("Reichstag", 
                                  "Reichstag",
                                  0,
                                  modifier_classes.Modifier_classes.BASE, 
                                  None, 
                                  {modifier_types.Modifier_types.STABILITY: 0.05}, 
                                  True)
    ruling_party_popularity = modifier.Modifier("Ruling_party_popularity", 
                                                "Ruling Party Popularity",
                                                0,
                                                modifier_classes.Modifier_classes.BASE, 
                                                None, 
                                                {modifier_types.Modifier_types.STABILITY: 0.06}, 
                                                True)
    
    mefo_bills = modifier.Modifier("MEFO_bills", 
                                   "MEFO Bills",
                                   0,
                                   modifier_classes.Modifier_classes.NATIONAL_SPIRIT, 
                                   None, 
                                   {modifier_types.Modifier_types.WAR_SUPPORT: 0.05}, 
                                   True)

    pride_of_the_fleet = modifier.Modifier("Pride_of_the_fleet", 
                                           "Pride of the Fleet",
                                           0,                                           modifier_classes.Modifier_classes.BASE, 
                                           None, 
                                           {modifier_types.Modifier_types.WAR_SUPPORT: 0.05}, 
                                           True)

    germany.modifiers.append(reichstag)
    germany.add_to_full_added_bonuses(reichstag)

    germany.modifiers.append(ruling_party_popularity)
    germany.add_to_full_added_bonuses(ruling_party_popularity)

    germany.national_spirits.append(mefo_bills)
    germany.add_to_full_added_bonuses(mefo_bills)

    germany.modifiers.append(pride_of_the_fleet)
    germany.add_to_full_added_bonuses(pride_of_the_fleet)

    #25% * floor((1-(-10%))*(1-12.4%) * 100) / 100 = 0.24

    return germany

#Creates a simple Germany for test_construction. Does not have any infrastructure level buffs, or bonus buffs like construction speed, consumer goods or anything else
def create_simple_germany(): 
    #Infrastructure levels are at 0, since the construction.py tests are made without infrastructure bonuses. Maybe change that at some point
    baden = state.State("Baden", 8, 0, 2, 0, 0, False, None)
    brandenburg = state.State("Brandenburg", 12, 4, 5, 0, 0, False, None)
    ermland_masuren = state.State("Ermland-Masuren", 4, 0, 0, 0, 0, False, None)
    franken = state.State("Franken", 6, 2, 0, 0, 0, False, None)
    hannover = state.State("Hannover", 8, 1, 2, 2, 0, True, None)
    hessen = state.State("Hessen", 9, 2, 1, 0, 0, False, None)
    hinterpommern = state.State("Hinterpommern", 4, 1, 0, 0, 0, True, None)
    holstein = state.State("Holstein", 8, 0, 1, 6, 0, True, None)
    konigsberg = state.State("Königsberg", 6, 2, 0, 0, 0, True, None)
    mecklenburg = state.State("Mecklenburg", 4, 0, 3, 0, 0, True, None)
    moselland = state.State("Moselland", 10, 3, 0, 0, 0, False, None)
    niederbayern = state.State("Niederbayern", 6, 1, 0, 0, 0, False, None)
    niederschlesien = state.State("Niederschlesien", 8, 1, 0, 0, 0, False, None)
    oberbayern = state.State("Oberbayern", 6, 1, 2, 0, 0, False, None)
    oberschlesien = state.State("Oberschlesien", 6, 0, 0, 0, 0, False, None)
    ostmark = state.State("Ostmark", 6, 1, 0, 0, 0, False, None)
    rhineland = state.State("Rhineland", 12, 4, 3, 0, 0, False, None)
    sachsen = state.State("Sachsen", 10, 7, 2, 0, 0, False, None)
    schleswig = state.State("Schleswig", 2, 0, 1, 0, 0, True, None)
    thuringen = state.State("Thüringen", 8, 1, 0, 0, 0, False, None)
    vorpommern = state.State("Vorpommern", 4, 0, 0, 0, 0, True, None)
    weser_ems = state.State("Weser-Ems", 6, 2, 0, 2, 0, True, None)
    westfalen = state.State("Westfalen", 9, 1, 3, 0, 0, False, None)
    wurttemberg = state.State("Württemberg", 8, 1, 3, 0, 0, False, None)
    
    custom_economy_law = modifier.Modifier("Custom", "Costum", 0, modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.24}, True)

    germany = country.Country(name="Germany", 
                       states={"baden": baden, "brandenburg": brandenburg, "ermland_masuren": ermland_masuren, "franken": franken, "hannover": hannover, "hessen": hessen, "hinterpommern": hinterpommern, "holstein": holstein, "konigsberg": konigsberg, "mecklenburg": mecklenburg, "moselland": moselland, "niederbayern": niederbayern, "niederschlesien": niederschlesien, "oberbayern": oberbayern, "oberschlesien": oberschlesien, "ostmark": ostmark, "rhineland": rhineland, "sachsen": sachsen, "schleswig": schleswig, "thuringen": thuringen, "vorpommern": vorpommern, "weser_ems": weser_ems, "westfalen": westfalen, "wurttemberg": wurttemberg},
                       tiles=None, 
                       resources=None, 
                       free_civs=0, 
                       civs_used_on_consumer_goods=0, 
                       free_mils=0, 
                       free_dockyards=0, 
                       construction=construction.Construction(), 
                       base_ic=4, 
                       base_stability=0.5, 
                       economy_law=custom_economy_law, 
                       base_war_support=0, 
                       political_power=0, 
                       population=0, 
                       fuel=0, 
                       command_power=0, 
                       convoys=0, 
                       army_exp=0, 
                       navy_exp=0, 
                       air_exp=0, 
                       ideology=None, 
                       democratic_support=25, 
                       non_aligned_support=25, 
                       communist_support=25, 
                       fascist_support=25, 
                       at_war=False, 
                       countries_at_war_with=[], 
                       research_slots=0, 
                       has_researched=[], 
                       can_research=[],
                       trade_law=None, 
                       conscription_law=None, 
                       advisors=[], 
                       possible_advisors={},
                       industrial_concern=None, 
                       possible_industrial_concerns={},
                       theorist=None, 
                       possible_theorists={},
                       chief_of_army=None, 
                       possible_chiefs_of_army={},
                       chief_of_navy=None,
                       possible_chiefs_of_navy={},
                       chief_of_air_force=None, 
                       possible_chiefs_of_air_force={},
                       high_commanders=[], 
                       possible_high_commanders={},
                       leader=None, 
                       possible_leaders={},
                       focus_tree=[], 
                       focuses_done=[], 
                       focuses_that_can_be_done=[], 
                       national_spirits=[], 
                       modifiers=[], 
                       full_added_bonuses={}
                       )

    for each_state in germany.get_states(): 
        germany.states[each_state].set_country(germany)

    total_civs = germany.get_total_civs()
    total_mils = germany.get_total_mils()
    total_factories = total_civs + total_mils
    total_dockyards = germany.get_total_dockyards()

    germany.civs_used_on_consumer_goods = germany.find_amount_of_factories_needed_to_use_for_consumer_goods()
    germany.free_civs = total_civs - germany.civs_used_on_consumer_goods
    germany.free_mils = total_mils
    germany.free_dockyards = total_dockyards




    return germany


    
    #Formula for consumer goods: 
    #https://www.reddit.com/r/hoi4/comments/17io39g/can_someone_explain_how_consumer_goods_percantage/
    #base_factor * math.floor(product(1-f_i) * 100) / 100
    #Starting germany consumer goods: 
    #25% * floor((1-(-10%))*(1-12.4%) * 100) / 100 = 0.24
    #Where -12.4% comes from the stability at the start of the game. Implement this later when implementing focus trees, decisions and events

    #Other example: 
    #35% * floor((1-30%)*(1-13.5%)*100) / 100

    #From research: 
    #Construction from one line to another DOES NOT carry over when the line finishes
    #Construction from one factory in a construction line to the next DOES carry over when the first factory finishes 



    #nummer 5

