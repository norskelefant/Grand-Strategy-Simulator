from hoi_simulator import country, state, setup_countries, construction, construction_types, construction_line, date, game, modifier, modifier_classes, modifier_types, economy_laws, ideologies




























def create_custom_country(): 

    custom_state = state.State("Custom_state", 50, 15, 15, 10, 3, True, None)

    custom_country = country.Country(name="Custom_country", 
                       states={"Custom_state": custom_state},
                       tiles=None, 
                       resources=None, 
                       free_civs=15, 
                       civs_used_on_consumer_goods=0, 
                       free_mils=15, 
                       free_dockyards=10, 
                       construction=construction.Construction(), 
                       base_ic=4, 
                       base_stability=0.7, 
                       stability_modifier=None,
                       economy_law=modifier.Modifier("Partial_mobilization", "Partial Mobilization", 0, modifier_classes.Modifier_classes.ECONOMY_LAW, None, {modifier_types.Modifier_types.CONSUMER_GOODS_FACTOR: 0.25, modifier_types.Modifier_types.MIL_CONSTRUCTION_SPEED: 0.10}, True), 
                       base_war_support=0.3, 
                       war_support_modifier=None,
                       political_power=0, 
                       population=0, 
                       fuel=0, 
                       command_power=0, 
                       convoys=0, 
                       army_exp=0, 
                       navy_exp=0, 
                       air_exp=0, 
                       ideology=ideologies.Ideologies.FASCIST, 
                       democratic_support=35, 
                       non_aligned_support=15, 
                       communist_support=10, 
                       fascist_support=40, 
                       at_war=False, 
                       countries_at_war_with=[], 
                       research_slots=4, 
                       has_researched=[], 
                       can_research=[],
                       trade_law=None, 
                       conscription_law=None, 
                       advisors=[], 
                       possible_advisors={},
                       industrial_concern=None, 
                       possible_industrial_concerns={},
                       theorist=None, 
                       possible_theorists={},
                       chief_of_army=None, 
                       possible_chiefs_of_army={},
                       chief_of_navy=None, 
                       possible_chiefs_of_navy={},
                       chief_of_air_force=None, 
                       possible_chiefs_of_air_force={},
                       high_commanders=[], 
                       possible_high_commanders={},
                       leader=None, 
                       possible_leaders={},
                       focus_tree=[], 
                       focuses_done=[], 
                       focuses_that_can_be_done=[], 
                       national_spirits=[], 
                       modifiers=[], 
                        possible_events={}, 
                       events_gotten=[], 
                       intelligence_agency=None,
                       full_added_bonuses={})
    
    custom_country.states["Custom_state"].set_country(custom_country)

    return custom_country