# 연, 월, 일 달력

t = int(input())

answers = []

def check_YMD(y, m, d):
    d_list = [32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]

    if int(y) < 0:
        return False
    
    if int(m) not in range(1, 13):
        return False
    
    if int(d) not in range(1, d_list[int(m) - 1]):
        return False
    return True
for _ in range(t):
    array = input()
    y = array[:4]
    m = array[4:6]
    d = array[6:]

    if check_YMD(y, m, d):
        answer = '/'.join([y, m, d])
    else:
        answer = -1
    
    answers.append(answer)

for i in range(t):
    print(f"#{i + 1} {answers[i]}")