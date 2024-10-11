class Calculator:
    calculation_type = "Arithmetic Operations"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return cls(a*b)

    @staticmethod
    def add(a,b):
        return a + b