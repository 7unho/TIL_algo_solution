"""
1. 한 번에 K칸 전진 -> K만큼 전력 소모
2. (현재까지 온 거리) * 2 위치로 순간이동 -> 전력소모 0

solution -> 반으로 줄이면서, 홀수일 경우 answer + 1
5000 -> 2500 -> 1250 -> (625) 
-> 624 -> 312 -> 156 -> 78 -> (39) 
-> 38 -> (19) 
-> 18 -> (9) 
-> 8 -> 4 -> 2 -> (1) 
-> 0
"""
def solution(n):
    answer = 0 if n % 2 == 0 else 1
    
    if n == 1: return 1
    
    sn = n if n % 2 == 0 else n - 1
    
    while True:
        if sn == 1: 
            answer += 1
            break
        
        if sn % 2 != 0:
            sn -= 1
            answer += 1
            continue
        
        sn //= 2
        
    return answer