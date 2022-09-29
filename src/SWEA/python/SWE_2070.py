# 큰 놈, 작은 놈, 같은 놈
t = int(input())

answers = []

for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        answer = '>'
    else:
        answer = '=' if a == b else '<'
    answers.append(answer)

for i in range(t):
    print(f"#{i + 1} {answers[i]}")