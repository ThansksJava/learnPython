def is_odd(n):
    return n % 2 == 1


print(filter(is_odd,[1,2,3,4,5,6,7]))
print(list(filter(is_odd,[1,2,3,4,5,6,7])))


print("==========is_palindrome===============")


def is_palindrome(n):
    int2str = str(n)
    return int2str == int2str[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
