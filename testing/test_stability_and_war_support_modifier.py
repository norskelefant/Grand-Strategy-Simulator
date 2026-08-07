import hoi_simulator as hoi

import pytest

import math

from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies, trade_laws

@pytest.fixture
def germany(): 
    #Creates an advanced new Germany instance before each test
    return created_advanced_germany()

@pytest.fixture
def new_game(germany): 
    #Creates a new game instance before each test, which has default date
    return create_game(germany)

def test_stability_modifier_at_50_percent(germany, new_game): 
    #Given Germany

    #When stability is 50%
    germany.add_base_stability(-0.31)

    assert germany.get_full_stability() == pytest.approx(0.50)

    #Then the bonuses should be the following
    #Only the 10% from mefo bills
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    assert germany.get_consumer_goods() == 0.275
    #Only 5% from limited exports
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.05)
    #No extra political power gain
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.10


def test_stability_modifier_at_70_percent(germany, new_game): 
    #Given Germany

    #When stability is 70%
    germany.add_base_stability(-0.11)

    assert germany.get_full_stability() == 0.70

    #Then the bonuses should be the following
    #10% from Mefo bills and -8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.02)
    #25% * ((1+10%)*(1-8%)) = 253
    assert germany.get_consumer_goods() == pytest.approx(0.253)
    #5% from limited exports and 8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.13
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.13
    #Political power gain of 4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.04
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.06


def test_stability_modifier_at_71_percent(germany, new_game): 
    #Given Germany

    #When stability is 71%
    germany.add_base_stability(-0.10)

    assert germany.get_full_stability() == 0.71

    #Then the bonuses should be the following
    #10% from Mefo bills and -8.40% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.0160
    #25% * ((1+10%)*(1-8%)) = 0.253
    assert germany.get_consumer_goods() == 0.2519
    #5% from limited exports and 8.40% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.134
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.134
    #Political power gain of 4.2%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.042
    #29 * 0.002 = 0.058
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.058

def test_stability_modifier_at_20_percent(germany, new_game): 
    #Given Germany

    #When stability is 20%
    germany.add_base_stability(-0.61)

    assert germany.get_full_stability() == pytest.approx(0.20)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * (1+10%) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -30% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == -0.25
    #Political power gain of -12%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.12
    #80 * 0.002 = 0.16
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.16

def test_stability_modifier_at_21_percent(germany, new_game): 
    #Given Germany

    #When stability is 21%
    germany.add_base_stability(-0.60)

    assert germany.get_full_stability() == pytest.approx(0.21)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * (1+10%) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -29% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == -0.24
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == -0.24
    #Political power gain of -11.6%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.116
    #79 * 0.002 = 0.158
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.158

def test_stability_modifier_at_100_percent(germany, new_game): 
    #Given Germany

    #When stability is 100%
    germany.add_base_stability(0.19)

    assert germany.get_full_stability() == 1.0

    #Then the bonuses should be the following
    #10% from Mefo bills and -20% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    #25% * ((1+10%)*(1-20%)) = 0.22
    assert germany.get_consumer_goods() == pytest.approx(0.22)
    #5% from limited exports and 20% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.25
    #Political power gain of 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    #0 * 0.002 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.0

def test_stability_modifier_at_0_percent(germany, new_game): 
    #Given Germany

    #When stability is 0%
    new_modifier = modifier.Modifier("testing_modifier", 
                                     "Testing modifier", 
                                     0, 
                                     modifier_classes.Modifier_classes.BASE, 
                                     None, 
                                     {modifier_types.Modifier_types.STABILITY: -0.16}, 
                                     True)

    germany.modifiers.append(new_modifier)
    germany.add_to_full_added_bonuses(new_modifier)

    germany.add_base_stability(-0.66)

    assert germany.get_full_stability() == 0

    #Then the bonuses should be the following
    #10% from Mefo bills
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -50% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == -0.45
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == -0.45
    #Political power gain of -20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.20
    #100 * 0.002 = 0.2
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.2

def test_stability_increased_from_60_to_70_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 60%
    germany.add_base_stability(-0.21)

    assert germany.get_full_stability() == pytest.approx(0.6)

    #Then the bonuses should be the following
    #10% from Mefo bills and -4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.06)
    #25% * ((1+10%)*(1-4%)) = 0.264
    assert germany.get_consumer_goods() == 0.264
    #5% from limited exports and 4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.09
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.09
    #Political power gain of 2%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.02
    #40 * 0.002 = 0.08
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.08

    #When stability changes to 70%
    germany.add_base_stability(0.10)

    assert germany.get_full_stability() == 0.70

    #Then the bonuses should be the following
    #10% from Mefo bills and -8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.02)
    #25% * ((1+10%)*(1-8%)) = 0.253
    assert germany.get_consumer_goods() == pytest.approx(0.253)
    #5% from limited exports and 8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.13
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.13
    #Political power gain of 4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.04
    #30 * 0.002 = 0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.06


def test_stability_decreased_from_84_to_62_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 84%
    germany.add_base_stability(0.03)

    assert germany.get_full_stability() == 0.84

    #Then the bonuses should be the following
    #10% from Mefo bills and -13.6% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.036)
    #25% * ((1+10%)*(1-13.6%)) = 0.2376
    assert germany.get_consumer_goods() == 0.2376
    #5% from limited exports and 13.6% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.186
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.186
    #Political power gain of 6.8%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.068
    #16 * 0.002 = 0.032
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.032

    #When stability changes to 62%
    germany.add_base_stability(-0.22)

    assert germany.get_full_stability() == 0.62

    #Then the bonuses should be the following
    #10% from Mefo bills and -4.8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.052)
    #25% * ((1+10%)*(1-4.8%)) = 0.2618
    assert germany.get_consumer_goods() == pytest.approx(0.2618)
    #5% from limited exports and 4.8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.098)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.098)
    #Political power gain of 2.4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.024
    #38 * 0.002 = 0.076
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.076

def test_stability_increased_from_10_to_22_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 10%
    new_modifier = modifier.Modifier("testing_modifier", 
                                     "Testing modifier", 
                                     0, 
                                     modifier_classes.Modifier_classes.BASE, 
                                     None, 
                                     {modifier_types.Modifier_types.STABILITY: -0.01}, 
                                     True)

    germany.modifiers.append(new_modifier)
    germany.add_to_full_added_bonuses(new_modifier)

    germany.add_base_stability(-0.70)

    assert germany.get_full_stability() == 0.10

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -40% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(-0.35)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(-0.35)
    #Political power gain of -16%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.16
    #90 * 0.002 = 0.18
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.18

    #When stability changes to 22%
    germany.add_base_stability(0.12)

    assert germany.get_full_stability() == 0.22

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -28% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(-0.23)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(-0.23)
    #Political power gain of -11.2%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.112
    #78 * 0.002 = 0.156
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.156

def test_stability_decreased_from_49_to_40_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 49%
    germany.add_base_stability(-0.32)

    assert germany.get_full_stability() == pytest.approx(0.49)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -1% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.04)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.04)
    #Political power gain of -0.4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.004
    #51 * 0.002 = 0.18
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == pytest.approx(0.102)

    #When stability changes to 40%
    germany.add_base_stability(-0.09)

    assert germany.get_full_stability() == pytest.approx(0.40)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -10% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(-0.05)
    #Political power gain of -4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.04
    #60 * 0.002 = 0.12
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.12

def test_stability_increased_from_50_to_57_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 50%
    germany.add_base_stability(-0.31)

    assert germany.get_full_stability() == pytest.approx(0.50)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.05)
    #Political power gain of 0%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.0
    #50 * 0.002 = 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.10

    #When stability changes to 57%
    germany.add_base_stability(0.07)

    assert germany.get_full_stability() == 0.57

    #Then the bonuses should be the following
    #10% from Mefo bills and -2.8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.072)
    #25% * ((1+10%)*(1-2.8%)) = 0.2673
    assert germany.get_consumer_goods() == pytest.approx(0.2673)
    #5% from limited exports and 2.8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.078)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.078)
    #Political power gain of 1.4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.014
    #43 * 0.002 = 0.086
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == pytest.approx(0.086)

def test_stability_decreased_from_50_to_43_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 50%
    germany.add_base_stability(-0.31)

    assert germany.get_full_stability() == pytest.approx(0.50)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.05)
    #Political power gain of 0%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.0
    #50 * 0.002 = 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.10

    #When stability changes to 43%
    germany.add_base_stability(-0.07)

    assert germany.get_full_stability() == pytest.approx(0.43)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -7% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(-0.02)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(-0.02)
    #Political power gain of -2.8%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.028
    #57 * 0.002 = 0.114
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.114

def test_stability_increased_from_40_to_60_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 40%
    germany.add_base_stability(-0.41)

    assert germany.get_full_stability() == pytest.approx(0.40)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -10% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(-0.05)
    #Political power gain of -4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.04
    #60 * 0.002 = 0.12
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.12

    #When stability changes to 60%
    germany.add_base_stability(0.20)

    assert germany.get_full_stability() == 0.60

    #Then the bonuses should be the following
    #10% from Mefo bills and -4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.06)
    #25% * ((1+10%)*(1-4%)) = 0.264
    assert germany.get_consumer_goods() == 0.264
    #5% from limited exports and 4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.09
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.09
    #Political power gain of 2%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.02
    #40 * 0.002 = 0.086
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.08

def test_stability_decreased_from_60_to_40_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability is 60%
    germany.add_base_stability(-0.21)

    assert germany.get_full_stability() == 0.60

    #Then the bonuses should be the following
    #10% from Mefo bills and -4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.06)
    #25% * ((1+10%)*(1-4%)) = 0.264
    assert germany.get_consumer_goods() == 0.264
    #5% from limited exports and 4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.09
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.09
    #Political power gain of 2%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.02
    #40 * 0.002 = 0.086
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.08

    #When stability changes to 40%
    germany.add_base_stability(-0.20)

    assert germany.get_full_stability() == pytest.approx(0.40)

    #Then the bonuses should be the following
    #10% from Mefo bills and 0% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -10% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(-0.05)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(-0.05)
    #Political power gain of -4%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.04
    #60 * 0.002 = 0.12
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.12


def test_stability_bonuses_do_not_go_under_0_percent(germany, new_game): 
    #Given Germany

    #When stability goes under 0%
    new_modifier = modifier.Modifier("testing_modifier", 
                                     "Testing modifier", 
                                     0, 
                                     modifier_classes.Modifier_classes.BASE, 
                                     None, 
                                     {modifier_types.Modifier_types.STABILITY: -0.50}, 
                                     True)

    germany.modifiers.append(new_modifier)
    germany.add_to_full_added_bonuses(new_modifier)

    germany.add_base_stability(-0.50)

    assert germany.get_full_stability() == 0.0

    #Then the bonuses should be the same as those for 0% stability
    #10% from Mefo bills
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == 0.10
    #25% * ((1+10%)) = 0.275
    assert germany.get_consumer_goods() == 0.275
    #5% from limited exports and -50% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == -0.45
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == -0.45
    #Political power gain of -20%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.20
    #100 * 0.002 = 0.2
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.2

def test_stability_bonuses_do_not_go_over_100_percent(germany, new_game): 
    #Given Germany

    #When stability goes above 100%
    germany.add_base_stability(0.30)

    assert germany.get_full_stability() == 1.0

    #Then the bonuses should be the same as those for 100% stability
    #10% from Mefo bills and -20% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == -0.10
    #25% * ((1+10%)*(1-20%)) = 0.22
    assert germany.get_consumer_goods() == pytest.approx(0.22)
    #5% from limited exports and 20% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.25
    #Political power gain of 10%
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    #0 * 0.002 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.0

def test_war_support_modifier_at_50_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_80_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_81_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_26_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_27_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_100_percent(germany, new_game): 
    assert True == False

def test_war_support_modifier_at_0_percent(germany, new_game): 
    assert True == False

def test_war_support_increased_from_53_to_96_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_73_to_70_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_increased_from_7_to_31_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_43_to_30_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_increased_from_50_to_60_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_50_to_25_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_increased_from_40_to_60_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_decreased_from_60_to_40_changes_modifier(germany, new_game): 
    assert True == False

def test_war_support_bonuses_do_not_go_under_0_percent(germany, new_game): 
    assert True == False

def test_war_support_bonuses_do_not_go_over_100_percent(germany, new_game): 
    assert True == False


def test_stability_and_war_support_changes_at_the_same_time_changes_modifier(germany, new_game): 
    assert True == False


































def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])