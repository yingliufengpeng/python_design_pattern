'''
    简单的工厂模式
'''

import abc


class Shape(abc.ABC):

    @abc.abstractmethod
    def draw(self):
        pass


class Triangle(Shape):

    def draw(self):
        print('画三角形')


class Square(Shape):

    def draw(self):
        print('画正方形')


class Circle(Shape):

    def draw(self):
        print('画圆')


types = ('Triangle', 'Square', 'Circle')

class ShapeFactory(object):

    def create(self, shape: str):

        if shape in types:

            return globals()[shape]()

        else:
            return None


factory = ShapeFactory()

t = factory.create("Circle")

t.draw()
