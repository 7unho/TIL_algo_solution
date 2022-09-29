# 1이 될 때 까지
## N이 1이 될 때 까지
## 1. N에서 1을 뺴거나, 2. N을 K로 나누는 연산
## 연산의 최소 횟수 구하기

import sys

n, k = map(int, sys.stdin.readline().split())
result = 0
# for i in range(n):
#     if n == 1 :
#         break
#
#     if n % k == 0 :
#         n = int(n / k)
#     else :
#         n -=1
#
#     result += 1
#
# print(result)

while True:

    #N이 K로 나눠지는 가장 가까운 수 : target을 구함
    target = (n // k) * k

    #result = N - targer -> 연산횟수
    result += ( n - target )
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += ( n - 1 )
print(result)