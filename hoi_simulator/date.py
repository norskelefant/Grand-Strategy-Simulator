class Date: 
    def __init__(self, day, month, year): 
        self.day = day
        self.month = month
        self.year = year

    def get_day(self): 
        return self.day
        
    def get_month(self): 
        return self.month
        
    def get_year(self): 
        return self.year
        
    def increment_date(self): 
        if self.month_has_28_days() == True and self.get_day() == 28: 
            self.month += 1
            self.day = 1
        if self.month_has_30_days() == True and self.get_day() == 30: 
            self.month += 1
            self.day = 1
        if self.month_has_31_days() == True and self.get_day() == 31: 
            if self.get_month() != 12: 
                self.month += 1
                self.day = 1
            elif self.get_month() == 12: 
                self.year += 1
                self.month = 1
                self.day = 1
        else: 
            self.day += 1

    def month_has_31_days(self): 
        return self.get_month() == 1 or self.get_month() == 3 or self.get_month() == 5 or self.get_month() == 7 or self.get_month() == 8 or self.get_month() == 10 or self.get_month() == 12
    
    def month_has_30_days(self): 
        return self.get_month() == 4 or self.get_month() == 6 or self.get_month() == 9 or self.get_month() == 11
    
    def month_has_28_days(self): 
        return self.get_month() == 2
    
    











