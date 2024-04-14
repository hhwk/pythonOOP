class Vagon:
    def __init__(self, number,cargo):
        self.number = number
        self.cargo = cargo
        self.train_numbers = []

    def add_train_number(self, train_number):
        self.train_numbers.append(train_number)

    def remove_train_number(self, train_number):
        self.train_numbers.remove(train_number)

    def get_train_numbers(self):
        return self.train_numbers

#vagon1=Vagon(12,'Уголь')
