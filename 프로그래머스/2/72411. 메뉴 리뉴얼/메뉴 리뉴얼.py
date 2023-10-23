from itertools import combinations
from collections import defaultdict
"""
orders := 주문 내역
course := 코스요리 개수 배열
answer := 각 개수별 코스요리의 조합 오름차순
"""

def solution(orders, course):
    answer = list()
    
    for c in course:
        courses = defaultdict(int)
        for order in orders:
            if len(order) < c: continue
            menus = list(map(list, combinations(order, c)))
            
            for menu in menus:
                menu.sort()
                courses[f"{''.join(menu)}"] += 1
                
    
        for k, v in courses.items():
            if max(courses.values()) == v and v >= 2:
                answer.append(k)
                
    return sorted(answer)