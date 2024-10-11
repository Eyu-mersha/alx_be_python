class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def multiply(cls, a, b):
        return cls(a*b)

    @staticmethod
    def add(a,b):
        return a + b