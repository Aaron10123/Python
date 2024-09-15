a = 10
print((lambda x: x + a)(10))

add_ten = lambda x: x + 10
print(add_ten(10))


def my_func(n):
    return lambda x: x + n


double_num = my_func(10)
triple_num = my_func(10)

print(double_num(10))
print(triple_num(10))
