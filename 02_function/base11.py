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