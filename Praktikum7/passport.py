class Passport:
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport):
        self.first_name = first_name  # Инициализация имени
        self.last_name = last_name  # Инициализация фамилии
        self.country = country  # Инициализация страны
        self.date_of_birth = date_of_birth  # Инициализация даты рождения
        self.numb_of_passport = numb_of_passport  # Инициализация номера паспорта

    def PrintInfo(self):
        print("Информация о паспорте:")
        print("Имя:", self.first_name, self.last_name)
        print("Страна:", self.country)
        print("Дата рождения:", self.date_of_birth)
        print("Номер паспорта:", self.numb_of_passport)


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport, visa):
        super().__init__(first_name, last_name, country, date_of_birth,
                         numb_of_passport)  # Вызов конструктора родительского класса
        self.visa = visa  # Инициализация визы

    def PrintInfo(self):
        super().PrintInfo()  # Вызов метода родительского класса для вывода информации о паспорте
        print("Виза:", self.visa)


# Создание списка для хранения объектов Passport и ForeignPassport
PassportList = [
    Passport("John", "Doe", "USA", "01/01/1990", "123456"),
    ForeignPassport("Jane", "Smith", "Canada", "02/02/1985", "654321", "Tourist"),
    Passport("Alice", "Johnson", "UK", "03/03/1988", "987654"),
    ForeignPassport("Bob", "Brown", "Australia", "04/04/1980", "456789", "Work")
]

# Перебор элементов списка PassportList и вызов метода PrintInfo для каждого объекта
for passport in PassportList:
    passport.PrintInfo()
