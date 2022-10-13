points = list()
for tc in range(1, int(input()) + 1):
    N = int(input())

    for _ in range(N):
        x, y = map(int, input().split())
        points.append(abs(x) + abs(y))

    max_points = max(points)

    if max_points == 0:
        print(f"#{1} 0")
        continue

    isOdd = 1 if max_points % 2 == 1 else 0
    answer = 1
    while True:
        max_points -= answer
        print(max_points)
        if max_points <= 0:
            break
        answer += 1
    
    if max_points != 0:
        answer = answer + 2 if abs(max_points) % 2 == 1 else answer + 1
        
    print(f"#{tc} {answer}")
