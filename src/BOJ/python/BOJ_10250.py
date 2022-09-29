import sys

testCnt = int(sys.stdin.readline())
room_list = []
for i in range(testCnt):
    h, w, n = map(int, sys.stdin.readline().split(' '))

    floor = n % h if n % h != 0 else h
    num = n // h + 1 if n % h != 0 else n // h
    num = f"0{num}" if num < 10 else num
    room_list.append(f"{floor}{num}")

for result in room_list:
    print(result)