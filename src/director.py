from builder import Builder
from car import Car


class Director:
    """Директор
    """
    def __init__(self):
        self.builder = Builder()
        self.car = Car()

    def add_car(self, engine, color, transmission, option):
        self.builder.add_engine(engine)
        self.builder.add_color(color)
        self.builder.add_transmission(transmission)
        self.builder.add_option(option)
        return self.builder.build()
