import sys
input = sys.stdin.readline

N, C = map(int, input().split())
array = [int(input()) for _ in range(N)]
array.sort()

# 인접 노드의 거리 범위 [ start: 최솟값, end: 최댓값 ]
start = 1
end = max(array) - min(array)


while start <= end:
    mid = (start + end) // 2
    
    # 처음노드
    current = array[0]
    count = 1

    for i in range(1, N):

        #현재 노드와 인접한 노드의 거리가 평균값 이상이라면
        ## 공유기 설치해주고, current이동
        if array[i] - current >= mid:
            count += 1
            current = array[i]

    # 공유기 설치 대수가 C이상이라면
    ## 목표보다 많이 설치되었다 -> 거리를 넓힌다 (우측 범위로 탐색)
    if count >= C:
        start = mid + 1
        result = mid
    ## 목표보다 적게 설치되었다 -> 거리를 좁힌다 (좌측 범위로 탐색)
    else:
        end = mid - 1

print(result)