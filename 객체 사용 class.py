class Cal(object):
                #첫번째 매소드가 제1 인스턴스 지정
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
        
    def add(self):
        return self.a1 + self.a2

    def subtract(self):
        return self.a1 - self.a2

#위의 클래스 사용 코드 시작
c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30, 20)
print(c2.add())
print(c2.subtract())
#종료
