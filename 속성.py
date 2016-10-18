"""
Ruby
c1.value => 불가능 => 가능하게
문구로 외부 변경가능해짐
""attr_reader : value"" 읽기
""attr_writer : value"" 쓰기
""attr_accessor : value" 모두 가능

Python
c1.value => 가능 => 불가능하게
"""
class C(object):
    def __init__(self, v):
        self.__value = v
        #self."__"value = v
        #이렇게 하면 읽기쓰기 금지
    def show(self):
        print(self.__value)

c1 = C(10)
#print(c1.__value)

c1.show()
