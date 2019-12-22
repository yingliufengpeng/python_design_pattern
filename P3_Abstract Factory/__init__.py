import abc
from typing import List


class AbstractFactory(abc.ABC):
    computer_name = ''

    @abc.abstractmethod
    def createCpu(self):
        pass

    @abc.abstractmethod
    def createMainBoard(self):
        pass


class AbsctractCpu(abc.ABC):
    pass


class AbstractMainBoard(abc.ABC):
    pass


class AmdCpu(AbsctractCpu):
    def __init__(self, series: str):
        self.series_name = series


class AmdMainBoard(AbstractMainBoard):
    def __init__(self, series: str):
        self.series_name = series


class AmdFactory(AbstractFactory):
    computer_name = 'Amd 4 computer'

    def createCpu(self):
        return AmdCpu('amd444')

    def createMainBoard(self):
        return AmdMainBoard('AMD-4000')


class IntelCpu(AbsctractCpu):

    def __init__(self, series: str):
        self.series_name = series


class IntelMainBoard(AbstractMainBoard):

    def __init__(self, series: str):
        self.series_name = series


class InterFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer'

    def createCpu(self):
        return IntelCpu('I7-6500')

    def createMainBoard(self):
        return IntelMainBoard('Intel-6000')


class ComputerEnginer(object):

    def makeComputer(self, factory: AbstractFactory):
        self.prepareHardWare(factory)

    def prepareHardWare(self, factory: AbstractFactory):
        self.cpu = factory.createCpu()
        self.mainboard = factory.createMainBoard()

        info = '''
------ computer {} info: 
cpu: {} 
mainboard: {}
-------- end -------
        '''.format(factory.computer_name, self.cpu.series_name,
                   self.mainboard.series_name)

        print(info)


if __name__ == '__main__':
    engineer = ComputerEnginer()

    computer_factory = InterFactory()

    engineer.makeComputer(computer_factory)

    computer_factory = AmdFactory()

    engineer.makeComputer(computer_factory)
