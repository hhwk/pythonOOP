class DataBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __str__(self):
        return f"Подключение к БД: пользователь={self.user}, пароль={self.psw}, порт={self.port}"

    def connect(self):
        print(f"Подключение к БД: пользователь={self.user}, пароль={self.psw}, порт={self.port}")

    def __del__(self):
        print("Закрытие подключения к БД")

    def get_data(self):
        pass

    def set_data(self):
        pass

db1 = DataBase("root", "1234", 80)
db1.connect()
print(db1)

db2 = DataBase("пользователь", "пароль", 8080)
db2.connect()
print(db2)

del db1
