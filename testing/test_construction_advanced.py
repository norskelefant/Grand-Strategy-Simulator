import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game

@pytest.fixture
def advanced_germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()




















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()



