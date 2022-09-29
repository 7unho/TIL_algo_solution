# 홀수만 더하기

t = int(input())
answers = []

for _ in range(t):
    array = list(map(int, input().split()))

    array = list(map(lambda x : x if x % 2 != 0 else 0, array))
    answers.append(sum(array))


for i in range(t):
    print(f"#{i + 1} {answers[i]}")