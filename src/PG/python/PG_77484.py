# 로또의 최고 순위와 최저 순위

# def solution(lottos, win_nums):
#     zero_count, count = 0, 0
#     for num in lottos:
#         if num == 0:
#             zero_count += 1
#         elif num in win_nums:
#             win_nums.remove(num)
#             count += 1
    
#     max_rank = 7 - (zero_count + count) if 7 - (zero_count + count) < 7 else 6
#     min_rank = 7 - count if 7 - count < 7 else 6
#     answer = [max_rank, min_rank]
#     return answer


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0

    for x in win_nums:
        if x in lottos:
            ans += 1
    
    return rank[cnt_0 + ans], rank[ans]

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))
