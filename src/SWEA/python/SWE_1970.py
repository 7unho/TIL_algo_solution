# 쉬운 거스름돈
## 그리디
## 입력값 : N원, 출력값 : 50000, 10000, 5000, 1000, 500, 100, 50, 10원의 최소 개수

for tc in range(1, int(input()) + 1):
    n = int(input())
    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answers = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(coins)):
        answers[i] += n // coins[i]
        n %= coins[i]

    print(f"#{tc}")
    for answer in answers:
        print(f"{answer}", end=' ')