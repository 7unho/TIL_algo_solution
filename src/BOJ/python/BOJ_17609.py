# # 회문
# 입력값 : 문자열의 개수 T, 출력값 : 회문 -> 0, 유사 회문 -> 1, 나머지 -> 2

# from copy import deepcopy
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     answer = 2
#     arr = list(input().rstrip())
#     reverse_arr = deepcopy(arr[len(arr):((len(arr) - 1) // 2):-1])
    
#     if arr[:(len(arr) // 2)] == reverse_arr:
#         answer = 0
#         print(answer)
#         continue

#     for i in range(len(arr)):
#         arr_cp = deepcopy(arr)
#         del arr_cp[i]

#         reverse_arr = deepcopy(arr_cp[len(arr_cp):((len(arr_cp) - 1) // 2):-1])

#         if arr_cp[:(len(arr_cp) // 2)] == reverse_arr:
#             answer = 1
#             break

#     print(answer)

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    str = input().rstrip()
    answer = 2

    # 바로 회문이라면 0으로 할당 후 출력
    if str == str[::-1]:
        answer = 0
        print(answer)
        continue

    # 삭제할 문자가 왼쪽(before)에 있을지, 오른쪽(after)에 있을지 체크용 리스트 2개
    before = list(str)
    after = list(str)

    for i in range((len(str) - 1) // 2 + 1):
        # 문자가 하나라도 다르다면 회문이 아니므로
        if str[i] != str[-(i + 1)]:
            before.pop(i)
            after.pop(-(i + 1))

            if before == before[::-1] or after == after[::-1]:
                answer = 1
                break
    print(answer)
