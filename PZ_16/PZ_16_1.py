# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.

class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self, step=1):
        self.value += step

    def decrement(self, step=1):
        self.value -= step

    def get_value(self):
        return self.value

    def reset(self, new_value=0):
        self.value = new_value


counter = Counter()
print('Изначальное значение:', counter.get_value())
counter.increment()
print('После инкремента:', counter.get_value())
counter.increment(5)
print('После инкремента на 5:', counter.get_value())
counter.decrement()
print('После деинкремента:', counter.get_value())
counter.reset()
print('После сброса', counter.get_value())
