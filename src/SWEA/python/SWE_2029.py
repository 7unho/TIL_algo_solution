# 몫과 나머지 출력

t = int(input())
answers = []

for _ in range(t):
    a, b = map(int, input().split())
    answers.append([a // b, a % b])

for i in range(t):
    print(f"#{i + 1} {answers[i][0]} {answers[i][1]}")