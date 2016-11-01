class C1():
    def c1_m(self):
        return print("c1_m")

    def m(self):
        return print("c1_m")

class C2():
    def c2_m(self):
        return print("c2_m")
    def m(self):
        return print("c2__m")
    
class C3(C1, C2):
    def m(self):
        print("C3__m")
    pass

c = C3()
c.c1_m()
c.c2_m()
c.m()
print(c3.__mro__)
