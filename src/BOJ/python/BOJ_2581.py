
import math

m = int(input())
n = int(input())
flag = True
result = []

for i in range(m, n + 1):
    if i <= 1 :
        flag = False
    else :
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                flag = False
                break

    if flag:
        result.append(i)

    flag = True

print(str(sum(result)) + '\n' + str(min(result)) if len(result) != 0 else '-1')
