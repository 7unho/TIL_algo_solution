"""
ENTER -> uid 님이 들어왔습니다.
LEAVE -> uid 님이 나갔습니다.
CHANGE -> 
"""
from collections import defaultdict
def messageBuilder(uid, command) -> tuple:
    """
    cmd:Enter -> 님이 들어왔습니다.
    cmd:Leave -> 님이 나갔습니다.
    """
    message = '님이 들어왔습니다.' if command == "Enter" else '님이 나갔습니다.'
    return (uid, message)

def solution(record):
    answer = []
    userLastChangedNickName = defaultdict(str)
    rawMessages = []
    
    for r in record:
        row = r.split(" ")
        command, uid = row[0], row[1]
        
        if command == 'Leave':
            rawMessages.append(messageBuilder(uid, command))
            continue
        
        nickname = row[2]
        userLastChangedNickName[f"{uid}"] = nickname
        
        if command == 'Change': continue
        rawMessages.append(messageBuilder(uid, command))
    
    for uid, message in rawMessages:
        answer.append(
            userLastChangedNickName[f"{uid}"] + message
        )
        
    return answer