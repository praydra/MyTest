# 사칙연산 함수 정의

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


# 테스트 코드
if __name__ == '__main__':
    a = 5
    b = 7

    print(f"더하기: {a} + {b} = {add(a, b)}")
    print(f"빼기: {a} - {b} = {subtract(a, b)}")
    print(f"곱하기: {a} * {b} = {multiply(a, b)}")
    print(f"나누기: {a} / {b} = {divide(a, b)}")