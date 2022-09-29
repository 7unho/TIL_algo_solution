import sys

n = int(sys.stdin.readline())


boundary, result = 1, 1

while n > boundary:
    boundary += 6 * result
    result += 1

print(result)



# boundary = 1
# result = 0
#
# while True:
#     if n == 1 :
#         break
#
#     if boundary - 6 * result <= n - 1 < boundary:
#         break
#
#     result += 1
#     boundary += 6 * result
#
# print(result + 1)