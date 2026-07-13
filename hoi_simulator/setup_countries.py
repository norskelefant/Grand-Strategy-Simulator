from hoi_simulator import country, state, construction

def create_germany(): 
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

    germany = country.Country("Germany", 
                       {"baden": baden, "brandenburg": brandenburg, "ermland_masuren": ermland_masuren, "franken": franken, "hannover": hannover, "hessen": hessen, "hinterpommern": hinterpommern, "holstein": holstein, "konigsberg": konigsberg, "mecklenburg": mecklenburg, "moselland": moselland, "niederbayern": niederbayern, "niederschlesien": niederschlesien, "oberbayern": oberbayern, "oberschlesien": oberschlesien, "ostmark": ostmark, "rhineland": rhineland, "sachsen": sachsen, "schleswig": schleswig, "thuringen": thuringen, "vorpommern": vorpommern, "weser_ems": weser_ems, "westfalen": westfalen, "wurttemberg": wurttemberg},
                       None, None, 0, 0, 0, 0, construction.Construction(), 4, 0.24)

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