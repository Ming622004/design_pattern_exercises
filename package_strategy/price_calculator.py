from .trans_strategy import BusStrategy, MRTStrategy


class PriceCalculator:

    def __init__(self):
        # 預設坐公車
        self._strategy = BusStrategy()
        pass

    def calculate(self, km, strategy_in=None):
        if not strategy_in:
            strategy_in = self._strategy
        self._strategy = strategy_in
        self.__pay = self._strategy.calculate(km)
        print("pay:", self.__pay)
        return self.__pay

    def set_strategy(self, strategy):
        self._strategy = strategy

