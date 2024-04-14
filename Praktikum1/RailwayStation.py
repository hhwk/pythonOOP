class RailwayStation:
    def __init__(self):
        self.way = []
        self.trains = []
        self.workers = []

    def add_way(self, way):
        self.way.append(way)

    def add_train(self, train):
        self.trains.append(train)

    def add_worker(self, worker):
        self.workers.append(worker)

    def print_way(self):
        for path in self.way:
            print(path.number)

    def print_trains(self):
        for train in self.trains:
            print(train)

    def print_workers(self):
        for worker in self.workers:
            print(worker)

    def remove_way(self, way):
        self.way.remove(way)

    def remove_train(self, train):
        self.trains.remove(train)

    def remove_worker(self, worker):
        self.workers.remove(worker)