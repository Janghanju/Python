class C1:
    def m(self):
        return "엄마"

class C2(C1):
    def m(self):
        
        return super().m() + "자식"
        
    
o = C2()
print(o.m())

#오버라이드는 자식클래스가 부모클래스의 기능을 수정해서 사용하는 것이다
