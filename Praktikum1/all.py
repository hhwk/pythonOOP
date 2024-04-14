from train import Train
from RailwayStation import RailwayStation
from Vagon import Vagon
from Way import Way
from Worker import Worker

# Создание объектов классов
way1 = Way(1)
way2 = Way(2)

train1 = Train()
train2 = Train()

vagon1 = Vagon(1)
vagon2 = Vagon(2)

worker1 = Worker(1, "Радиостанция 1", "Иванов Иван Иванович", "Диспетчер")
worker2 = Worker(2, "Радиостанция 2", "Петров Петр Петрович", "Осмотрщик")

station = RailwayStation()

# Добавление вагонов на пути
way1.add_vagon(vagon1)
way2.add_vagon(vagon2)

# Прицепление вагонов к поезду
train1.attach_vagon(vagon1)
train2.attach_vagon(vagon2)

# Добавление номера поезда к вагону
vagon1.add_train_number(1)
vagon2.add_train_number(2)

# Добавление осматриваемых поездов работником
worker1.add_inspected_train(train1)
worker2.add_inspected_train(train2)

# Добавление путей, поездов и работников на станцию
station.add_way(way1)
station.add_way(way2)
station.add_train(train1)
station.add_train(train2)
station.add_worker(worker1)
station.add_worker(worker2)

# Вывод путей, поездов и работников на станции
station.print_way()
station.print_trains()
station.print_workers()

# Удаление пути, поезда и работника
station.remove_way(way1)
station.remove_train(train1)
station.remove_worker(worker1)
