from itertools import permutations
# 한자리 수의 조합을 활용해 소수 경우의 수 구하기

numbers = "17"
# numbers = "011"
temp = []
answer = set()

def solution(numbers):
    global answer
    numbers = list(numbers)

    subset(0)
    return len(answer)

def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0: return False
    return True

def subset(depth):
    global answer

    if depth >= len(numbers):
        arr = permutations(temp, len(temp))
        
        for item in arr:
            number = ''.join(item)
            if (number and int(number) >= 2) and isPrime(int(number)): 
                answer.add(int(number))
        return

    temp.append(numbers[depth])
    subset(depth + 1)
    temp.pop()
    subset(depth + 1)

print(solution(numbers))