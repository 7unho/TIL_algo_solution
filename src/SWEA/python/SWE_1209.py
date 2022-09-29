# Sum
## 100 * 100의 배열이 주어질 때,
## 각 행, 각 열, 각 대각선의 합중 최댓값을 구하는 프로그램

answer = 0

for tc in range(1, 11):
    t = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    cross_sum, rev_cross_sum = 0, 0
    rows_max, cols_max, cols_sum = 0, 0, 0

    for i in range(100):
        rows_max = max(rows_max, sum(graph[i]))
        cols_max = max(cols_max, cols_sum)
        cols_sum = 0
        cross_sum += graph[i][i]
        rev_cross_sum += graph[i][99 - i]

        for j in range(100):
            cols_sum += graph[j][i]
    
    print(rows_max, cols_max, rev_cross_sum, cross_sum)
    answer = max(cross_sum, rev_cross_sum, rows_max, cols_max)

    print(f"#{tc} {answer}")
