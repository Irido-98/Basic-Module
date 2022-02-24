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


def tan(x):
    try:
        value = sin(x) / cos(x)
    except ZeroDivisionError:
        return 'Math Error'

    return round(value, 5)


def exp(x):
    value = 1
    n = 200  # precision
    i = 1
    while i < n:
        value = value + power(x, i) / factorial(i)
        i = i + 1

    return round(value, 5)


def natlog(x):
    try:
        value = math.log(x)
    except ValueError:
        return 'Math Error'
    return round(value, 5)


def base10log(x):
    try:
        value = math.log10(x)
    except ValueError:
        return 'Math Error'
    return round(value, 5)


def asin(x):
    try:
        value = math.asin(x)
    except ValueError:
        return 'Math Error'
    return round(value, 5)


def acos(x):
    try:
        value = math.acos(x)
    except ValueError:
        return 'Math Error'
    return round(value, 5)


def atan(x):
    try:
        value = math.atan(x)
    except ValueError:
        return 'Math Error'
    return round(value, 5)


pi = math.pi
print(asin(1))
print(acos(1))
print(atan(1))
print(tan(pi/2))
