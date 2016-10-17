class AAA:
    def __init__(self, a):
        self.value = a
    def show(self):
        print(self.value)
        
a1 = AAA(10)
print(a1.value)
a1.value = 20
print(a1.value)
a1.show()
