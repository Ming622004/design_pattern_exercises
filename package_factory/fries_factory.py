from .factory import Factory
from .fries import Fries


class FriesFactory(Factory):

    def __init__(self):
        pass

    def get_product(self, *state):
        # print(type(state))
        return Fries(*state)
        pass

