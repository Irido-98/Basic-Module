import math


def factorial(n):
    value = float(1)
    for i in range(1, n + 1):
        value = value * i
    return value


def power(base, exponent):
    return base ** exponent


def sin(x):
    value = x
    sign = -1
    n = 200  # precision
    i = 3
    while i < n:
        value = value + (power(x, i) / factorial(i) * sign)
        i = i + 2
        sign = sign * -1
    return round(value, 5)


def cos(x):
    value = 1
    sign = -1
    n = 200  # precision
    i = 2
    while i < n:
        value = value + (power(x, i) / factorial(i) * sign)
        i = i + 2
        sign = sign * -1

    return round(value, 5)


def exp(x):
    value = 1
    n = 200  # precision
    i = 1
    while i < n:
        value = value + power(x, i) / factorial(i)
        i = i + 1

    return round(value, 5)


def tan(x):
    try:
        value = sin(x) / cos(x)
    except ZeroDivisionError:
        return 'Math Error'

    value = round(value, 5)
    if value == -0.0:
        value = 0.0
    return value


pi = math.pi
# print(sin(1.35))
# print(cos(pi))
#print(tan(pi / 2))
print(exp(1))
