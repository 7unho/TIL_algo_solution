# 개미 전사
# 입력값 : 식량 창고의 개수 (N), 각 식량창고에 저장된 식량의 개수 (K)
# 출력값 : 식량의 최댓값

import sys
input = sys.stdin.readline

N = int(input())
K = list(map(int, input().split()))

# memoization을 위한 리스트 d
d  = [0] * 101

# 리스트 인덱스 3부터 진행하기 위해, 리스트 1, 2번값 초기화
d[1] = K[0]
d[2] = max(K[0], K[1])

# index - 1 값과 index - 2 + 현재 index 값을 비교하여
# 더 큰 값을 저장 -> 최댓값을 구하기 위해
for i in range(3, N + 1):
    d[i] = K[i - 1]

    d[i] = max(d[i - 1], d[i - 2] + d[i])

print(d[N])


# ## 교재 답안

# n = int(input())

# array = list(map(int, input().split()))

# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0], array[1])

# for i in range(2, n):
#     d[i] = max(d[i - 2], d[i - 1] + array[i])

# print(d[n - 1])
