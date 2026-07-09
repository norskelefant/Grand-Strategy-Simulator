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
        elif self.month_has_30_days() == True and self.get_day() == 30: 
            self.month += 1
            self.day = 1
        elif self.month_has_31_days() == True and self.get_day() == 31: 
            if self.get_month() != 12: 
                self.month += 1
                self.day = 1
            elif self.get_month() == 12: 
                self.year += 1
                self.month = 1
                self.day = 1
        else: 
            self.day += 1

    def next_month(self): 
        if self.month_has_31_days(): 
            for i in range(31 - self.get_day() + 1): 
                self.increment_date()
        elif self.month_has_30_days(): 
            for i in range(30 - self.get_day() + 1): 
                self.increment_date()
        elif self.month_has_28_days(): 
            for i in range(28 - self.get_day() + 1): 
                self.increment_date()

    def next_year(self): 
        days_to_go_over = 0
        #Counts only from 1 to before the current month
        for i in range(1, self.get_month()): 
            if self.month_has_31_days(i): 
                days_to_go_over += 31
            elif self.month_has_30_days(i): 
                days_to_go_over += 30
            elif self.month_has_28_days(i): 
                days_to_go_over += 28
        days_to_go_over += self.get_day()
        for i in range(365 - days_to_go_over + 1): 
            self.increment_date()

    def month_has_31_days(self, month=None): 
        if month == None: 
            month = self.get_month()

        return month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12
    
    def month_has_30_days(self, month=None): 
        if month == None: 
            month = self.get_month()

        return month == 4 or month == 6 or month == 9 or month == 11
    
    def month_has_28_days(self, month=None):
        if month == None: 
            month = self.get_month()

        return month == 2

    def get_days_remaining_in_month(self, day, month):
        if self.month_has_28_days(month) == True: 
            return 28 - day + 1
        elif self.month_has_30_days(month) == True: 
             return 30 - day + 1
        elif self.month_has_31_days(month) == True: 
             return 31 - day + 1
    
    











