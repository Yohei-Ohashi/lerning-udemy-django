def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    # if n <= 1:
    #     return 1
    # else:
    #     return n * factorial(n - 1)


print(factorial(5))
print(factorial(4))


def fibonacci(n):
    first = 0
    second = 1
    for _ in range(n):
        first, second = second, first + second
    return first

    # if n < 2:
    #     return n
    # return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
