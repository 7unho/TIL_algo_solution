# 자성체
from collections import deque

answers = []
for _ in range(10):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for i in range(n):
        stack = deque()
        for j in range(n):
            if graph[j][i] == 1:
                stack.append(1)
            elif graph[j][i] == 2 and len(stack) >= 1:
                temp = stack.pop()
                if temp == 1:
                    answer += 1
                stack.append(temp)
                stack.append(2)
    
    answers.append(answer)

for i in range(10):
    print(f"#{i + 1} {answers[i]}")



