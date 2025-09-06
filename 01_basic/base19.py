# enumerate, zip
fruits = ["grape", "pine", "apple"]
print(list(enumerate(fruits, 10)))

for index, fruit in enumerate(fruits):
    print(f"index: {index}")
    print(f"fruit: {fruit}")

class_a_members = ["Taro", "Hanako", "Jiro", "Yoshiko"]
class_b_members = ["Katsuo", "Wakame", "Shiro"]

# 複数ループ（小さい方に合わせてループ）
for a, b in zip(class_a_members, class_b_members):
    print(f"a: {a}, b: {b}")

# while
count = 0
while count < 10:
    print(count)
    count += 1  # インクリメント
