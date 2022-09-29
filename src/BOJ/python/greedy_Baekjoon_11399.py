# 백준 알고리즘 11399_greedy 알고리즘
## 인원 ( N ), 각각의 실행 시간 ( time_list ), 총 실행 시간의 최소값 ( result )

import sys

input_N = int(sys.stdin.readline())
time_list = []
result = 0
userList = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]

for i in range(input_N) :
    time_list.append(sorted(userList)[i])
    result += sum(time_list)
print(result)
