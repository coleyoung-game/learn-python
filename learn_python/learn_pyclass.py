class FourCal:
    # 생성자(constructor)
    # self는 객체 변수(instance variable) -> 값 변경 불가
    # 객체의 고유한 속성을 관리하는데 많이 사용 됨
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
       self.first = first
       self.second = second
    # 클래스내 메서드 구현시 매개변수에 객체 변수를 반드시 추가해야 한다.
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
