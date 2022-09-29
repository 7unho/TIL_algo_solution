# 1978. 소수 찾기
import math


a, b, c, d = map(int, input().split())

result = [a, b, c, d]

for i in range(4):
    if result[i] <= 1:
        result[i] = 0
    else:
        for j in range(2, int(math.sqrt(result[i])) + 1):
            if result[i] % j == 0:
                result[i] = 0
                break

result = list(map(lambda a : a if a == 0 else 1, result))
print(sum(result))