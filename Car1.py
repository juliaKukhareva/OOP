from tracemalloc import start


class Car:
    def __init__(self, color = "blue", type = "Golf4", year = 1998,):
        self.color = color
        self.type = type
        self.year = year  
              
    
    def get_color(self):
        return f'The color of the car is - {self.color}'

    def get_type(self):
        return f'Model of the car is - {self.type}'

    def get_year (self):
        return f'Year of manufacture is - {self.year}'
    

  
MyCar = Car ()

print(f'{MyCar.get_color()}, {MyCar.get_type()}, {MyCar.get_year()}')
