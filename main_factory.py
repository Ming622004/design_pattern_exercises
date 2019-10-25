# https://ithelp.ithome.com.tw/articles/10202075
"""
先做兩個抽象類別Factory跟Product
做一個想生產的產品類別(繼承Product)
做一個製造這個產品的工廠類別(繼承Factory)
"""

from package_factory import FriesFactory


def main():
    factory1 = FriesFactory()
    product1 = factory1.get_product()
    product1.describe()
    product2 = factory1.get_product("無鹽")
    product2.describe()
    pass


if __name__ == '__main__':
    main()
    pass
