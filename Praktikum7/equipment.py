class Equipment:
    def __init__(self, name, make, year):
        self.name = name  # Инициализация наименования
        self.make = make  # Инициализация производителя
        self.year = year  # Инициализация года выпуска

    def action(self):
#Возвращает строку 'Не определено'
        return 'Не определено'

    def __str__(self):
#Возвращает строку с информацией об оборудовании
        return f"Наименование: {self.name}, Производитель: {self.make}, Год выпуска: {self.year}"


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)  # Вызов конструктора родительского класса
        self.series = series  # Инициализация серии

    def action(self):
        #Возвращает строку 'Печатает'
        return 'Печатает'


class Scaner(Equipment):
    def action(self):
        #Возвращает строку 'Сканирует'
        return 'Сканирует'


class Xerox(Equipment):
    def action(self):
        #Возвращает строку 'Копирует'

        return 'Копирует'


# Создание списка для хранения объектов Printer, Scaner и Xerox
sklad = [
    Printer("1234", "Принтер", "HP", 2022),
    Scaner("Сканер", "Epson", 2023),
    Xerox("Ксерокс", "Canon", 2021)
]

# Вывод содержимого списка sklad и использование метода action для каждого объекта
for item in sklad:
    print(item.action())

# Удаление всех объектов класса Printer из списка sklad
sklad = [item for item in sklad if not isinstance(item, Printer)]

# Вывод оставшегося содержимого списка sklad и использование метода action для каждого объекта
for item in sklad:
    print(item.action())
