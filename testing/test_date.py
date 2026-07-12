import hoi_simulator as hoi

import pytest

from hoi_simulator import date

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

def test_month_can_increase_by_1(default_date): 
    #Given default date

    #When the date increments
    for i in range(31): 
        default_date.increment_date()

    #Then the mopnth should be 2
    assert default_date.get_day() == 1
    assert default_date.get_month() == 2
    assert default_date.get_year() == 1936

def test_year_can_increase_by_1(default_date): 
    #Given default date

    #When the date increments
    for i in range(365): 
        default_date.increment_date()

    #Then the month should be 2
    assert default_date.get_day() == 1
    assert default_date.get_month() == 1
    assert default_date.get_year() == 1937

def test_three_years_can_pass(default_date): 
    #Given default date
    
    #When the year is increased by 3
    for i in range(3): 
        default_date.next_year()

    #Then the year should be 1939
    assert default_date.get_day() == 1
    assert default_date.get_month() == 1
    assert default_date.get_year() == 1939

def test_year_can_pass_at_weird_date(default_date): 
    #Given default date
    
    #When the date is made weird
    for i in range(194): 
        default_date.increment_date()
    
    assert default_date.get_day() == 14
    assert default_date.get_month() == 7
    assert default_date.get_year() == 1936

    #And the next year is gone to
    default_date.next_year()

    #Then the year should be 1937
    assert default_date.get_day() == 1
    assert default_date.get_month() == 1
    assert default_date.get_year() == 1937

def test_year_can_pass_at_weird_date_two(default_date): 
    #Given default date
    
    #When the date is made weird
    for i in range(1000): 
        default_date.increment_date()
    
    assert default_date.get_day() == 28
    assert default_date.get_month() == 9
    assert default_date.get_year() == 1938

    #And the next year is gone to
    default_date.next_year()

    #Then the year should be 1939
    assert default_date.get_day() == 1
    assert default_date.get_month() == 1
    assert default_date.get_year() == 1939

def test_month_can_pass_at_weird_date(default_date): 
    #Given default date
    
    #When the date is made weird
    for i in range(3292): 
        default_date.increment_date()
    
    assert default_date.get_day() == 8
    assert default_date.get_month() == 1
    assert default_date.get_year() == 1945

    #And the next month is gone to
    default_date.next_month()

    #Then the month should be 2
    assert default_date.get_day() == 1
    assert default_date.get_month() == 2
    assert default_date.get_year() == 1945

def test_next_month_moves_year(default_date): 
    #Given default date
    
    #When the date is made weird
    for i in range(350): 
        default_date.increment_date()
    
    assert default_date.get_day() == 17
    assert default_date.get_month() == 12
    assert default_date.get_year() == 1936

    #And the next month is gone to
    default_date.next_month()

    #Then the month should be 1 and year 1937
    assert default_date.get_day() == 1
    assert default_date.get_month() == 1
    assert default_date.get_year() == 1937



def create_default_date(): 
    return date.Date(1, 1, 1936)

#https://chatgpt.com/c/6a4f882a-5a18-83eb-b2ab-4a3eae557bbe











