def isFinished(arr, num):
    for a in arr:
        if num % a != 0: return False
    return True

def solution(arr):
    arr.sort()
    
    answer = arr[-1]
    while True:
        answer += arr[-1]
        if isFinished(arr, answer):
            break
            
    return answer