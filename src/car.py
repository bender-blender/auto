class Car:
    """Машина
    """
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.color = None
        self.option = None

    def __str__(self):
        return f"Двигатель:{self.engine}\nТрансмиссия:{self.transmission}\nЦвет:{self.color}\nОпции:{self.option}"