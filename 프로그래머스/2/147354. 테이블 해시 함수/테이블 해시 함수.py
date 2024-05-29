def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col - 1], -x[0]))
    sn = list()
    for row in range(row_begin - 1, row_end):
        # sn.append(data[row])
        sn.append(sum(map(lambda x: x % (row + 1), data[row])))
    
    answer = sn[0]
    for i in range(1, len(sn)):
        answer = answer ^ sn[i]
    return answer