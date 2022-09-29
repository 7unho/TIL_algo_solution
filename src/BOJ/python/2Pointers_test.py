# 특정한 합을 가지는 부분 연속 수열 찾기
## 입력값 : 길이가 N인 리스트, 출력값 : M의 합을 갖는 부분 수열
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list = list(map(int, input().split()))

answer = 0
interval_sum = 0
end = 0

for start in range(N):

    # 부분 수열의 합이 M보다 작거나, end가 N을 넘지 않을 때,
    # interval_sum에 end좌표의 데이터를 누산하고
    # end를 1 이동시켜준다.
    while interval_sum < M and end < N:
        interval_sum += list[end]
        end += 1
    
    # 부분 수열의 합이 M과 같다면 answer + 1
    if interval_sum == M:
        answer +=1
    
    # 모든 연산이 끝나면, interval_sum이 M보다 크거나 같다면
    ## start를 이동해야 하므로 interval_sum에서 start좌표의 
    interval_sum -= list[start]

print(answer)