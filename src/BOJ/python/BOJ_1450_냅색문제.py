from itertools import combinations
# N, C = 물건의 개수, 최대 무게
N, C = map(int, input().split())
mid = N // 2
things = list(map(int, input().split()))
answer = 0
# things를 반으로 나눠서
a = things[:mid]
b = things[mid:]

sum_a = list()
sum_b = list()

for i in range(len(a) + 1):
    for subset in list(combinations(a, i)):
        sum_a.append(sum(subset))

for i in range(len(b) + 1):
    for subset in list(combinations(b, i)):
        sum_b.append(sum(subset))
    
sum_a.sort()

for item in sum_b:
    if item > C: continue

    start = 0
    end = len(sum_a) - 1

    while start <= end:
        mid = (start + end) // 2

        if sum_a[mid] + item <= C: 
            start += 1
        else:
            end = mid - 1

    answer += end + 1
    print(answer)

print(answer)