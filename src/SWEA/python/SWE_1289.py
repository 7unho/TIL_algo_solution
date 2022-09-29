# 원재의 메모리 복구하기

t = int(input())

answers = []

for _ in range(t):
    target = list(map(int, input()))
    base = [0 for _ in range(len(target))]
    answer = 0

    for i in range(len(base)):
        if base[i] != target[i]:
            base[i:] = map(lambda x : 1 - x, base[i:])
            answer += 1
    
    answers.append(answer)
for i in range(t):
    print(f"#{i + 1} {answers[i]}")
