import abc


class AbstractRoad(abc.ABC):

    @abc.abstractmethod
    def run(self):
        pass


class AbatractCar(abc.ABC):

    @abc.abstractmethod
    def run(self):
        pass


class Street(AbstractRoad):

    def __init__(self, car: AbatractCar):
        self.car = car

    def run(self):
        self.car.run()
        print('在市区街道上行驶')


class SpeedWay(AbstractRoad):

    def __init__(self, car: AbatractCar):
        self.car = car

    def run(self):
        self.car.run()
        print('在高速公路上行驶')


class Car(AbatractCar):
    def run(self):
        print('小汽车在行驶')


class Bus(AbatractCar):
    def run(self):
        print('小汽车在公路上行驶')


if __name__ == '__main__':
    car1 = Car()
    car2 = Bus()

    road1 = Street(car1)
    road2 = SpeedWay(car2)

    road1.run()
    road2.run()
