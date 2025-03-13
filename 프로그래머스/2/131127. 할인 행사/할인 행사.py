def solution(want, number, discount):
    answer = 0
    target = dict()
    window = dict()
    for i, product in enumerate(want):
        target[product] = number[i]
        window[product] = 0
        
    gap = sum(number)
    
    for i in range(gap):
        if discount[i] not in want: continue
        window[discount[i]] += 1
    
    if window == target: answer += 1
    
    for day in range(1, len(discount) - gap + 1):
        end = day + gap - 1
        
        if discount[day - 1] in want:
            window[discount[day - 1]] -= 1
        
        if end < len(discount) and discount[end] in want: 
            window[discount[end]] += 1
        
        if window == target: answer += 1
    
    return answer