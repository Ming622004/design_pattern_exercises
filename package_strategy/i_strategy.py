from abc import abstractmethod, ABCMeta


class IStrategy(metaclass=ABCMeta):

    @abstractmethod
    def calculate(self, a, b):
        pass


class IStrategy2(metaclass=ABCMeta):

    @abstractmethod
    def calculate(self):
        pass
