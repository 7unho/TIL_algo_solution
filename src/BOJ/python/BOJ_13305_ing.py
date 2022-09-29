# 주유소
import sys
input = sys.stdin.readline

n = int(input())

dist_list = list(map(int, input().split()))
city_list = list(map(int, input().split()))

answer = dist_list[0] * city_list[0]

for i in range(1, (n - 1)):
    answer += dist_list[i] * min(city_list[:(i + 1)])

print(answer)
