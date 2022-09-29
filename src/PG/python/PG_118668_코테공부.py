# result 15
# alp = 10
# cop = 10
# problems = [[10,15,2,1,2],[20,20,3,3,4]]

# ## result 13
alp = 0
cop = 0
problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]


def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for i in range(len(problems)):
        max_alp = max(max_alp, problems[i][0])
        max_cop = max(max_cop, problems[i][1])
    # max_alp,max_cop 가  초기값보다 낮을수도있으므로 세팅
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    dp = [[151] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 배열 범위벗어나지않게
            ## 알고력을 공부하는 경우
            if i + 1 <= max_alp:
                dp[i + 1][j] = min (dp[i + 1][j], dp[i][j] + 1)
            ## 코딩력을 공부하는 경우
            if j + 1 <= max_cop:
                dp[i][j + 1] = min (dp[i][j + 1], dp[i][j] + 1)

            # 모든문제 순회 하면서 
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 현재 i,j 로 풀수있다면
                ## i = 현재 알고력, j = 현재 코딩력
                if i >= alp_req and j >= cop_req:
                    # 풀어서 얻은 내 최종 알고,코딩력이 max_alp,max_cop 보다크면 그대로 max_alp,max_cop 에 저장 
                    next_alp, next_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    return dp[max_alp][max_cop]

print(solution(alp, cop, problems))