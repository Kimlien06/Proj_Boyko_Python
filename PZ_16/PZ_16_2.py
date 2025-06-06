# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.

class Avto:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year

    def information(self):
        return f'Марка: {self.marka}, Модель: {self.model}, Год выпуска: {self.year}'


class Gruzovik(Avto):
    def __init__(self, marka, model, year, gruz):
        super().__init__(marka, model, year)
        self.gruz = gruz

    def information(self):
        return super().information() + f' Грузоподёмность: {self.gruz} т'


class Car(Avto):
    def __init__(self, marka, model, year, count_pass):
        super().__init__(marka, model, year)
        self.count_pass = count_pass

    def information(self):
        return super().information() + f' Кол-во пассажиров: {self.count_pass}'


gruzovik = Gruzovik("Volvo", "FH16", 2022, 20)
car = Car("Toyota", "Camry", 2023, 5)

print("Грузовик:", gruzovik.information())
print("Легковой автомобиль:", car.information())
