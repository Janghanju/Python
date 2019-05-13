class C1():
    def c1_m(self):
        print("aaa")

class C2():
    def c2_m(self):
        print("abc")

class C3(C1, C2):
    pass

c = C3()
c.c1_m()
c.c2_m()
