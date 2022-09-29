import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    input_data = input().split()

    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key = lambda student : student[1], reverse=True)

for student in array:
    print(student[0])