def getFinishedJobCount(job, remains) -> int:
    """
    현재 작업을 기준으로 배포될 작업의 개수 리턴
    """
    idx, cnt = len(remains), 1
    condition = remains[job]
    for i in range(job + 1, len(remains)):
        if condition < remains[i]: 
            idx = i
            break
        cnt += 1
        
    return (idx, cnt)
def getRemains(progresses, speeds) -> list:
    """
    return [각 작업의 소요 일 수]
    """
    
    res = list()

    for i, progress in enumerate(progresses):
        remain = (100 - progress) // speeds[i] if (100 - progress) % speeds[i] == 0 else ((100 - progress) // speeds[i]) + 1
        res.append(remain)
    
    return res
def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    remains = getRemains(progresses, speeds)
    pointer = 0
    
    while True:
        if pointer == N:
            break
        
        nJob, cnt = getFinishedJobCount(pointer, remains)
        print(nJob, cnt)
        answer.append(cnt)
        pointer = nJob
        
       
    return answer