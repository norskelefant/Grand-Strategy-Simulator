from country import *
from state import *



def create_germany(): 
    baden = State("Baden", 8, 0, 2, 3)
    brandenburg = State("Brandenburg", 12, 4, 5, 4)
    ermland_masuren = State("Ermland-Masuren", 4, 0, 0, 3)
    franken = State("Franken", 6, 2, 0, 4)
    hannover = State("Hannover", 8, 1, 2, 4)
    hessen = State("Hessen", 8, 2, 1, 4)
    hinterpommern = State("Hinterpommern", 4, 1, 0, 3)
    holstein = State("Holstein", 8, 0, 1, 3)
    konigsberg = State("Königsberg", 6, 2, 0, 3)
    mecklenburg = State("Mecklenburg", 4, 0, 3, 3)
    moselland = State("Moselland", 10, 3, 0, 4)
    niederbayern = State("Niederbayern", 6, 0, 0, 3)
    niederschlesien = State("Niederschlesien", 8, 1, 0, 3)
    oberbayern = State("Oberbayern", 6, 1, 2, 4)
    oberschlesien = State("Oberschlesien", 6, 0, 0, 3)
    ostmark = State("Ostmark", 6, 1, 0, 3)
    rhineland = State("Rhineland", 12, 4, 3, 4)
    sachsen = State("Sachsen", 10, 7, 2, 4)
    schleswig = State("Schleswig", 2, 0, 1, 3)
    thuringen = State("Thüringen", 8, 1, 0, 3)
    vorpommern = State("Vorpommern", 4, 0, 0, 3)
    weser_ems = State("Weser-Ems", 6, 2, 0, 3)
    westfalen = State("Westfalen", 8, 1, 3, 3)
    wurttemberg = State("Württemberg", 8, 1, 5, 4)

    germany = Country("Germany", 
                      [baden, brandenburg, ermland_masuren, franken, hannover, hessen, hinterpommern, holstein, konigsberg, mecklenburg, moselland, niederbayern, niederschlesien, oberbayern, oberschlesien, ostmark, rhineland, sachsen, schleswig, thuringen, vorpommern, weser_ems, westfalen, wurttemberg],
                      None, None, 35, 20, 28, 28)

    return germany
    