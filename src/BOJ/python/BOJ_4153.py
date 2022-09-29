while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        test = [a, b, c]
        test.sort(reverse=True)

        if test[0]**2 == test[1]**2 + test[2]**2:
            print('right')
        else:
            print('wrong')