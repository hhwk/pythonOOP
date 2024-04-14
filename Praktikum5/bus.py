class Bus:
    def __init__(self, speed, distance):
        self.__speed = speed
        self.__distance = distance
        self.__max_speed = 120
        self.__passengers = []
        self.__capacity = 75
        self.__empty_seats = None
        self.__seats_occupied = None
        self.__fuel_tank = 100
        self.__toplivo = None
        self.__kartet_tank = 6
        self.__maslo = None
        self.__luggage_spaces = 150
        self.__luggage = None

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def capacity(self):
        return self.__capacity

    @property
    def fuel_tank(self):
        return self.__fuel_tank

    @property
    def kartet_tank(self):
        return self.__kartet_tank

    @property
    def luggage_spaces(self):
        return self.__luggage_spaces

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.__max_speed:
            raise ValueError("Скорость не может быть больше максимальной")
        self.__speed = value

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        if len(value) > self.__capacity:
            raise ValueError("Количество пассажиров не может превышать вместимость")
        self.__passengers = value

    @property
    def empty_seats(self):
        return self.__empty_seats

    @empty_seats.setter
    def empty_seats(self, value):
        if value > self.__capacity:
            raise ValueError("Количество свободных мест не может превышать вместимость")
        self.__empty_seats = value

    @property
    def seats_occupied(self):
        return self.__seats_occupied

    @seats_occupied.setter
    def seats_occupied(self, value):
        if value > self.__capacity:
            raise ValueError("Количество занятых мест не может превышать вместимость")
        self.__seats_occupied = value

    @property
    def toplivo(self):
        return self.__toplivo

    @toplivo.setter
    def toplivo(self, value):
        self.__toplivo = value

    @property
    def maslo(self):
        return self.__maslo

    @maslo.setter
    def maslo(self, value):
        self.__maslo = value

    @property
    def luggage(self):
        return self.__luggage

    @luggage.setter
    def luggage(self, value):
        if value > self.__luggage_spaces:
            raise ValueError("Объем багажа не может превышать количество багажных мест")
        self.__luggage = value

    def __str__(self):
        return f"Скорость: {self.__speed}\nРасстояние: {self.__distance}\nМаксимальная скорость: {self.__max_speed}\nПассажиры: {self.__passengers}\nВместимость: {self.__capacity}\nПустые места:"
