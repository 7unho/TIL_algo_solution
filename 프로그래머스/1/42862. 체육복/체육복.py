"""
n := 전체 학생의 수
lost := [도난 당한 학생 번호...]
reserve := [여벌이 있는 학생 번호...]
answer := 체육 수업을 들을 수 있는 학생의 최댓값
student: [is]
"""
def solution(n, lost, reserve):
    answer = 0
    students = { i: [False, False] for i in range(1, n + 1)}
    
    for student in lost:
        students[student][0] = True
        
    for student in reserve:
        students[student][1] = True
    
    for student, [isLost, isReserved] in students.items():
        if not isLost:
            answer += 1
            continue
        
        if isReserved:
            answer += 1
            isReserved = False
            continue
        
        if canBorrow(students, student, student - 1):
            answer += 1
            continue
            
        if canBorrow(students, student, student + 1):
            answer += 1
            continue

            
    return answer

def canBorrow(students, student, render) -> bool:
    n = len(students)
    if render < 1 or render > n: return False
    if students[render][0]: return False
    if not students[render][1]: return False
    students[render][1] = False
        
    return True