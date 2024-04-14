class Sedan:
    def __init__(self):
        self._doors = 4
        self._engine_type = "petrol"

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        self._doors = value

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value):
        self._engine_type = value

    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Accelerating")

class SUV:
    def __init__(self):
        self._doors = 4
        self._engine_type = "diesel"
        self._cargo_space = "large"

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        self._doors = value

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value):
        self._engine_type = value

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Accelerating")

    def brake(self):
        print("Braking")

class Hatchback:
    def __init__(self):
        self._doors = 5
        self._engine_type = "electric"
        self._cargo_space = "small"
        self._transmission = "automatic"

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        self._doors = value

    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, value):
        self._engine_type = value

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, value):
        self._transmission = value

    def start_transmission(self):
        print("Transmission started")

class Car(Sedan, SUV, Hatchback):
    def __init__(self):
        super().__init__()
        self._cargo_space = None
        self._transmission = None

    @property
    def cargo_space(self):
        return self._cargo_space

    @cargo_space.setter
    def cargo_space(self, value):
        self._cargo_space = value

    @property
    def transmission(self):
        return self._transmission

    @transmission.setter
    def transmission(self, value):
        self._transmission = value

    def drive(self):
        self.start_engine()
        self.start_transmission()
        self.accelerate()
        self.brake()

if __name__ == "__main__":
    car = Car()
    print("Car Type: Sedan")
    print("Number of doors:", car.doors)
    print("Engine type:", car.engine_type)
    print("Cargo space:", car.cargo_space)
    print("")

    print("Car Type: SUV")
    car.engine_type = "diesel"  # Changing engine type for SUV
    print("Number of doors:", car.doors)
    print("Engine type:", car.engine_type)
    print("Cargo space:", car.cargo_space)
    print("")

    print("Car Type: Hatchback")
    car.engine_type = "electric"  # Changing engine type for Hatchback
    car.cargo_space = "medium"  # Adding cargo space attribute
    car.transmission = "manual"  # Adding transmission attribute
    print("Number of doors:", car.doors)
    print("Engine type:", car.engine_type)
    print("Cargo space:", car.cargo_space)
    print("Transmission type:", car.transmission)
    print("")

    print("Driving the car:")
    car.drive()
