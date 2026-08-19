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

def test_stability_modifier_at_start(germany, new_game): 
    #Given default Germany

    #When stability is the default of 81%
    assert germany.get_full_stability() == pytest.approx(0.81)

    #Then the bonuses should be the following
    #10% from Mefo bills and -12.4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(-0.024)
    #25% * ((1+10%)*(1-12.4%)) = 0.2409
    assert germany.get_consumer_goods() == pytest.approx(0.2409)
    #5% from limited exports and 12.4% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.174
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.174
    #Political power gain of 6.2%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.162
    #19 * 0.002 = 0.038
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.038

def test_war_support_modifier_at_start(germany, new_game): 
    #Given Germany

    #When war support is the default of 35%
    assert germany.get_full_war_support() == 0.35

    #Then the bonuses should be the following
    #-0.01 * 15 = -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.15
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 15 = -0.285
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.285
    #-0.006 * 15 = -0.09
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.09

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
    #No extra political power gain except for 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.10


def test_stability_modifier_at_70_percent(germany, new_game): 
    #Given Germany

    #When stability is 70%
    germany.add_base_stability(-0.11)

    assert germany.get_full_stability() == 0.70

    #Then the bonuses should be the following
    #10% from Mefo bills and -8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.02)
    #25% * ((1+10%)*(1-8%)) = 0.253
    assert germany.get_consumer_goods() == pytest.approx(0.253)
    #5% from limited exports and 8% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == 0.13
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == 0.13
    #Political power gain of 4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.14
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
    #Political power gain of 4.2%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.142)
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
    #Political power gain of -12%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(-0.02)
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
    #Political power gain of -11.6%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.016
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
    #Political power gain of 10%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.20
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
    #Political power gain of -20%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.10
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
    #Political power gain of 2%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.12)
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
    #Political power gain of 4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.14
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
    #Political power gain of 6.8%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.168
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
    #Political power gain of 2.4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.124
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
    #Political power gain of -16%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.06
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
    #Political power gain of -11.2%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(-0.012)
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
    #Political power gain of -0.4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.096
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
    #Political power gain of -4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.06)
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
    #Political power gain of 0%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
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
    #Political power gain of 1.4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.114
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
    #Political power gain of 0%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.10
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
    #Political power gain of -2.8%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.072)
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
    #Political power gain of -4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.06)
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
    #Political power gain of 2%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.12)
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
    #Political power gain of 2%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.12)
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
    #Political power gain of -4%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == pytest.approx(0.06)
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
    #Political power gain of -20%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == -0.10
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
    #Political power gain of 10%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.20
    #0 * 0.002 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.0

def test_war_support_modifier_at_50_percent(germany, new_game): 
    #Given Germany

    #When war support is 50%
    germany.add_base_war_support(0.15)

    assert germany.get_full_war_support() == pytest.approx(0.50)

    #Then the bonuses should be the following
    #0.0060 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.0
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #0.01 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.0
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

def test_war_support_modifier_at_80_percent(germany, new_game): 
    #Given Germany

    #When war support is 80%
    germany.add_base_war_support(0.45)

    assert germany.get_full_war_support() == 0.80

    #Then the bonuses should be the following
    #0.0060 * 30 = 0.18
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.18
    #0.0020 * 30 = 0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.06
    #0.01 * 30 = 0.3
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.3
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

def test_war_support_modifier_at_81_percent(germany, new_game): 
    #Given Germany

    #When war support is 81%
    germany.add_base_war_support(0.46)

    assert germany.get_full_war_support() == 0.81

    #Then the bonuses should be the following
    #0.0060 * 31 = 0.186
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.186
    #0.0020 * 31 = 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.062
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.062
    #0.01 * 31 = 0.31
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.31
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

def test_war_support_modifier_at_26_percent(germany, new_game): 
    #Given Germany

    #When war support is 26%
    germany.add_base_war_support(-0.09)

    assert germany.get_full_war_support() == 0.26

    #Then the bonuses should be the following
    #-0.01 * 24 = -0.24
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.24
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0
    #-0.019 * 24 = -0.456
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == pytest.approx(-0.456)
    #-0.006 * 24 = -0.144
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == pytest.approx(-0.144)

def test_war_support_modifier_at_27_percent(germany, new_game): 
    #Given Germany

    #When war support is 27%
    germany.add_base_war_support(-0.08)

    assert germany.get_full_war_support() == pytest.approx(0.27)

    #Then the bonuses should be the following
    #-0.01 * 23 = -0.23
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.23
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0
    #-0.019 * 23 = -0.437
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.437
    #-0.006 * 23 = -0.138
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == pytest.approx(-0.138)

def test_war_support_modifier_at_100_percent(germany, new_game): 
    #Given Germany

    #When war support is 100%
    germany.add_base_war_support(0.65)

    assert germany.get_full_war_support() == 1.0

    #Then the bonuses should be the following
    #0.0060 * 50 = 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.30
    #0.0020 * 50 = 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.10
    #0.01 * 50 = 0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.50
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

def test_war_support_modifier_at_0_percent(germany, new_game): 
    #Given Germany

    #When war support is 0%

    new_modifier = modifier.Modifier("testing_modifier", 
                                     "Testing modifier", 
                                     0, 
                                     modifier_classes.Modifier_classes.BASE, 
                                     None, 
                                     {modifier_types.Modifier_types.WAR_SUPPORT: -0.05}, 
                                     True)

    germany.modifiers.append(new_modifier)
    germany.add_to_full_added_bonuses(new_modifier)

    germany.add_base_war_support(-0.30)

    assert germany.get_full_war_support() == 0.0

    #Then the bonuses should be the following
    #-0.01 * 50 = -0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.50
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0
    #-0.019 * 50 = -0.95
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.95
    #-0.006 * 50 = -0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.30

def test_war_support_increased_from_53_to_96_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 53%
    germany.add_base_war_support(0.18)

    assert germany.get_full_war_support() == 0.53

    #Then the bonuses should be the following
    #0.0060 * 3 = 0.018
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == pytest.approx(0.018)
    #0.0020 * 3 = 0.006
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.006
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.006
    #0.01 * 3 = 0.03
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.03
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

    #When war support increases to 96%
    germany.add_base_war_support(0.43)

    assert germany.get_full_war_support() == 0.96

    #Then the bonuses should be the following
    #0.0060 * 46 = 0.276
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.276
    #0.0020 * 46 = 0.092
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.092
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.092
    #0.01 * 46 = 0.46
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.46
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

def test_war_support_decreased_from_73_to_70_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 73%
    germany.add_base_war_support(0.38)

    assert germany.get_full_war_support() == 0.73

    #Then the bonuses should be the following
    #0.0060 * 23 = 0.138
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.138
    #0.0020 * 23 = 0.046
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.046
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.046
    #0.01 * 23 = 0.23
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.23
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

    #When war support decreases to 70%
    germany.add_base_war_support(-0.03)

    assert germany.get_full_war_support() == 0.70

    #Then the bonuses should be the following
    #0.0060 * 20 = 0.12
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.12
    #0.0020 * 20 = 0.04
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.04
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.04
    #0.01 * 20 = 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.20
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

def test_war_support_increased_from_7_to_31_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 7%
    germany.add_base_war_support(-0.28)

    assert germany.get_full_war_support() == pytest.approx(0.07)

    #Then the bonuses should be the following
    #-0.01 * 43 = -0.43
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.43
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 43 = -0.817
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.817
    #-0.006 * 43 = -0.258
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.258

    #When war support increases to 31%
    germany.add_base_war_support(0.24)

    assert germany.get_full_war_support() == pytest.approx(0.31)

    #Then the bonuses should be the following
    #-0.01 * 19 = -0.19
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.19
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 19 = -0.361
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.361
    #-0.006 * 19 = -0.114
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.114

def test_war_support_decreased_from_43_to_30_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 43%
    germany.add_base_war_support(0.08)

    assert germany.get_full_war_support() == 0.43

    #Then the bonuses should be the following
    #-0.01 * 7 = -0.07
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.07
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 7 = -0.133
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.133
    #-0.006 * 7 = -0.042
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.042

    #When war support decreases to 30%
    germany.add_base_war_support(-0.13)

    assert germany.get_full_war_support() == 0.30

    #Then the bonuses should be the following
    #-0.01 * 20 = -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.20
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 20 = -0.38
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.38
    #-0.006 * 20 = -0.12
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.12

def test_war_support_increased_from_50_to_60_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 50%
    germany.add_base_war_support(0.15)

    assert germany.get_full_war_support() == pytest.approx(0.50)

    #Then the bonuses should be the following
    #0.0060 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.0
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #0.01 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.0
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

    #When war support increases to 60%
    germany.add_base_war_support(0.10)

    assert germany.get_full_war_support() == 0.60

    #Then the bonuses should be the following
    #0.0060 * 10 = 0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.06
    #0.0020 * 10 = 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.02
    #0.01 * 10 = 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.10
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

def test_war_support_decreased_from_50_to_25_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 50%
    germany.add_base_war_support(0.15)

    assert germany.get_full_war_support() == pytest.approx(0.50)

    #Then the bonuses should be the following
    #0.0060 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.0
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #0.01 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.0
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0

    #When war support decreases to 25%
    germany.add_base_war_support(-0.25)

    assert germany.get_full_war_support() == pytest.approx(0.25)

    #Then the bonuses should be the following
    #-0.01 * 25 = -0.25
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.25
    #0.0020 * 0 = 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 25 = -0.475
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.475
    #-0.006 * 25 = -0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.15

def test_war_support_increased_from_40_to_60_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 40%
    germany.add_base_war_support(0.05)

    assert germany.get_full_war_support() == pytest.approx(0.40)

    #Then the bonuses should be the following
    #-0.01 * 10 = -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.10
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 10 = -0.19
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.19
    #-0.006 * 10 = -0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.06

    #When war support increases to 60%
    germany.add_base_war_support(0.20)

    assert germany.get_full_war_support() == pytest.approx(0.60)

    #Then the bonuses should be the following
    #0.0060 * 10 = 0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.06
    #0.0020 * 10 = 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.02
    #0.01 * 10 = 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.10
    #-0.006 * 0 = -0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0

def test_war_support_decreased_from_60_to_40_changes_modifier(germany, new_game): 
    #Given Germany

    #When war support is 60%
    germany.add_base_war_support(0.25)

    assert germany.get_full_war_support() == pytest.approx(0.60)

    #Then the bonuses should be the following
    #0.0060 * 10 = 0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.06
    #0.0020 * 10 = 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.02
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.02
    #0.01 * 10 = 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.10
    #-0.006 * 0 = -0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0

    #When war support decreases to 40%
    germany.add_base_war_support(-0.20)

    assert germany.get_full_war_support() == 0.40

    #Then the bonuses should be the following
    #-0.01 * 10 = -0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.10
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 10 = -0.19
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.19
    #-0.006 * 10 = -0.06
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.06

def test_war_support_bonuses_do_not_go_under_0_percent(germany, new_game): 
    #Given Germany

    #When war support goes below 0%

    new_modifier = modifier.Modifier("testing_modifier", 
                                     "Testing modifier", 
                                     0, 
                                     modifier_classes.Modifier_classes.BASE, 
                                     None, 
                                     {modifier_types.Modifier_types.WAR_SUPPORT: -0.20}, 
                                     True)

    germany.modifiers.append(new_modifier)
    germany.add_to_full_added_bonuses(new_modifier)

    germany.add_base_war_support(-0.50)

    assert germany.get_full_war_support() == 0.0

    #Then the bonuses should be the same as at 0%
    #-0.01 * 50 = -0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.50
    #0.0020 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0
    #-0.019 * 50 = -0.95
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.95
    #-0.006 * 50 = -0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.30

def test_war_support_bonuses_do_not_go_over_100_percent(germany, new_game):     
    #Given Germany

    #When war support is over 100%
    germany.add_base_war_support(0.80)

    assert germany.get_full_war_support() == 1.0

    #Then the bonuses should be the same as if war support is at 100%
    #0.0060 * 50 = 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == 0.30
    #0.0020 * 50 = 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.10
    #0.01 * 50 = 0.50
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == 0.50
    #-0.006 * 0 = 0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == 0.0


def test_stability_and_war_support_changes_at_the_same_time_changes_modifier(germany, new_game): 
    #Given Germany

    #When stability changes to 65% and war support changes to 20%
    germany.add_base_stability(-0.16)
    germany.add_base_war_support(-0.15)

    assert germany.get_full_stability() == pytest.approx(0.65)
    assert germany.get_full_war_support() == 0.20

    #Then the bonuses should be the following
    #10% from Mefo bills and -6% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR] == pytest.approx(0.04)
    #25% * ((1+10%)*(1-6%)) = 0.2585
    assert germany.get_consumer_goods() == 0.2585
    #5% from limited exports and 6% from stability
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FACTORY_OUTPUT] == pytest.approx(0.11)
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DOCKYARD_OUTPUT] == pytest.approx(0.11)
    #Political power gain of 3%, 10% from leader
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.POLITICAL_POWER_GAIN] == 0.13
    #35 * 0.002 = 0.07
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.RESISTANCE_TARGET_IN_OCCUPIED_TERRITORIES] == 0.07

    #-0.01 * 30 = -0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MOBILIZATION_SPEED] == -0.30
    #0.0020 * 0 = 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_ATTACK_ON_CORE_TERRITORY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DIVISION_DEFENSE_ON_CORE_TERRITORY] == 0.0
    #-0.019 * 30 = -0.57
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_COMMAND_POWER_GAIN_MULTIPLIER] == -0.57
    #-0.006 * 30 = -0.18
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.SURRENDER_LIMIT] == -0.18





































def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])