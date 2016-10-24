class AA:
    @staticmethod #규칙
    def sm():
        print("Startic method")

    @classmethod  #규칙
    def cm(cls):
        print("Class method")

    def instance_method(self):
        print("Instance method")

i = AA()
AA.sm()
AA.cm()
i.instance_method()
