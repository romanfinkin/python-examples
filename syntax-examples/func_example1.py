def foo(x, y):
    return x + y


def bar(x, y, z=1):
    return x * y * z


print(foo(2, 3))  # 2 + 3 = 5
print(bar(2, 3))  # 2 * 3 = 6
print(foo(bar(2, 3), 4))  # (2 * 3) + 4 = 10