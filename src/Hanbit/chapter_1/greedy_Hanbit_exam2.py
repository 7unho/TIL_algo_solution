# 각 자리가 숫자( 0 ~ 9 )로 된 문자열 입력 ( data )
## 각 자리의 연산은 +, * 로만 이루어짐
## 연산이 끝난 후 최대값 산출

import sys

data = sys.stdin.readline().strip()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num

print(result)