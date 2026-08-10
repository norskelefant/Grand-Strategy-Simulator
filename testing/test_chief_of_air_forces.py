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

def test_albert_kesselring(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Albert Kesselring is hired
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Albert_kesselring")

    assert germany.get_political_power() == 0

    #Then Albert Kesselring has the following bonuses
    albert_kesselring = germany.find_modifier_by_id("Albert_kesselring")

    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Albert Kesselring is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_albert_kesselring_without_fulfilling_political_power_cost(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Albert Kesselring is hired without enough political power
    germany.add_political_power(0)

    germany.hire_chief_of_air_force("Albert_kesselring")

    assert germany.get_political_power() == 0

    #Then Albert Kesselring has the following bonuses
    albert_kesselring = germany.find_modifier_by_id("Albert_kesselring")

    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Albert Kesselring is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_hermann_göring_while_fulfilling_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Hermann Göring is hired when Germany is fascist
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Hermann_goring")

    assert germany.get_political_power() == 0

    #Then Hermann Göring has the following bonuses
    hermann_goring = germany.find_modifier_by_id("Hermann_goring")

    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

    #and Germany has the following bonuses because Hermann Göring is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

def test_hermann_göring_while_fulfilling_having_reinstated_nazi_leadership(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Hermann Göring is hired when Germany has reinstated nazi leadership
    germany.activate_event("Reinstated_nazi_leadership")
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Hermann_goring")

    assert germany.get_political_power() == 0

    #Then Hermann Göring has the following bonuses
    hermann_goring = germany.find_modifier_by_id("Hermann_goring")

    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

    #and Germany has the following bonuses because Hermann Göring is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

def test_hermann_göring_without_fulfilling_being_fascist_or_having_reinstated_nazi_leadership(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Hermann Göring is hired when Germany has not reinstated nazi leadership and is not fascist
    germany.change_ideology(ideologies.Ideologies.COMMUNIST)
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Hermann_goring")

    assert germany.get_political_power() == 100

    #Then Hermann Göring has the following bonuses
    hermann_goring = germany.find_modifier_by_id("Hermann_goring")

    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

    #but Germany has the following bonuses because Hermann Göring is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_ritter_von_greim(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BAD_WEATHER_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Ritter von Greim is hired when Germany has completed focus Expanding the luftwaffe
    germany.complete_focus("Expanding_the_luftwaffe")
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Ritter_von_greim")

    assert germany.get_political_power() == 0

    #Then Ritter von Greim has the following bonuses
    ritter_von_greim = germany.find_modifier_by_id("Ritter_von_greim")

    assert ritter_von_greim.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert ritter_von_greim.get_modifier_bonuses()[modifier_types.Modifier_types.BAD_WEATHER_PENALTY] == -0.20
    assert ritter_von_greim.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #and Germany has the following bonuses because Ritter von Greim is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BAD_WEATHER_PENALTY] == -0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

def test_ritter_von_greim_without_fulfilling_having_completed_focus_expanding_the_luftwaffe(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BAD_WEATHER_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Ritter von Greim is hired when Germany has not completed focus Expanding the luftwaffe
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Ritter_von_greim")

    assert germany.get_political_power() == 100

    #Then Ritter von Greim has the following bonuses
    ritter_von_greim = germany.find_modifier_by_id("Ritter_von_greim")

    assert ritter_von_greim.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert ritter_von_greim.get_modifier_bonuses()[modifier_types.Modifier_types.BAD_WEATHER_PENALTY] == -0.20
    assert ritter_von_greim.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20

    #but Germany has the following bonuses because Ritter von Greim is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.BAD_WEATHER_PENALTY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0

def test_helmuth_wilberg(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Helmuth Wilberg is hired when Germany is not fascist and has completed focus Reorganize the luftwaffe
    germany.change_ideology(ideologies.Ideologies.DEMOCRATIC)
    germany.complete_focus("Reorganize_the_luftwaffe")
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Helmuth_wilberg")

    assert germany.get_political_power() == 0

    #Then Helmuth Wilberg has the following bonuses
    helmuth_wilberg = germany.find_modifier_by_id("Helmuth_wilberg")

    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.40
    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.15
    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 30

    #and Germany has the following bonuses because Helmuth Wilberg is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.40
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.15
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 30

def test_helmuth_wilberg_without_fulfilling_not_being_fascist(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Helmuth Wilberg is hired when Germany is fascist and has completed focus Reorganize the luftwaffe
    germany.complete_focus("Reorganize_the_luftwaffe")
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Helmuth_wilberg")

    assert germany.get_political_power() == 100

    #Then Helmuth Wilberg has the following bonuses
    helmuth_wilberg = germany.find_modifier_by_id("Helmuth_wilberg")

    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.40
    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.15
    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 30

    #but Germany has the following bonuses because Helmuth Wilberg is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_helmuth_wilberg_without_fulfilling_having_completed_focus_reorganize_the_luftwaffe(germany, new_game):
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When Helmuth Wilberg is hired when Germany is not fascist and has not completed focus Reorganize the luftwaffe
    germany.change_ideology(ideologies.Ideologies.NON_ALIGNED)
    germany.add_political_power(100)

    germany.hire_chief_of_air_force("Helmuth_wilberg")

    assert germany.get_political_power() == 100

    #Then Helmuth Wilberg has the following bonuses
    helmuth_wilberg = germany.find_modifier_by_id("Helmuth_wilberg")

    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.40
    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.15
    assert helmuth_wilberg.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 30

    #but Germany has the following bonuses because Helmuth Wilberg is not hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

def test_cannot_have_more_than_one_chief_of_air_force(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0

    germany.add_political_power(200)

    germany.hire_chief_of_air_force("Albert_kesselring")
   
    assert germany.get_political_power() == 100
   
    #Then Albert Kesselring has the following bonuses
    albert_kesselring = germany.find_modifier_by_id("Albert_kesselring")
   
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
   
    #and Germany has the following bonuses because Albert Kesselring is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0

    #Then hiring another chief of air force
    germany.hire_chief_of_air_force("Hermann_goring")

    assert germany.get_political_power() == 0

    #Then Hermann göring has the following bonuses
    hermann_goring = germany.find_modifier_by_id("Hermann_goring")

    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

    #and Germany has the following bonuses because Hermann Göring is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0

    #and the length of chiefs of air force hired is only 1
    chief_of_air_force_list = [germany.get_chief_of_air_force()]
    assert len(chief_of_air_force_list) == 1

def test_swapping_chief_of_air_force(germany, new_game): 
    #Given a normal Germany game
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0

    germany.add_political_power(200)

    germany.hire_chief_of_air_force("Albert_kesselring")
   
    assert germany.get_political_power() == 100
   
    #Then Albert Kesselring has the following bonuses
    albert_kesselring = germany.find_modifier_by_id("Albert_kesselring")
   
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert albert_kesselring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
   
    #and Germany has the following bonuses because Albert Kesselring is hired
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.30
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == 0.0
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.0

    #Then hiring another chief of air force
    germany.hire_chief_of_air_force("Hermann_goring")

    assert germany.get_political_power() == 0

    #Then Hermann göring has the following bonuses
    hermann_goring = germany.find_modifier_by_id("Hermann_goring")

    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert hermann_goring.get_modifier_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10

    #and Germany has the following bonuses because Abert kesselring is replaced with Hermann Göring
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.20
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.TACTICAL_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.STRATEGIC_BOMBER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.FIGHTER_PRODUCTION_COST] == -0.025
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_SUPERIORITY] == 0.05
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 10
    assert germany.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0

def test_another_country_cannot_hire_german_chief_of_air_force(germany, new_game): 
    #Given a testing country that is not Germany
    testing_country = create_custom_country(new_game)

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0

    #When testing country hires Albert Kesselring
    testing_country.add_political_power(100)

    testing_country.hire_chief_of_navy("Albert_kesselring")

    #Then Albert Kesselring should not be hired
    assert testing_country.get_political_power() == 100

    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.DAILY_AIR_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.AIR_EXPERIENCE_GAIN] == 0.0
    assert testing_country.get_full_added_bonuses()[modifier_types.Modifier_types.MAX_COMMAND_POWER_INCREASE] == 0.0




















def created_advanced_germany(): 
    return setup_countries.create_advanced_germany()

def create_game(germany): 
    return game.Game(date.Date(1, 1, 1936), [germany])

def create_custom_country(game): 
    return custom_country.create_custom_country(game)
