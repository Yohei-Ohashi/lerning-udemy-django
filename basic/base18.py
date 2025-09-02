# for, range
for i in range(10):
    print(i)
    print("-" * 10)

for i in range(2, 20, 3):
    print(i)
    print("-" * 10)

list_a = [i for i in range(2, 30)]
print(list_a, type(list_a))

# 同じ処理を10回実行する。
# 変数の値は使わない場合は_で示す
for _ in range(10):
    print("A")

samples = ["A", "B", "C", "D"]

for sample in samples:
    print(sample)

human = {
    "name": "Taro",
    "age": 20,
    "gender": "man"
}

# key一覧
for key in human:
    print(key, human[key])

# value一覧
for value in human.values():
    print(value)

# (key, value)一覧
for key, value in human.items():
    print(key, value)