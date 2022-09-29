# 평균값 구하기

t = int(input())

answers = []

for _ in range(t):
    array = list(map(int, input().split()))
    answers.append(round(sum(array) / 10))

for i in range(t):
    print(f"#{i + 1} {answers[i]}")