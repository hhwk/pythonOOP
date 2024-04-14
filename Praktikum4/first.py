import random

class Vagon:
    NumList = ["Вагон_1", "Вагон_2", "Вагон_3", "Вагон_4", "Вагон_5", "Вагон_6", "Вагон_7", "Вагон_8", "Вагон_9", "Вагон_10", "Вагон_11", "Вагон_12", "Вагон_13", "Вагон_14"]
    MasList = ["Станки", "Автозапчасти", "Бумага", "Керамическая плитка"]

    def __init__(self, vagon_number):
        self.vagon_number = vagon_number
        self.cargo = self.assign_cargo()

    def assign_cargo(self):
        cargo_index = int(self.vagon_number.split('_')[1]) % len(self.MasList)
        return self.MasList[cargo_index]

class TarainsOfVagon:
    def __init__(self):
        self.train = [Vagon(f"Вагон_{i}") for i in range(1, 15)]

    def shuffle(self):
        random.shuffle(self.train)

    def get(self, i):
        return self.train[i].vagon_number, self.train[i].cargo

train_instance = TarainsOfVagon()
train_instance.shuffle()

while True:
    try:
        vagon_number = int(input("Введите номер вагона: "))
        if 1 <= vagon_number <= 14:
            vagon_info = train_instance.get(vagon_number - 1)
            print(f"Выбран вагон {vagon_info[0]}, груз: {vagon_info[1]}")
        else:
            print("Номер вагона должен быть от 1 до 14.")
    except ValueError:
        print("Пожалуйста, введите корректный номер вагона.")
    except IndexError:
        print("Произошла ошибка. Попробуйте еще раз.")
    else:
        choice = input("Продолжить выбор вагонов? (y/n): ")
        if choice.lower() == 'n':
            print("Выбор вагонов завершен.")
            break