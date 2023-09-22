from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0

    start = 0    
    end = len(people) - 1
    while True:
        if not people: break
        _sum = people[start] + people[end] if start != end else people[start]
        
        if _sum <= limit:
            answer += 1
            if start == end:
                people.popleft()
            else:
                people.pop()
                people.popleft()
            
            start = 0
            end = len(people) - 1
            continue
            
        if _sum > limit:
            people.pop()
            answer += 1
            end -= 1
            continue
            
    return answer