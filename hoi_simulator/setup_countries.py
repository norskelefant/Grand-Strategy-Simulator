from hoi_simulator import country, state, construction

def create_germany(): 
    baden = state.State("Baden", 8, 0, 2, 0, 3, False)
    brandenburg = state.State("Brandenburg", 12, 4, 5, 0, 4, False)
    ermland_masuren = state.State("Ermland-Masuren", 4, 0, 0, 0, 3, False)
    franken = state.State("Franken", 6, 2, 0, 0, 4, False)
    hannover = state.State("Hannover", 8, 1, 2, 2, 4, True)
    hessen = state.State("Hessen", 8, 2, 1, 0, 4, False)
    hinterpommern = state.State("Hinterpommern", 4, 1, 0, 0, 3, True)
    holstein = state.State("Holstein", 8, 0, 1, 6, 3, True)
    konigsberg = state.State("Königsberg", 6, 2, 0, 0, 3, True)
    mecklenburg = state.State("Mecklenburg", 4, 0, 3, 0, 3, True)
    moselland = state.State("Moselland", 10, 3, 0, 0, 4, False)
    niederbayern = state.State("Niederbayern", 6, 0, 0, 0, 3, False)
    niederschlesien = state.State("Niederschlesien", 8, 1, 0, 0, 3, False)
    oberbayern = state.State("Oberbayern", 6, 1, 2, 0, 4, False)
    oberschlesien = state.State("Oberschlesien", 6, 0, 0, 0, 3, False)
    ostmark = state.State("Ostmark", 6, 1, 0, 0, 3, False)
    rhineland = state.State("Rhineland", 12, 4, 3, 0, 4, False)
    sachsen = state.State("Sachsen", 10, 7, 2, 0, 4, False)
    schleswig = state.State("Schleswig", 2, 0, 1, 0, 3, True)
    thuringen = state.State("Thüringen", 8, 1, 0, 0, 3, False)
    vorpommern = state.State("Vorpommern", 4, 0, 0, 0, 3, True)
    weser_ems = state.State("Weser-Ems", 6, 2, 0, 2, 3, True)
    westfalen = state.State("Westfalen", 8, 1, 3, 0, 3, False)
    wurttemberg = state.State("Württemberg", 8, 1, 5, 0, 4, False)

    germany = country.Country("Germany", 
                       {"baden": baden, "brandenburg": brandenburg, "ermland_masuren": ermland_masuren, "franken": franken, "hannover": hannover, "hessen": hessen, "hinterpommern": hinterpommern, "holstein": holstein, "konigsberg": konigsberg, "mecklenburg": mecklenburg, "moselland": moselland, "niederbayern": niederbayern, "niederschlesien": niederschlesien, "oberbayern": oberbayern, "oberschlesien": oberschlesien, "ostmark": ostmark, "rhineland": rhineland, "sachsen": sachsen, "schleswig": schleswig, "thuringen": thuringen, "vorpommern": vorpommern, "weser_ems": weser_ems, "westfalen": westfalen, "wurttemberg": wurttemberg},
                       None, None, 35, 20, 28, 28, construction.Construction())

    return germany
    

    #nummer 5