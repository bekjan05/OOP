import functools

def check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, int):
                raise ValueError("Бир гана сан берилиш мүмкүн!!!")
        return func(*args, **kwargs)
    return wrapper

@check
def add(a, b):
    return a + b

@check
def sub(a, b):
    return a - b

@check
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError("0'гө бөлүнбөйт")

@check
def multiple(a, b):
    return a*b


def sum(x, n, y):
    result = None
    if n == "+":
        result = add(x, y)
    elif n == "-":
        result = sub(x, y)
    elif n == "/":
        result = divide(x, y)
    elif n == "*":
        result = multiple(x, y)
    else:
        raise ValueError("Түшүнбөдүм")
    return result

def calculator():
    a = int(input("бир сан:"))
    b = input("бироону танда:*,/,+,-:")
    c = int(input("бир сан:"))
    result = sum(a, b, c)
    print(result)

if __name__ == "__main__":
    calculator()

