# https://ithelp.ithome.com.tw/articles/10202506
"""
第二個例子
做一個IStrategy2, 裡面有calculate方法
建立兩種類別繼承做一個IStrategy2, 分別為BusStrategy, MusStrategy
建立一個主要呼叫的類別PriceCalculator
這個例子中, 可以set strategy, 以及輸入km計算price
也可以同時輸入km以及strategy
strategy輸入的方式為直接將一實例輸入
"""

from package_strategy import PriceCalculator, BusStrategy, MRTStrategy


def main():
    c = PriceCalculator()
    # 公車 30公里跟 10公里
    print("=== default test ===")
    c.calculate(30)
    c.calculate(10)

    # 設定成MRT 30公里跟10公里
    print()
    print("=== MRT test ===")
    c.set_strategy(MRTStrategy())
    c.calculate(30)
    c.calculate(10)

    print()
    print("=== strategy input test ===")
    # # MRT15公里 公車15公里
    c.calculate(15, MRTStrategy())
    c.calculate(15, BusStrategy())
    pass


if __name__ == '__main__':
    main()


