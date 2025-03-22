def intToTime(hours, minutes):
    return f"{hours if hours >= 10 else '0' + str(hours)}:{minutes if minutes >= 10 else '0' + str(minutes)}"

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort(reverse=True)
    available = list()
    for turn in range(n):
        hours = (turn * t) // 60 + 9
        minutes = (turn * t) % 60
        rmCnt = 0
        bus = intToTime(hours, minutes)
        for crew in timetable:
            if rmCnt == m: break
            if bus < crew: continue
            rmCnt += 1
        

        for _ in range(rmCnt):
            available.append(timetable.pop())
        
        if turn == n - 1 and rmCnt < m:
            print(bus, available, rmCnt, m)
            answer = bus
    
    if answer != '' or not available: return answer
    
    h, m = map(int, available[-1].split(":"))
    
    if m > 0:
        m -= 1
    else:
        h -= 1
        m = 59
    
    answer = intToTime(h, m)
    return answer