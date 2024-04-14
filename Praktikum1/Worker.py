class Worker:
    def __init__(self, id, radio, name, position):
        self.id = id
        self.radio = radio
        self.inspected_trains = []
        self.name = name
        self.position = position

    def add_inspected_train(self, train):
        self.inspected_trains.append(train)

    def get_inspected_trains(self):
        return self.inspected_trains

    def set_radio(self,radio):
        self.radio=radio

worker1=Worker()
worker1.set_radio('Радиостанция_1')
worker2=Worker()
worker2.set_radio('Радиостанция_1')

worker1.print_radio()
worker2.print_radio()