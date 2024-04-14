class SeparateText:
    def __init__(self, text):
        print("Старт инициализатора в классе SeparateText.__init__()")
        self.splitword = text.split()
        print("Конец инициализатора в классе SeparateText.__init__()")

# Создаем класс CountWorld, который наследуется от SeparateText
class CountWorld(SeparateText):
    def __init__(self, text):
        print("Старт инициализатора в классе CountWorld.__init__()")
        SeparateText.__init__(self, text)
        self.word_count = len(self.splitword)
        print("Конец инициализатора в классе CountWorld.__init__()")

# Создаем класс Unique, который наследуется от SeparateText
class Unique(SeparateText):
    def __init__(self, text):
        print("Старт инициализатора в классе Unique.__init__()")
        SeparateText.__init__(self, text)
        self.unic = set(''.join(self.splitword))
        print("Конец инициализатора в классе Unique.__init__()")

# Создаем класс Describer, который наследуется от CountWorld и Unique
class Describer(CountWorld, Unique):
    def __init__(self, text):
        print("Старт инициализатора в классе Describer.__init__()")
        CountWorld.__init__(self, text)
        Unique.__init__(self, text)
        self.splitword = self.splitword
        self.unic = self.unic
        self.word_count = self.word_count
        print("Конец инициализатора в классе Describer.__init__()")

# Создаем экземпляр класса Describer и передаем ему текст для обработки
text = "Создайте экземпляр класса Describer и передайте ему текст для обработки."
describer = Describer(text)

# Выводим результаты работы класса Describer
print("Список слов:", describer.splitword)
print("Множество уникальных символов:", describer.unic)
print("Количество слов:", describer.word_count)




