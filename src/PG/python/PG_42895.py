# # N으로 표현

# N = 4
# number = 31

# def solution(N, number):
#     if N == number:
#         return 1

#     dp = [[] for _ in range(9)]
#     dp[1] = [N]
#     answer = -1

#     for i in range(2, 9):
#         temp = set()
#         # N, NN, NNN
#         temp.add(int(str(N) * i))

#         for j in dp[i - 1]:
#             temp.add(j + N if 1 <= j + N <= 32000 else N)
#             temp.add(j - N if 1 <= j - N <= 32000 else N)
#             temp.add(j * N if 1 <= j * N <= 32000 else N)
#             temp.add(j / N if j != 0 and 1 <= j // N <= 32000 else N)
        
#         dp[i] = list(temp)
        
#         if number in dp[i]:
#             return i

#     return answer

# print(solution(N, number))


# N으로 표현
def solution(N, number):
    
    # N과 number가 같다면 바로 1 리턴
    if N == number:
        return 1

    dp = [[] for _ in range(9)]
    dp[1] = [N]
    answer = -1

    for i in range(2, 9):

        # N, NN, NNN
        dp[i].append(int(str(N) * i))
        
        # 가령 i = 3,
        #     j  = 1, 2
        for j in range(1, i):   
            
            # num1 == dp[1] ~ dp[2]
            for num1 in dp[j]:
                
                # num2 == dp[2] ~ dp[1]
                ## dp[2]와 dp[1]의 요소들을 연산 수행
                for num2 in dp[i - j]:
                    dp[i].append(num1 + num2)
                    dp[i].append(num1 - num2)
                    dp[i].append(num1 * num2)

                    if num2 != 0:
                        dp[i].append(num1 // num2)
        
        # 중복 제거
        dp[i] = list(set(dp[i]))
        
        if number in dp[i]:
            return i
            
    return answer



