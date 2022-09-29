import math

#최소 공배수(LCM)을 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(a, b)) # 최대 공약수 (GCD) 계산
print(lcm(a, b))      # 최소 공배수 (LCM) 계산
