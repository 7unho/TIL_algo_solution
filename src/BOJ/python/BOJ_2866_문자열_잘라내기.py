# 입력값 : R * C 의 배열
# 출력값 : 지울 수 있는 최대 행의 개수 ( 행을 지워도 열 문자열의 중복이 없다면 행을 지운다 )

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

start = 0
end = R - 1
answer = 0

while start <= end:
    mid = (start + end) // 2

    # 중복 문자열 확인용 변수
    isExist = set()
    
    for j in range(C):
        temp = ""

        # mid ~ 문자열의 끝까지 반복
        for i in range(mid, R):
            temp += graph[i][j]
        isExist.add(temp)

    # isExist의 길이가 C보다 작다면,
    # 중복된 문자열이 존재했다는 뜻이므로 mid를 위쪽으로 옮겨준다.
    if len(isExist) < C:
        end = mid - 1

    # isExist의 길이가 C와 같다면,
    # 중복된 문자열이 없었다는 뜻이므로, 가장 최적된 값을 찾기 위해
    # mid를 아래쪽으로 옮겨주고 해당 값을 기록해줍니다
    else :
        start = mid + 1
        answer = mid

    
print(answer)
