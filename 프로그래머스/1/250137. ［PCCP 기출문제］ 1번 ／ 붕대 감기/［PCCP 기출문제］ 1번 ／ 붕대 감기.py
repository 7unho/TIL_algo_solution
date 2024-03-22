"""
t := 초 동안 붕대감기
x := 1초 회복량
y := t초간 붕대감기 성공시 추가 회복량

bandage := [붕대시전시간, x, y]
health := 최대체력
attacks := [공격 시간, 피해량]

answer = 체력, (-1)
"""
def solution(bandage, health, attacks):
    answer = health
    lastAttacked = 0
    for time, damage in attacks:        
        answer = doHeal(answer, time, bandage, lastAttacked, health)
        if isGameOver(answer, damage): return -1
        answer, lastAttacked = doAttack(answer, time, lastAttacked, damage)
    
    return answer if answer > 0 else -1

def isGameOver(health, damage) -> bool: # 현재 체력이 0 이하가 되었다면
    return health - damage <= 0

def doHeal(answer, time, bandage, lastAttacked, health):
    successTime = (time - 1) - lastAttacked
    return min(health, answer + (successTime // bandage[0]) * bandage[2] + successTime * bandage[1])

def doAttack(answer, time, lastAttacked, damage):
    answer -= damage
    lastAttacked = time
    return answer, lastAttacked