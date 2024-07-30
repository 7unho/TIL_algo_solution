def solution(numbers, hand):
    answer = ''
    hand = 'R' if hand == 'right' else 'L'
    _hash = [hand, 'L', hand, 'R', 'L', hand, 'R', 'L', hand, 'R']
    address = [
        (3, 1),
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2)
    ]
    left, right = (3, 0), (3, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            answer += _hash[number]
            left = address[number]
            continue
        
        if number in [3, 6, 9]:
            answer += _hash[number]
            right = address[number]
            continue
        
        x, y = address[number]
        RDist = abs(right[0] - x) + abs(right[1] - y)
        LDist = abs(left[0] - x) + abs(left[1] - y)
        
        if RDist > LDist:
            answer += 'L'
            left = address[number]
        elif LDist > RDist:
            answer += 'R'
            right = address[number]
        else:
            answer += hand
            if hand == 'L':
                left = address[number]
                continue
            right = address[number]
        
    return answer