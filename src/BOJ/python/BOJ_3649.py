# 로봇 프로젝트
## 입력값 : X (구멍의 너비 -> 센티미터), N (조각의 수), 레고조각 ( 나노미터 )
## 출력값 : 각 테케마다 구멍을 완벽하게 막을 수 있는 두 조각이 없다면 danger, 막을 수 있다면 yes val1, val2 출력

import sys
input = sys.stdin.readline

# 예외처리 // 입력은 여러 개의 테스트 케이스로 이루어져 있다.
while True:
    try:
        X = int(input()) * 10_000_000
        N = int(input())
        array = [int(input()) for _ in range(N)]
        array.sort()

        start = 0
        end = N - 1

        answer = False

        while True:
            
            # start가 end와 교차되지 않게
            if start >= end:
                break

            current = array[start] + array[end]

            # 현재 두 조각의 합이 X와 같다면 정답 출력
            if X == current:
                answer = f"yes {array[start]} {array[end]}"
                break

            # X 보다 작다면 start 증가
            if X > current:
                start += 1
                continue
            
            # X 보다 크다면 end 감소
            if X < current:
                end -= 1
                continue

        print(answer if answer else 'danger')
    except:
        break