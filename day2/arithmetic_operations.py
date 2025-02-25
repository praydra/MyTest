# 사칙연산 클래스 정의
class ArithmeticOperations:
    DIVISION_BY_ZERO_ERROR = "Error: Cannot divide by zero."  # 상수로 에러 메시지 정의

    @classmethod
    def calculate_add(cls, a, b):
        return a + b

    @classmethod
    def calculate_subtract(cls, a, b):
        return a - b

    @classmethod
    def calculate_multiply(cls, a, b):
        return a * b

    @classmethod
    def calculate_divide(cls, a, b):
        if b == 0:
            return cls.DIVISION_BY_ZERO_ERROR
        return a / b

    @classmethod
    def calculate_power(cls, a, b):
        return a ** b

    @classmethod
    def calculate_mod(cls, a, b):
        return a % b


# 테스트 코드
if __name__ == '__main__':
    a = 5
    b = 7
    operations = [
        ("더하기", ArithmeticOperations.calculate_add),
        ("빼기", ArithmeticOperations.calculate_subtract),
        ("곱하기", ArithmeticOperations.calculate_multiply),
        ("나누기", ArithmeticOperations.calculate_divide),
        ("제곱근", ArithmeticOperations.calculate_power),
        ("나머지", ArithmeticOperations.calculate_mod),
    ]

    for name, operation in operations:
        print(f"{name}: {a}, {b} = {operation(a, b)}")
