# # 최적의 행렬 곱셈
# def solution(sizes):
#     dp = [[0 for _ in range(len(sizes))] for _ in range(len(sizes))]

#     # gap = 
#     for gap in range(1, len(sizes)):
#         for s in range(len(sizes) - gap):
#             e = s + gap

#             temp = list()

#             for m in range(s, e):
#                 temp.append(dp[s][m] + dp[m + 1][e] + sizes[s][0] * sizes[m][1] * sizes[e][1])
            
#             dp[s][e] = min(temp)
    
#     return dp[0][-1]

# matrix_sizes = [[5, 3], [3, 10], [10, 6], [6,5]]
# print(solution(matrix_sizes))
from collections import deque

def solution(matrix_sizes):
    answer = 0
    sizes = deque([(matrix_sizes[i][1], i+1) for i in range(len(matrix_sizes))])
    sizes.pop()
    op_order = sorted(sizes,reverse = True)
    sizes.appendleft((matrix_sizes[0][0], 0))
    sizes.append((matrix_sizes[-1][1], len(sizes)))
    for i in range(len(op_order)):
        idx = op_order[i][1]
        left, right = idx-1, idx+1
        while True:
            if sizes[left][0] != 0:
                break
            left -= 1
        while True:
            if sizes[right][0] != 0:
                break
            right += 1
        answer += sizes[left][0]*sizes[idx][0]*sizes[right][0]
        sizes[idx] = (0,idx)

    return answer

print(solution([[5,3],[3,10],[10,6], [6,5]]))