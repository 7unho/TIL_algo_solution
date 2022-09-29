# # 함수와 람다식
# ## lambda expression 활용 시 간단한 함수를 한 줄에 작성 가능
# print('=' * 20 + "exam1" + '=' * 20)
# def add(a, b):
#     return print(f"{a} + {b} -> {a + b}")
#
# add(2, 3)
#
# print((lambda a, b : a + b)(3, 7))
#
# # Lambda expression example2
# print('=' * 20 + "exam2" + '=' * 20)
#
# arr = [('홍길동', 50), ('이순신', 32), ('아무개', 73)]
#
# def my_key(x):
#     return x[1]
#
# print(sorted(arr, key=my_key))
# print(sorted(arr, key=lambda x : x[1], reverse=True))
#
# # Lambda expression example3
# print('=' * 20 + "exam3" + '=' * 20)

list1 = [i for i in range(1, 6)]
list2 = [i for i in range(6, 11)]

result = map(lambda a, b : a + b if  0 else '-1', list1, list2)
print(list(result))