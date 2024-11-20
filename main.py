class Vehicle :
    __COLOR_VARIANTS = ['black' , 'white' , 'grey' , 'brown' , 'red' , 'yellow' , 'green' , 'blue' , 'orange' ,'purple']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int (__engine_power)
        self.__color = str(__color)
    def get_model(self):
        return (f'Модель: {self.__model}')
    def get_horsepower (self):
        return (f'Мощность двигателя: {self.__engine_power}')
    def get_color (self):
        return (f'Цвет: {self.__color}')
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color (self, new_color):
        new_color=str(new_color).lower()
        if self.__COLOR_VARIANTS.count(new_color) :
            self.__color = new_color
        else: print(f'Нельзя сменить цвет на {new_color}')


    pass

class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5
    pass

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()