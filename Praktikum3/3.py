class Vagon:
    numbers = {}

    def __new__(cls, name, number):
        if not name.startswith("vagon_"):
            raise ValueError("Имя должно начинаться с 'vagon_'")
        number = name.replace("vagon_", "")
        instance = super().__new__(cls)
        cls.numbers[number] = instance
        return instance

    def __init__(self, name, number):
        pass

v1 = Vagon("vagon_1", 1)