def solution(people, limit):
    people.sort()
    
    start = 0    
    end = len(people) - 1
    answer = 0
    
    while True:
        if start >= end: break
        
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1
        end -= 1
            
    return len(people) - answer