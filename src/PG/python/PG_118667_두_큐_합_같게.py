# result 2
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

# # result 7
# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]

# # result -1
# queue1 = [1, 1]
# queue2 = [1, 5]

from collections import deque
    

def solution(queue1, queue2):
    deQueue1 = deque(queue1)
    deQueue2 = deque(queue2)
    sum1 = sum(deQueue1)
    sum2 = sum(deQueue2)


    for i in range(len(queue1) * 3):

        # 두 큐의 합이 같다면 i리턴
        if sum1 == sum2:
            return i
        
        # 큐1이 더 크다면, pop해주고 해당 값 큐2에 append
        ## sum1, sum2에 해당 숫자만큼 누적합
        if sum1 > sum2:
            temp = deQueue1.popleft()
            deQueue2.append(temp)

            sum1 -= temp
            sum2 += temp

        # 큐2가 더 클 때, 반대로
        else :
            temp = deQueue2.popleft()
            deQueue1.append(temp)

            sum1 += temp
            sum2 -= temp
    
    # for문을 다 돌았음에도 return 되지 않았다면
    # 경우의 수가 없으므로 -1 리턴
    return -1

print(solution(queue1, queue2))

