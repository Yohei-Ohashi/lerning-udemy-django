f = lambda x: x + 10
print(f(3))

f = lambda x, y: x * y
print(f(3, 5))

f = lambda x: "even"if x % 2 == 0 else "odd"
print(f(4))
print(f(5))

f = lambda x, y=2: x ** y
print(f(3))
print(f(3, 4))

f = lambda x, y: (x + y, x * y)
print(f(2, 4))

def process_list(numbers, func):
    for number in numbers:
        print(func(number))

numbers = list(range(5))
process_list(numbers, lambda x: x ** 2)