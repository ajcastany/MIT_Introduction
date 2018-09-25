"""
Finger Ex 5:
Ask for one int as input, and prints two numbers, root and pwr such that 0 < pwr < 6 and root**power = int.
"""
# x = int(input('Enter an int: '))
# pwr = 1
# root = 2
# result = 0

# while result < x:
#     while pwr < 6 and pwr > 0:
#         print('1', result)
#         result = root**pwr
#         if result == x or result > x:
#             print('break', result)
#             break
#         else:
#             pwr = pwr + 1
#     if result == x:
#         print('the root is', root, 'and the power is: ',pwr)
#         break
#     elif result > x:
#         print('There is no combination for that int')
#     else:
#         root = root + 1
# x = 25
# root = 1
# pwr = 1
# result = 0
# while result < x:
#     result = root ** pwr
#     while pwr < 6 and pwr > 0:
#         if result == x or result > x:
#             if result == x:
#                 print('result:', result)
#                 break
#             elif result > x:
#                 break
#         else:
#             pwr = pwr + 1
#             break
#     if result == x:
#         print('result is:', pwr, root)
#         break
#     elif result > x:
#         print('no combi for these')
#         break
#     root = root + 1


# x = 25
# root = 1
# pwr = 1
# result = 0

# while root < x:
#     result = root ** pwr
#     print(result, root, pwr)
#     if result == x:
#         print(root, pwr)
#         break
#     elif root < x:
#         root = root + 1
#         while pwr < 6 and pwr > 0:
#             if pwr == 6:
#                 pwr = 0
#             else:
#                 pwr = pwr + 1
#    # print('if', root, pwr)


root = 1
pwr = 1
result = 0

x = int(input('Enter an int: '))

while root != x:
    while pwr < 6 and pwr > 0:
        result = root ** pwr
        # print(result, root, pwr)
        if result == x:
            print('The number %d has %d root and %d power' % (x, root, pwr))
            break
    # elif root == (x - 1):
    #     print('The number %d has no combination of int root and pwr' % x)
    #     break
        else:
            pwr = pwr + 1
        # print(result, root, pwr)
    root = root + 1
    pwr = 1
    if root == x:
        print('The number %d has no combination of int root and pwr' % x)
        break
    elif result == x:
        break
# print(result, root, pwr)
