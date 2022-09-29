import sys
input = sys.stdin.readline

target, base = map(int, input().strip().split())
answer = 1

while True:
    if base <= target:
        break
    if base % 10 == 1:
        base = base // 10
    elif base % 2 == 0:
        base //= 2
    else:
        break
    answer += 1

print(answer if base == target else '-1')
