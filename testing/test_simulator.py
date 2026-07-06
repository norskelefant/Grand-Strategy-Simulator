from main import get_test
from hoi_simulator.construction import construction_test

def test_get_test(): 
    assert get_test(5) == True

def test_construction_test(): 
    assert construction_test(2) == 2



