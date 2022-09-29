import sys
input = sys.stdin.readline

def dfs(numbers, target, index, total):
    global answer
    print(index, len(numbers))
    if index == len(numbers):
        if target == total:
            answer += 1
            return
    dfs(numbers, target, index + 1, total + numbers[index])
    dfs(numbers, target, index + 1, total - numbers[index])


answer = 0

numbers = list(map(int, input().split()))
target = int(input())

dfs(numbers, target, 0, 0)

print(answer)