"""
fees := [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
records := ["시간 차량 IN/OUT"]
result := [차량 번호별 정산 금액( 번호 오름차순 )]

정산금
1. 누적 주차 시간 <= 기본 시간 : 기본 요금
2. 누적 주차 시간 > 기본 시간 : 기본 요금 + (단위 시간 * 단위 요금)

"""

def solution(fees, records):
    answer = []
    carInfo = dict()
    accounts = dict()
    
    # 1. 차량별 주차 정보 세팅
    for record in records:
        time, car, check = record.split(' ')
        if not carInfo.get(car):
            carInfo[car] = list()
            accounts[car] = 0
        carInfo[car].append((time, check))
    
    # 2. 누적 주차시간 계산
    for car, info in carInfo.items():
        stack = info[:]
        
        while stack:
            time, check = stack.pop()
            
            if check == 'IN':
                res = cal('23:59', time)
                accounts[car] += res
                continue
                
            inTime, inCheck = stack.pop()
            res = cal(time, inTime)
            accounts[car] += res
    
    # 3. 정산금 계산
    for car in sorted(accounts.keys()):
        parkingFee = calParkingFee(accounts[car], fees)
        answer.append(parkingFee)

    return answer

def cal(outTime, inTime) -> int:
    """
    출차 시간, 입차 시간을 입력 받아 주차 시간 리턴
    """
    oH, oM = map(int, outTime.split(':'))
    iH, iM = map(int, inTime.split(':'))
    
    return (oH - iH) * 60 + (oM - iM) if oM >= iM else (oH - iH - 1) * 60 + (60 + oM - iM)

def calParkingFee(parkingTime, fees) -> int:
    """
    fees := [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
    return 정산금
    
    정산금
    1. 누적 주차 시간 <= 기본 시간 : 기본 요금
    2. 누적 주차 시간 > 기본 시간 : 기본 요금 + (단위 시간 * 단위 요금)
    """
    defaultTime, defaultFee, timeUnit, feeUnit = fees
    res = defaultFee

    # 2. 기본 시간 초과
    if parkingTime > defaultTime:
        res += ((parkingTime - defaultTime) // timeUnit) * feeUnit if (parkingTime - defaultTime) % timeUnit == 0 else ((parkingTime - defaultTime) // timeUnit) * feeUnit + feeUnit
    return res