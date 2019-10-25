from abc import abstractmethod, ABCMeta


class Factory(metaclass=ABCMeta):

    @abstractmethod
    def get_product(self):
        pass
