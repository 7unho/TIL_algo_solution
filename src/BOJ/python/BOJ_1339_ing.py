import sys
input = sys.stdin.readline

N = int(input())
numList = [str(i) for i in range(9, -1, -1)]
alphabets = []
arrays = []
answer = 0

for _ in range(N):
    array = input().rstrip()
    arrays.append(array)
    alphabets += array

arrays.sort(key=lambda x : len(x[0]), reverse=True)
print(arrays)


# alphabets = dict.fromkeys(alphabets)              

# i = 0
# for key in alphabets.keys():
#     alphabets[key] = numList[i]
#     i += 1
    

# for array in arrays:
#     for key, value in alphabets.items():
#         array = array.replace(key, value)
#     answer += int(array)

# print(answer)