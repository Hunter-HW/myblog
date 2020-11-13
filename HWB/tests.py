from django.test import TestCase

# Create your tests here.
# def unique_list(l):
#     set_A = set(l)
#     list_A = list(set_A)
#     return list_A
#
# l = [1, 2, 2, 3]
# print(unique_list(l))

# str1 = ' '
# str2 = '*'
# for i in range(10):
#     print((9-i)*str1+(2*i-1)*str2)

# def compare_lists(x, y):
#     flag = True
#     for i in range(len(x)):
#         if x[i] != y[i]:
#             flag = False
#     return flag
#
# n1 = [20, 10, 30, 10, 20, 30]
# n2 = [30, 20, 10, 30, 20, 50]
# print(compare_lists(n1, n2))

# def log(func):
#     print('begin to run xxx')
#     return func
#
# @log
# def func_test():
#     pass
#
# if __name__=='main':
#     func_test()

def HalfSearch(OrdereList, key, right, left):
    left = OrdereList[0]
    right = OrdereList[len(OrdereList)-1]

    for i in range(len(OrdereList)):
        if key == OrdereList[int(right+left)/2 ]:
            print(int(int(right+left)/2))
            return int(right+left)
        elif key < OrdereList[int(int(right+left)/2 )]:
            right = OrdereList[int(int(right+left)/2) ]
        else:
            left = OrdereList[int(int(right+left)/2 )]

if __name__=='main':
    HalfSearch([1,2,3,4,5,6,7], 2)


