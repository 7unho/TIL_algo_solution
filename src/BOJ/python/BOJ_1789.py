# 수들의 합
## 서로 다른 N개의 자연수들의 합이 S
## 입력값 : S, 출력값 : N의 최댓값

s = int(input())
i = 1
sum = 0
while True:
    sum += i
    if sum > s:
        i -= 1
        break
    i += 1

print(i)