# https://ithelp.ithome.com.tw/articles/10202506
"""
第一個例子
做一個簡單的計算機，這邊稍微改了一些東西，像是執行的時候預設前面的數字為now
先做一個抽象類別IStrategy (python好像沒interface?)
製作四則運算的類別(繼承IStrategy)
做一個計算機類別Calculator，可set(n)、reset()、設定運算符號，輸入值
設定運算符號時，因沒有java的Enum，這邊用dict取代
另外就不設定"="按鍵了
"""

from package_strategy import Calculator


def main():
    c = Calculator()
    c.set(5)

    print("=== try: +5 ===")
    c.set_strategy("+")
    c.execute(5)

    print("=== try: -6 ===")
    c.set_strategy("-")
    c.execute(6)

    print("=== try: *6 ===")
    c.set_strategy("*")
    c.execute(6)

    print("=== try: /2 ===")
    c.set_strategy("/")
    c.execute(2)

    print("=== try: reset ===")
    c.reset()
    pass


if __name__ == '__main__':
    main()


