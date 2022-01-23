from abc import ABCMeta,abstractmethod

class PizzaFactory(metaclass=ABCMeta): # 抽象工厂
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNoVegPizza(self):
        pass

class IndianPizzaFactory(PizzaFactory): #具体工厂
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNoVegPizza(self):
        return ChickenPizza()

class USAPizzaFactory(PizzaFactory): #具体工厂
    def createVegPizza(self):
        return MexicanVegPizza()
    def createNoVegPizza(self):
        return HamPizza()

class VegPizza(metaclass=ABCMeta): #抽象产品
    @abstractmethod
    def prepare(self,VegPizza):
        pass

class NoVegPizza(metaclass=ABCMeta): #抽象产品
    @abstractmethod
    def serve(self,VegPizza):
        pass


class DeluxVeggiePizza(VegPizza): # 具体产品
    def prepare(self):
        print('prepare ',type(self).__name__)


class ChickenPizza(NoVegPizza): # 具体产品
    def serve(self,VegPizza):
        print(type(self).__name__, 'is served with Chicken on ',type(VegPizza).__name__)

class MexicanVegPizza(VegPizza): # 具体产品
    def prepare(self):
        print('prepare ',type(self).__name__)


class HamPizza(NoVegPizza): # 具体产品
    def serve(self,VegPizza):
        print(type(self).__name__, 'is served with Chicken on ',type(VegPizza).__name__)

class PizzaStore: #客户端
    def __init__(self):
        pass
    def makePizzas(self):
        for factory in [IndianPizzaFactory(),USAPizzaFactory()]:
            self.factory=factory
            self.NoVegPizza=self.factory.createNoVegPizza()
            self.VegPizza=self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NoVegPizza.serve(self.VegPizza)

if __name__ == '__main__':
    pizza=PizzaStore()
    pizza.makePizzas()