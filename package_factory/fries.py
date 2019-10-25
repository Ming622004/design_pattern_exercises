from package_factory.product import Product


class Fries(Product):

    def __init__(self, state="有鹽巴"):
        self.state = state
        pass

    def describe(self):
        print("我是%s的薯條" % self.state)
        pass
