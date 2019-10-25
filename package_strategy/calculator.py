from ._arithmetic import _Add, _Minus, _Multiply, _Divide


class Calculator:

    def __init__(self):
        self._now = 0

    def set_strategy(self, arith_name):
        self._strategy = self.__do_type[arith_name]

    def execute(self, num):
        self._now = self._strategy.calculate(self._now, num)
        print("now:", self._now)
        return self._now

    def reset(self):
        self._now = 0
        print("now:", self._now)

    def set(self, num):
        self._now = num
        print("now:", self._now)
    pass

    __do_type = {"+": _Add(), "-": _Minus(), "*": _Multiply(), "/": _Divide()}


