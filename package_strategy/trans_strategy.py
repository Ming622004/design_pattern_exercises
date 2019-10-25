from .i_strategy import IStrategy2


class BusStrategy(IStrategy2):
    # 一段票15元
    # 十公里內一段票，超過十公里兩段票

    def calculate(self, km):
        count = 0

        if km <= 10:
            count = 1
        elif km > 10:
            count = 2

        return count * 15


class MRTStrategy (IStrategy2):
    # 小於十公里20元，超過每五公里五元

    def calculate(self, km):

        result = 0

        if km <= 0:
            return result
        elif km < 20:
            result = 20
        elif km >= 20:
            count = ((km - 20) // 5) + 1
            result = 20 + 5 * count

        return result




