from abc import abstractmethod, ABCMeta


class Product(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass
