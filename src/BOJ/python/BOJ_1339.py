# 단어 수학
import sys
input = sys.stdin.readline

n = int(input())
array = [list(input().strip()) for _ in range(n)]
alpha_dict = dict()
alpha_list = list()

for i in range(n):
    for j in range(len(array[i])):
        if array[i][j] in alpha_dict:
            alpha_dict[array[i][j]] += 10 ** ((len(array[i]) - j) - 1)
        else:
            alpha_dict[array[i][j]] = 10 ** ((len(array[i]) - j) - 1)

for key, value in alpha_dict.items():
    alpha_list.append([key, value])

alpha_list.sort(key=lambda x : x[1], reverse=True)
answer = 0
pows = 9

for i in range(len(alpha_list)):
    answer += alpha_list[i][1] * pows
    pows -= 1

print(answer)


# # 단어 수학
# import sys
# input = sys.stdin.readline

# n = int(input())
# array = [list(input().strip()) for _ in range(n)]
# array.sort(key=lambda x : len(x), reverse=True)
# dict_list = []

# for i in range(1, n):
#     for j in range(len(array[0]) - len(array[i])):
#         array[i].insert(0, '0')


# for i in range(len(array[0])):
#     for j in range(n):
#         if array[j][i] != '0' and array[j][i] not in dict_list :
#             dict_list.append(array[j][i])

# for i in range(len(array)):
#     temp = ''.join(array[i])
#     idx = 9
#     for alphabet in dict_list:
#         temp = temp.replace(alphabet, str(idx))
#         idx -= 1
    
#     array[i] = temp

# array = [int(i) for i in array]
# print(sum(array))
