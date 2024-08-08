def solution(number, k):
    number = list(number)
    n = len(number)
    deleted = set()
    last = 0
    for i in range(1, n):
        if len(deleted) == k: break
        if number[i - 1] >= number[i]: continue
            
        for j in range(i - 1, -1, -1):
            if len(deleted) == k: break
            if number[j] >= number[i]: break
            deleted.add(j)

    for i in deleted:
        number[i] = ''
    
    number = list(''.join(number))
    
    k -= len(deleted)
    
    while True:
        if k == 0: break
        number.pop()
        k -= 1
    
    return ''.join(number)
