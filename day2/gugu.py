# 구구단 출력
for i in range(1, 10):  # 1단부터 9단까지
    print(f"{i}단:")
    for j in range(1, 10):  # 각 단의 1부터 9까지 곱셈
        print(f"{i} x {j} = {i * j}")
    print()  # 각 단 사이의 빈 줄 추가