def has_required_war_support(self, war_support, country): 
    return country.get_full_war_support() > war_support

def has_required_ideology(self, ideologies, country): 
    for ideology in ideologies: 
        if country.get_ideology() == ideology: 
            return True

