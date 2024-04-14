#1
class WinDoor:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#2
class Room:
    def __init__(self, width, length, height, wallpaper_roll_width, wallpaper_roll_height):
        self.width = width
        self.length = length
        self.height = height
        self.wallpaper_roll_width = wallpaper_roll_width
        self.wallpaper_roll_height = wallpaper_roll_height
        self.windows_doors = []

    def add_window(self, width, height):
        window = WinDoor(width, height)
        self.windows_doors.append(window)

    def add_door(self, width, height):
        door = WinDoor(width, height)
        self.windows_doors.append(door)

    def calculate_wallpaper_area(self):
        room_area = 2 * (self.width + self.length) * self.height
        doors_windows_area = sum([(wd.width * wd.height) for wd in self.windows_doors])
        return room_area - doors_windows_area

    def calculate_wallpaper_rolls(self):
        wallpaper_area = self.calculate_wallpaper_area()
        return wallpaper_area / (self.wallpaper_roll_width * self.wallpaper_roll_height)

#3
room1 = Room(5, 7, 3, 0.5, 10)
room1.add_window(1, 1)
room1.add_door(3, 7)

room2 = Room(4, 6, 2.5, 0.7, 15)
room2.add_window(1.5, 1.5)

room3 = Room(6, 8, 3, 0.6, 12)
room3.add_door(2, 6)
room3.add_window(2, 2)

#4
width = float(input("Введите ширину комнаты: "))
length = float(input("Введите длину комнаты: "))
height = float(input("Введите высоту комнаты: "))
wallpaper_roll_width = float(input("Введите ширину рулона обоев: "))
wallpaper_roll_height = float(input("Введите высоту рулона обоев: "))

#5
user_room = Room(width, length, height, wallpaper_roll_width, wallpaper_roll_height)
user_room.add_window(1, 1)
user_room.add_door(2, 5)

wallpaper_area = user_room.calculate_wallpaper_area()
wallpaper_rolls = user_room.calculate_wallpaper_rolls()

print(f"Площадь под оклейку: {wallpaper_area} кв.м")
print(f"Количество необходимых рулонов обоев: {wallpaper_rolls}")
