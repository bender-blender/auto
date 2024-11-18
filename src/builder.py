from interface import CarBuilder
from car import Car


class Builder(CarBuilder):
    """Строитель

    Args:
        CarBuilder (_type_): _description_
    """
    def __init__(self):
        self.car = Car()
    

    def add_engine(self, engine):
        self.car.engine = engine
        return self
    
    def add_color(self, color):
        self.car.color = color
        return self
    
    def add_option(self, option):
        self.car.option = option
        return self
    
    def add_transmission(self, transmission):
        self.car.transmission = transmission
        return self
    
    def build(self):
        return self.car