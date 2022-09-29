# 입력값 N, K
# 1. N에서 1을 빼는 연산
# 2. N을 K로 나누는 연산
## result = 두 연산을 통해 N을 1로 만드는 최소횟수

n, k = map(int, input().split())
result = 0

while True:
    if n == 1:
        break
    result = result + 1
    if n % k == 0:
        n = n / k
        continue

    n = n - 1

print(result)