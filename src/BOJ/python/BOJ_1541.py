import sys
input = sys.stdin.readline

array = input().strip().split('-')
answer = 0
for item in array[0].split('+'):
    answer += int(item)

for i in range(1, len(array)):
    array[i] = [int(i) for i in array[i].split('+')]
    answer -= sum(array[i])

print(answer)
