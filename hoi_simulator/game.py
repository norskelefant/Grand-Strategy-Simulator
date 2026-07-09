class Game: 
    def __init__(self, date, countries): 
        self.date = date
        self.countries = countries

    #Goes through all countries, since that will be needed later when there are more countries
    def pass_day(self): 
        self.get_date().increment_date()
        for country in self.countries: 
            for construction_line in country.get_construction().get_construction_line_list(): 
                construction_line.day_has_passed(country.get_ic())

    def pass_month(self): 
        amount_of_days_remaining_in_month = self.get_date().get_days_remaining_in_month(self.get_date().get_month(), self.get_date().get_month())
        for country in self.countries: 
            for construction_line in country.get_construction().get_construction_line_list(): 
                construction_line.pass_to_next_month(country.get_ic(), amount_of_days_remaining_in_month)
        self.get_date().next_month()

    def get_date(self): 
        return self.date



