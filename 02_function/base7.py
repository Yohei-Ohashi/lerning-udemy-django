def sub_gen():
    yield "X"
    yield "Y"
    return "サブジェネレータの結果"

def main_gen():
    result = yield from sub_gen()
    print(f"サブジェネレータから受け取った値: {result}")
    yield result

g = main_gen()
print(next(g))  # X
print(next(g))  # Y
print(next(g))  # サブジェネレータの結果
print(next(g))  # StopIteration

