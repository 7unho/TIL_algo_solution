def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(1, len(phone_book)):
        n = len(phone_book[i - 1])
        if phone_book[i - 1] != phone_book[i][:n]: continue
        answer = False; 
        break;
        
    return answer