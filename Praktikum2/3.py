from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self, current_date=date.today()):
        age = current_date.year - self.date_of_birth.year - ((current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

person1 = Person("Иванов Иван Иванович", "Россия", date(1946, 8, 15))
person2 = Person("Петров Сергей Александрович", "Беларусь", date(1982, 10, 22))
person3 = Person("Федоров Андрей Алексеевич", "Китай", date(2020, 2, 1))

print("Человек 1:")
print("Имя:", person1.name)
print("Страна:", person1.country)
print("Дата рождения:", person1.date_of_birth)
print("Возраст:", person1.calculate_age())

print("Человек 2:")
print("Имя:", person2.name)
print("Страна:", person2.country)
print("Дата рождения:", person2.date_of_birth)
print("Возраст:", person2.calculate_age())

print("Человек 3:")
print("Имя:", person3.name)
print("Страна:", person3.country)
print("Дата рождения:", person3.date_of_birth)
print("Возраст:", person3.calculate_age())
