# 수 묶기
## 두 수씩 묶고, 묶은 수는 곱하여 누산

import sys
input = sys.stdin.readline

n = int(input())

answer = 0
numbers = [[],[]]

for _ in range(n):
    number = int(input())
    if number >= 1:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

numbers[0].sort(reverse=True)
numbers[1].sort()


for i in range(2):
    while True:
        if not numbers[i]:
            break

        if len(numbers[i]) >= 2:
            answer += numbers[i][0] * numbers[i][1] if numbers[i][0] != 1 and numbers[i][1] != 1 else numbers[i][0] + numbers[i][1]
            numbers[i].remove(numbers[i][1])
            numbers[i].remove(numbers[i][0])
            continue

        answer += numbers[i][0]
        numbers[i].remove(numbers[i][0])

print(answer)