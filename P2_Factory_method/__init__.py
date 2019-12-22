import abc


class AbstractSchool(abc.ABC):
    name = ''
    addr = ''
    principal = ''

    @abc.abstractmethod
    def enroll(self, name, course):
        pass

    @abc.abstractmethod
    def info(self):
        pass


class AbstractCourse(abc.ABC):

    def __init__(self, name, time_range, study_type, fee):
        self.name = name
        self.time_range = time_range
        self.study_type = study_type
        self.fee = fee

    @abc.abstractmethod
    def enroll_test(self):
        print('课程{}测试中'.format(self.name))

    @abc.abstractmethod
    def print_course_outline(self):
        pass


class LinuxOPSCourse(AbstractCourse):

    def print_course_outline(self):
        outline = '''
            Linux 基础
            Linux 基本服务使用
            Linux 高级服务篇
            Linux Shell编程
        '''

        print(outline)

    def enroll_test(self):
        print('不需要进行测试!!!')


class PythonCourse(AbstractCourse):

    def print_course_outline(self):
        outline = '''
            Python 基础
            Python 基本服务使用
            Python 高级服务篇
            Python 网络编程
        '''

        print(outline)

    def enroll_test(self):
        print('---Python入学测试---')
        print('---500道题答对了---')
        print('---通过了---')


class BJSchol(AbstractSchool):

    name = "老男孩北京校区"

    def create_course(self, course_type: str):
        pass

    def enroll(self, name, course: AbstractCourse):
        print('开始为新学员{}进行办学手续'.format(name))
        print('帮学员{}注册课程{}'.format(name, course))
        course.enroll_test()

    def info(self):
        print('-----{}-----'.format(self.name))


class SHSchol(AbstractSchool):
    name = "老男孩上海校区"

    def create_course(self, course_type: str):
        pass

    def enroll(self, name, course: AbstractCourse):
        print('开始为新学员{}进行办学手续'.format(name))
        print('帮学员{}注册课程{}'.format(name, course))
        course.enroll_test()

    def info(self):
        print('-----{}-----'.format(self.name))


bg = BJSchol()

sh = SHSchol()

