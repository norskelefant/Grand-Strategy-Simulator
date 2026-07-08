import hoi_simulator as hoi

import pytest

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date

@pytest.fixture
def default_date(): 
    #Creates a new Germany instance before each test
    return create_default_date()

def test_day_can_increase_by_1(default_date): 
    #Given default date

    #When the date increments
    default_date.increment_date()

    #Then the day should be 2
    assert default_date.get_day() == 2
    assert default_date.get_month() == 1
    assert default_date.get_year() == 1936

def test_month_can_increase_by_3(default_date): 
    #Given default date

    #When the date increments
    for i in range(31): 
        default_date.increment_date()

    #Then the day should be 2
    assert default_date.get_day() == 1
    assert default_date.get_month() == 2
    assert default_date.get_year() == 1936





def create_default_date(): 
    return date.Date(1, 1, 1936)













