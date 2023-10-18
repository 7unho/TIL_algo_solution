"""
우선순위
1. 가입자 최대
2. 판매액 최대

n := 사용자
M := 할인할 이모티콘 개수
users := [비율, 가격]
할인율 := 10~40%

이모티콘 구입 || 서비스 가입 기준
1. 각자의 기준에 따라, 일정 비율 이상 할인하는 이모티콘 모두 구매
2. 이모티콘 구매 비용의 합 >= 일정 가격 := 이모티콘 구매를 모두 취소하고, 서비스에 가입

res = [가입자 수, 매출액]
"""
answer = [0, 0]
def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    dcList = [0.1, 0.2, 0.3, 0.4]
    
    def process(case):
        cnt = 0    # 가입자 수
        sales = 0  # 매출액
        for dc, condition in users:
            sale = 0
            for i, c in enumerate(case):
                if dc > c * 100: continue
                
                sale += emoticons[i] * (1 - c)
                
            if sale >= condition:
                cnt +=1
                continue
            
            sales += sale
            
        return cnt, sales
    
    def makeCase(depth, case):
        global answer
        if depth == m:
            cnt, sales = process(case)
            
            if cnt > answer[0]: answer = [cnt, sales]
            elif cnt == answer[0] and sales > answer[1]: answer = [cnt, sales]

            return

        for dc in dcList:
            case.append(dc)
            makeCase(depth + 1, case)
            case.pop()
    
    makeCase(0, [])
    
    return answer

