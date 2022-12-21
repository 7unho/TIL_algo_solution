import sys
input = sys.stdin.readline

# 입력값 : T(문자열의 개수)
# 출력값 : 회문이라면 0, 유사 회문(한 문자를 삭제하면 회문이 될 떄)이라면 1, 그 이외는 2

def solution(left, right):
    global case

    while left < right:
        if case[left] != case[right]: return False
        left += 1
        right -= 1

    return True

for _ in range(int(input())):
    case = list(input().rstrip())

    left = 0
    right = len(case) - 1
    answer = 0
    while left < right:
        # 두 문자가 같다면,
        if case[left] == case[right]:
            left += 1
            right -= 1
            continue

        # 두 문자가 다를 때,
        # 왼쪽에서 제거 한거, 혹은 오른쪽에서 제거했을 때 회문이라면,
        if solution(left + 1, right) or solution(left, right - 1):
            answer = 1
            break
        else :
            answer = 2
            break
    
    print(answer)
