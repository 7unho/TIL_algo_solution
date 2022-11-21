for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    li = list(map(int, input().split()))

    # 최댓값은 모든 점원의 합이다
    answer = sum(li)

    def solution(depth, sum):
        global answer 

        # 백트래킹
        ## 이미 sum이 answer보다 크다면 return
        if sum > answer:
            return

        # 모든 부분집합 중에
        if depth == N:
            # sum이 B보다 큰 경우
            if sum >= B:
                # 최솟값 갱신
                answer = min(answer, sum)
            return

        solution(depth + 1, sum + li[depth])
        solution(depth + 1, sum)

    solution(0, 0)

    print(f"#{tc} {answer - B}")