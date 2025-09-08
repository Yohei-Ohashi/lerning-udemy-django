# ジェネレータ関数
from cgi import print_arguments


def generator():
    yield 1
    yield 2
    yield 3

gen = generator()  # ジェネレータオブジェクトを作成
print(type(gen))  # <class 'generator'>
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))  # StopIteration
for i in gen:
    print(i)

# ジェネレータ2
def print_num(max):
    print("ジェネレータ作成")
    for n in range(max):
        print(f"n: {n}")
        yield n

gen = print_num(10)
for i in gen:
    print(f"i: {i}")

# ジェネレータ3
import sys

N = 10 ** 6

def get_list():
    return [i for i in range(N)]

def get_generator():
    for i in range(N):
        yield i

lst = get_list()
print(sys.getsizeof(lst), "bytes")

gen_list = get_generator()
print(sys.getsizeof(gen_list), "bytes")