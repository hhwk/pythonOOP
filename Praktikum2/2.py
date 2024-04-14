class Visogod:
    def __init__(self, year):
        self.year = year

    def is_year_leap(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

abc = Visogod(1999)

for i in range(100):
    year = 2000 + i
    print(year, abc.is_year_leap(year))