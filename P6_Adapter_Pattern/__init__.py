import abc


class Player(abc.ABC):
    # name = ''

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def defense(self):
        pass


class ForwardPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print('前锋{}进攻'.format(self.name))

    def defense(self):
        print('前锋{}防守'.format(self.name))


class CenterPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print('中锋{}进攻'.format(self.name))

    def defense(self):
        print('中锋{}防守'.format(self.name))


class BackPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print('后卫{}进攻'.format(self.name))

    def defense(self):
        print('后卫{}防守'.format(self.name))

class ForeignCenter(abc.ABC):

    def __init__(self, name):
        self.name = name

    def foreignattack(self):
        print('外国中锋{}进攻'.format(self.name))

    def foreigndefense(self):
        print('外国中锋{}防守'.format(self.name))

class AdapterPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.foreigin = ForeignCenter(name)

    def attack(self):
        self.foreigin.foreignattack()

    def defense(self):
        self.foreigin.foreigndefense()


def clientUI():

    b = ForwardPlayer('巴蒂尔')

    m = BackPlayer('姚明')

    ym = AdapterPlayer('麦克格雷迪')

    b.attack()
    m.defense()
    ym.attack()

if __name__ == '__main__':
    clientUI()