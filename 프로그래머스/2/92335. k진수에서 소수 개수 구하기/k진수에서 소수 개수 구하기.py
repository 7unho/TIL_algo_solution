def solution(n, k):
    answer = 0
    items = list(map(lambda x: int(x) if x.isdigit() else 0, NtoKBase(n, k).split('0')))
    
    for item in items:
        if isPrime(item): answer += 1
    
    return answer

def NtoKBase(n, k):
    res = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        res += str(mod)
        
    return res[::-1]

def isPrime(n):
    # 소수 판별
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True