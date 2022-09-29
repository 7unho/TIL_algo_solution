x, y, w, h = map(int, input().split())

print(min([x, y, abs(w-x), abs(h-y)]))