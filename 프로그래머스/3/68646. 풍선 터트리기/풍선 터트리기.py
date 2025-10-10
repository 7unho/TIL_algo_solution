"""
각 풍선을 순회
해당 풍선을 살리려면, 마지막에 남은 풍선이 해당 풍선보다 작아야함.

작은 풍선을 터트리는건 한번만 가능.
"""

def solution(a):
    """
    [-5, -1, 9]
    [-92, -71, -68, -61, -33, -16, -2, 27, 58, 65]
    작은거 <> 나 <> 큰거
    작은거는 한번만 터트려, 큰거는 무제한
    
    좌, 큰 우 큰 무조건 true
    좌, 큰 우 작 true
    좌, 작 우 큰 true
    좌, 작 우 작 false
    """
    answer = len(a)
    n = len(a)
    left = [a[0]] * n
    right = [a[n - 1]] * n

    for i in range(1, n):
        left[i] = min(left[i - 1], a[i])
        right[n - 1 - i] = min(right[n - i], a[n - i])

    for i in range(1, n - 1):
        if a[i] > left[i] and a[i] > right[i]:
            answer -= 1
    
    return answer