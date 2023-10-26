import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(input().rstrip())
    sys.exit(0)

words = [input().rstrip() for _ in range(n)]
answer = ''

for i in range(len(words[0])):
    for j in range(1, n):
        word = words[0][i]
        if words[j - 1][i] != words[j][i]:
            word = '?'
            break

    answer += word


print(answer)