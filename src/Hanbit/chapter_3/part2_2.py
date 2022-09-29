# n, m, k = map(int, input().split())
#
# result = 0
# cnt = k
#
# numList = [int(i) for i in input().split()]
# numList.sort(reverse=True)
#
# print(numList)
#
# for i in range(m):
#     print(result)
#     if cnt == 0:
#         result = result + numList[1]
#         cnt = k
#         continue
#
#     result = result + numList[0]
#     cnt = cnt - 1
#
# print(result)

# point = 반복되는 구조를 하나의 수열로 보기
n, m, k = map(int, input().split())

result = 0
numList = list(map(int, input().split()))
numList.sort()

first = numList[n-1]
second = numList[n-2]

first = first * k * int(m/(k+1))
first = first + first * int(m%(k+1))

second = int(m/(k+1)) * second

result = first + second
print(result)