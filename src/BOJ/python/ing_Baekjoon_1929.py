# 에라토스테네스의 체를 이용한 소수구하기
import math

m, n = map(int, input().split())
result = [int(i) for i in range(m, n+1)]
i = 2
flag = True
prime_list = []


# for i in range(2, int(math.sqrt(n)) + 1):
#     result = list(map(lambda a : 0 if a % i == 0 else a, result))

# print(result)