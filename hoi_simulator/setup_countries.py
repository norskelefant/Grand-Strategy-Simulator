from hoi_simulator import country, state, construction, modifier, modifier_types, modifier_classes, economy_laws, ideologies

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
                       base_stability=70, 
                       economy_law=modifier.Modifier("Partial_mobilization", "Partial Mobilization", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}), 
                       base_war_support=30, 
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
                       trade_law=modifier.Modifier("Limited_exports", "Limited Exports", modifier_classes. Modifier_classes.TRADE_LAW, None, {modifier_types.Modifier_types.CONSTRUCTION_SPEED: 0.05, modifier_types.Modifier_types.RESEARCH_SPEED: 0.01, modifier_types.Modifier_types.FACTORY_OUTPUT: 0.05, modifier_types.Modifier_types.DOCKYARD_OUTPUT: 0.05, modifier_types.Modifier_types.RESOURCES_TO_MARKET: 0.25, modifier_types.Modifier_types.LEND_LEASE_TENSION_LIMIT: 0.20,
                       modifier_types.Modifier_types.CIVILIAN_INTELLIGENCE_TO_OTHERS: 0.10, modifier_types.Modifier_types.NAVY_INTELLIGENCE_TO_OTHERS: 0.05, modifier_types.Modifier_types.BASE_CONSTRUCTION_LINE_SPEED_BOOST: -0.05}),
                       conscription_law=None, 
                       advisors=[], 
                       industrial_concern=None, 
                       theorist=None, 
                       chief_of_army=None, 
                       chief_of_navy=None, 
                       chief_of_air_force=None, 
                       high_commanders=[], 
                       focus_tree=[], 
                       focuses_done=[], 
                       focuses_that_can_be_done=[], 
                       national_spirits=[], 
                       modifiers=[]
                       )

    germany.switch_economy_law(economy_laws.Economy_laws.PARTIAL_MOBILIZATION)

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
                                  modifier_classes.Modifier_classes.BASE, 
                                  None, 
                                  {modifier_types.Modifier_types.STABILITY: 5})
    ruling_party_popularity = modifier.Modifier("Ruling_party_popularity", 
                                                "Ruling Party Popularity",
                                                modifier_classes.Modifier_classes.BASE, 
                                                None, 
                                                {modifier_types.Modifier_types.STABILITY: 6})
    
    mefo_bills = modifier.Modifier("MEFO_bills", 
                                   "MEFO Bills",
                                   modifier_classes.Modifier_classes.NATIONAL_SPIRIT, 
                                   None, 
                                   {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: -0.10, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10, modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED: 0.10})

    pride_of_the_fleet = modifier.Modifier("Pride_of_the_fleet", 
                                           "Pride of the Fleet",
                                           modifier_classes.Modifier_classes.BASE, 
                                           None, 
                                           {modifier_types.Modifier_types.WAR_SUPPORT: 5})

    germany.modifiers.append(reichstag)
    germany.modifiers.append(ruling_party_popularity)
    germany.national_spirits.append(mefo_bills)
    germany.modifiers.append(pride_of_the_fleet)



    #25% * floor((1-(-10%))*(1-12.4%) * 100) / 100 = 0.24



    return germany

#Creates a simple Germany for test_construction. Does not have any infrastructure level buffs, or bonus buffs like construction speed, consumer goods or anything else
def create_simple_germany(): 
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

    custom_economy_law = modifier.Modifier("Custom", "Costum", modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.24})

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
                       base_stability=50, 
                       economy_law=custom_economy_law, 
                       war_support=0, 
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
                       industrial_concern=None, 
                       theorist=None, 
                       chief_of_army=None, 
                       chief_of_navy=None,
                       chief_of_air_force=None, 
                       high_commanders=[], 
                       focus_tree=[], 
                       focuses_done=[], 
                       focuses_that_can_be_done=[], 
                       national_spirits=[], 
                       modifiers=[]
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