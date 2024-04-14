class Vehicle:
    def __init__(self):
        print("Initializing Vehicle")

class Sedan(Vehicle):
    def __init__(self):
        super().__init__()
        print("Initializing Sedan")
        self._doors = 4

    @property
    def doors(self):
        return self._doors

class SUV(Vehicle):
    def __init__(self):
        super().__init__()
        print("Initializing SUV")
        self._doors = 5

    @property
    def doors(self):
        return self._doors

class Hatchback(Sedan, SUV):
    def __init__(self):
        super().__init__()
        print("Initializing Hatchback")
        self._engine_type = "electric"

    @property
    def engine_type(self):
        return self._engine_type

class Car(Hatchback):
    def __init__(self):
        super().__init__()
        print("Initializing Car")

    def drive(self):
        print("Driving the car")

if __name__ == "__main__":
    car = Car()
    print("Car Type: Sedan")
    print("Number of doors:", car.doors)
    print("")

    print("Car Type: SUV")
    suv_car = SUV()
    print("Number of doors:", suv_car.doors)
    print("")

    print("Car Type: Hatchback")
    print("Engine type:", car.engine_type)
    print("")

    print("Driving the car:")
    car.drive()
