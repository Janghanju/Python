class AA:
    count = 0
    def __init__(self):
        AA.count = AA.count + 1
    @classmethod
    def getCount(cls):
        return AA.count

i1 = AA()
i2 = AA()
i3 = AA()
i4 = AA()
print(AA.getCount())
