from .i_strategy import IStrategy


class _Add(IStrategy):
    def calculate(self, a, b):
        return a + b


class _Minus(IStrategy):
    def calculate(self, a, b):
        return a - b


class _Multiply(IStrategy):
    def calculate(self, a, b):
        return a * b


class _Divide(IStrategy):
    def calculate(self, a, b):
        return a / b
