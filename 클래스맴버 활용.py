class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):#int는 정수
            self.v1 = v1
        if isinstance(v2, int):#int는 정수
            self.v2 = v2

    def add(self):#더하기
        result = self.v1 + self.v2
        Cal._history.append("add : %d + %d = %d" %(self.v1, self.v2, result))
        return result
    
    def subtract(self):#빼기
        return self.v1 - self.v2

    def setV1(self, v):#V1 지정
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1#V1 출력

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

class CalMultiply(Cal):
    def multiply(self):
        return self.v1 * self.v2#곱하기

class CalDivide(CalMultiply):
    def divide(self):
        return self.v1 / self.v2#나누기

c1 = CalMultiply(10, 10)
print(c1, c1.add())
print(c1, c1.multiply())

c2 = CalDivide(20, 10)
print(c2, c2.divide())
print(c2, c2.add())
print(c2, c2.multiply())

Cal.history()
