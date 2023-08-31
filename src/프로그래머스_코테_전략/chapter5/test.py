arr = '123'
N = len(arr)
isSelected = [False] * (N + 1)
test = list()
def subset(depth):
    if(depth == 3):
        print(test)
        return
    
    
    test.append(arr[depth])
    subset(depth + 1)
    test.pop()
    subset(depth + 1)

subset(0)