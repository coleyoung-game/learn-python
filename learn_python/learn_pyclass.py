class FourCal:
    # ������(constructor)
    # self�� ��ü ����(instance variable) -> �� ���� �Ұ�
    # ��ü�� ������ �Ӽ��� �����ϴµ� ���� ��� ��
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
       self.first = first
       self.second = second
    # Ŭ������ �޼��� ������ �Ű������� ��ü ������ �ݵ�� �߰��ؾ� �Ѵ�.
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def dosomething(ss):
        print('do something')

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second

a = FourCal(4, 2)
a.setdata(4, 2)
a.add()
print(a)

b = MoreFourCal(4, 2)
result = b.div()
print(result)

b.dosomething()
