# 알파벳 -> 숫자 변환

convert_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

array = list(input())
array = list(map(lambda a : convert_list.index(a.upper()) + 1, array))

for num in array:
    print(num, end=' ')