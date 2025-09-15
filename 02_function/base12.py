import time


def decorator_func(func):
    def wrap():
        print("計測開始")
        start_time = time.time()
        func()
        func()
        func()
        end_time = time.time()
        print("計測終了")
        print(f"計測時間: {end_time - start_time:.6f}秒")

    return wrap


# a = decorator_func(print)
# a()
@decorator_func
def introduce():
    print("私は田中です。")


# introduce = decorator_func(introduce)
introduce()


def log_calls(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        result = func(*args, **kwargs)
        print(f"完了: {result}")
        return result

    return wrapper


@log_calls
def add(a, b):
    return a + b


print(add(2, 3))


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"{i + 1}回目")
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hello(name):
    print(f"こんにちは、{name}さん")


say_hello("太郎")
