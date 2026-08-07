import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, custom_country

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_hjalmar_schact(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany has enough political power
    germany.add_political_power(75)

    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 0

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #and the full added bonuses should be the following
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.124
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == pytest.approx(0.30)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.20

def test_hjalmar_schacht_without_fulfilling_political_power_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany does not have enough political power
    germany.hire_advisor("Hjalmar_schacht", 0)

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #but the full bonuses should remain the same as Schacht should not be hired
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

def test_hjalmar_schacht_without_fulfilling_not_communist_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany is communist
    germany.add_political_power(75)

    germany.change_ideology(ideologies.Ideologies.COMMUNIST)

    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 75

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #but the full bonuses should remain the same as Schacht should not be hired
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

def test_hjalmar_schacht_without_fulfilling_not_having_hired_walther_funk_requirement(germany, new_game): 
    #Given a normal Germany game
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #When Hjalmar Schacht is hired when Germany already has Walther Funk hired
    germany.add_political_power(225)

    germany.hire_advisor("Walther_funk", 1)

    germany.hire_advisor("Hjalmar_schacht", 0)

    assert germany.get_political_power() == 75

    #Then Hjalmar Schacht has the following bonuses
    Hjalmar_schacht = germany.find_modifier_by_id("Hjalmar_schacht")

    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.10
    assert Hjalmar_schacht.get_modifier_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

    #but the full bonuses should remain the same as Schacht should not be hired
    #25% * ((1+10%)*(1-12.4%)*(1-10%)) = 0.21681(since Walther Funk also has -10% consumer goods bonus)
    assert germany.get_consumer_goods() == 0.21681
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.124)
    #Only default 20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED] == 0.20
    #Only default 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_CONSTRUCTION_SPEED] == 0.10

def test_walther_funk(germany, new_game): 
    assert True == False

def test_franz_seldte(germany, new_game): 
    assert True == False

def test_hanns_kerrl(germany, new_game):
    assert True == False

def test_reinhard_heydrich(germany, new_game):
    assert True == False

def test_joachim_von_ribbentrop(germany, new_game):
    assert True == False

def test_konstantin_von_neurath(germany, new_game):
    assert True == False

def test_leni_riefenstahl(germany, new_game):
    assert True == False

def test_wilhelm_canaris(germany, new_game):
    assert True == False

def test_hans_oster(germany, new_game):
    assert True == False

def test_alfred_hugenberg(germany, new_game):
    assert True == False

def test_carl_friedrich_goerdeler(germany, new_game):
    assert True == False

def test_julius_leber(germany, new_game):
    assert True == False

def test_kurt_schumacher(germany, new_game):
    assert True == False

def test_theodor_heuss(germany, new_game):
    assert True == False

def test_hans_luther(germany, new_game):
    assert True == False

def test_ludwig_erhard(germany, new_game):
    assert True == False

def test_hermann_ehrhardt(germany, new_game):
    assert True == False

def test_adolf_friedrich_of_mecklenburg(germany, new_game):
    assert True == False

def test_wilhelm_von_gayl(germany, new_game):
    assert True == False

def test_andreas_hermes(germany, new_game):
    assert True == False

def test_dietrich_bonhoeffer(germany, new_game):
    assert True == False

def test_ernst_thälmann(germany, new_game):
    assert True == False

def test_walter_ulbricht(germany, new_game):
    assert True == False

def test_wilhelm_zaisser(germany, new_game):
    assert True == False

def test_otto_rühle(germany, new_game):
    assert True == False

def test_hermann_duncker(germany, new_game):
    assert True == False

def test_august_thalheimer(germany, new_game):
    assert True == False

def test_bernhard_bästlein(germany, new_game):
    assert True == False

def test_having_three_advisors(germany, new_game): 
    assert True == False

def test_replacing_an_advisor(germany, new_game): 
    assert True == False

def test_one_cannot_hire_advisors_with_illegal_slot(germany, new_game): 
    assert True == False

def test_another_country_cannot_hire_german_advisor(germany, new_game): 
    assert True == False





def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)

def get_advisor(country, name): 
    return country.get_possible_advisors()[name]
