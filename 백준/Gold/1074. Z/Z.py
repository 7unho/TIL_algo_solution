def loop(sx, sy, ex, ey, r, c):
    global answer
    if sx == ex and sy == ey:
        if sx == r and sy == c:
            print(answer)
            exit(0)
        answer += 1
        return
    
    mid_x = (sx + ex) // 2
    mid_y = (sy + ey) // 2
    size = (mid_x - sx + 1) * (mid_y - sy + 1)
    
    # Z 순서대로 4분할 탐색
    if r <= mid_x and c <= mid_y:
        loop(sx, sy, mid_x, mid_y, r, c)
    elif r <= mid_x and c > mid_y:
        answer += size
        loop(sx, mid_y+1, mid_x, ey, r, c)
    elif r > mid_x and c <= mid_y:
        answer += size * 2
        loop(mid_x+1, sy, ex, mid_y, r, c)
    else:
        answer += size * 3
        loop(mid_x+1, mid_y+1, ex, ey, r, c)


n, r, c = map(int, input().split())
answer = 0
loop(0, 0, 2 ** n - 1, 2 ** n - 1, r, c)