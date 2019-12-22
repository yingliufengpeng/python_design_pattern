import abc


class PersonBuilder(abc.ABC):

    @abc.abstractmethod
    def buildHead(self):
        pass

    @abc.abstractmethod
    def buildBody(self):
        pass

    @abc.abstractmethod
    def buildArm(self):
        pass

    @abc.abstractmethod
    def buildLeg(self):
        pass


class PersonDirector(abc.ABC):

    def __init__(self, pb: PersonBuilder):
        self.pb = pb

    def createPreson(self):
        self.pb.buildHead()
        self.pb.buildBody()
        self.pb.buildArm()
        self.pb.buildLeg()


class PersonFatBuiler(PersonBuilder):

    def buildHead(self):
        print('构建胖子的头')

    def buildBody(self):
        print('构建胖子的身体')

    def buildArm(self):
        print('构建胖子的胳膊')

    def buildLeg(self):
        print('构建胖子的大腿')


class PersonThinBuilder(PersonBuilder):

    def buildHead(self):
        print('构建瘦子的头')

    def buildBody(self):
        print('构建瘦子的身体')

    def buildArm(self):
        print('构建瘦子的胳膊')

    def buildLeg(self):
        print('构建瘦子的大腿')


def clientUI():
    pb = PersonFatBuiler()
    pd = PersonDirector(pb)
    pd.createPreson()
    print('-' * 20)
    pb2 = PersonThinBuilder()
    pd2 = PersonDirector(pb2)
    pd2.createPreson()


if __name__ == '__main__':
    clientUI()
