import abc
from typing import List


class Store(abc.ABC):

    @abc.abstractmethod
    def add(self, store: 'Store'):
        pass

    @abc.abstractmethod
    def remove(self, store: 'Store'):
        pass

    @abc.abstractmethod
    def pay_by_card(self):
        pass

class BranStore(Store):

    def __init__(self, name):
        self.name = name
        self.my_store_list: List[Store] = []

    def add(self, store: 'Store'):
        self.my_store_list.append(store)

    def remove(self, store: 'Store'):
        self.my_store_list.remove(store)

    def pay_by_card(self):
        print('店面  {}  积分已累加进该会员卡'.format(self.name))
        for s in self.my_store_list:
            s.pay_by_card()


class JoinStore(Store):

    def __init__(self, name):
        self.name = name

    def add(self, store: 'Store'):
        print('无添加自子店的权限')

    def remove(self, store: 'Store'):
        print('无删除子店的权限')

    def pay_by_card(self):
        print('店面  {}  积分已累加进该会员卡'.format(self.name))


if __name__ == '__main__':

    store = BranStore('朝阳总店')
    branch = BranStore('海滨分店')

    join_branch = JoinStore('昌平加盟1店')
    join_branch2 = JoinStore('昌平加盟2店')

    branch.add(join_branch)
    branch.add(join_branch2)

    store.add(branch)

    store.pay_by_card()

