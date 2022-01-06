'''
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
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

a = FourCal()
a.setdata(4, 2) #a객체에 first가 생성되면서 4가 저장됨, second가 생성되면서 2가 저장
b = FourCal()
b.setdata(3, 5) #b는 다른 값을 가지게 됨

print(a.add())

'''
class FourCal:
    def __init__(self, first, second): #생성자
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second
    lastname = "Rhee" #클래스 변수
'''
a = FourCal(4, 2)
b = FourCal(3, 8)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
'''

class MoreFourCal(FourCal): #클래스 상속
    def pow(self):
        return self.first ** self.second
'''
a = MoreFourCal(4, 2)
print(a.add())
'''

class SafeFourCal(FourCal):
    def div(self): #Method Overriding
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())
