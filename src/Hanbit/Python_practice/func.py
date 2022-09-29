# global keyword

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# list는 global keyword 없이도 전역변수처럼 사용
array = [1, 2, 3, 4, 5]

def func2():
    array.append(2)
    print(f"func2 에서의 array : {array}")

def func3():
    array = [i for i in range(10) if i % 2 == 0]
    print(f"func3 에서의 array : {array}")

func2()
func3()

# python은 다수의 리턴값을 가질 수 있음
print('=' * 24 + '복수의 리턴 값' + '=' * 24)

def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(operator(7, 3))


