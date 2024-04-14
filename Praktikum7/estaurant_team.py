class Employee:
    def __init__(self, name, salary):
        self.name = name  # Имя сотрудника
        self.salary = salary  # Зарплата сотрудника

    def giveRaise(self, percent):
        """
        Увеличивает зарплату на заданный процент
        """
        self.salary *= (1 + percent / 100)

    def work(self):
        """
        Выводит сообщение о том, что сотрудник работает
        """
        print(f"{self.name} работает.")

    def __repr__(self):
        """
        Возвращает строку с информацией о сотруднике
        """
        return f"{self.__class__.__name__}(Name: {self.name}, Salary: {self.salary})"


class Chef(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)  # Вызов конструктора родительского класса

    def work(self):
        """
        Выводит сообщение о том, что повар готовит еду
        """
        print(f"{self.name} готовит еду.")


class Server(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)  # Вызов конструктора родительского класса

    def work(self):
        """
        Выводит сообщение о том, что официант обслуживает клиентов
        """
        print(f"{self.name} обслуживает клиентов.")


class PizzaRobot(Chef):
    def __init__(self, name, salary):
        super().__init__(name, salary)  # Вызов конструктора родительского класса

    def work(self):
        """
        Выводит сообщение о том, что робот готовит пиццу
        """
        print(f"{self.name} готовит пиццу.")


# Создание объекта bob класса PizzaRobot
bob = PizzaRobot("Bob", 1000)

# Вызов методов work и giveRaise для объекта bob
bob.work()
bob.giveRaise(10)

# Создание объектов для каждого класса и вызов их методов work
employee1 = Employee("Alice", 800)
chef1 = Chef("John", 1200)
server1 = Server("Emily", 900)
robot1 = PizzaRobot("Robbie", 1500)

employee1.work()
chef1.work()
server1.work()
robot1.work()
