def process_user(name, age):
    def validate():
        if not name or not isinstance(age, int) or age < 0:
            raise ValueError("無効な入力です")

    validate()

    print(f"{name}({age})の処理を実行しました。")


# process_user("太郎", 25)
# process_user("", -1)


def make_multiplier(factor):
    def multiply(x):
        return x * factor

    return multiply


times3 = make_multiplier(3)  # multiply(x) return x * 3
print(times3(10))


def outer(y):
    x = 0

    def inner():
        # x = x + 1  外の変数を直接書き換えることはできない(エラーになる)
        nonlocal x  # 外の変数を書き換えるためにはnonlocalを使用する
        x = x + 1

        print(x, y)

    inner()


outer(12)
