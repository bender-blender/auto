from abc import ABC, abstractmethod


class CarBuilder(ABC):
    """Создатель машины

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def add_engine(self, engine):
        """Добавить двигатель
        """
        raise NotImplementedError()

    @abstractmethod
    def add_transmission(self, transmission):
        """Добавить трансмиссию
        """
        raise NotImplementedError()

    @abstractmethod
    def add_color(self, color):
        """Добавить цвет
        """
        raise NotImplementedError()

    @abstractmethod
    def add_option(self, option):
        """Добавить опции
        """
        raise NotImplementedError()
