# タプル
fruits = ('apple', 'banana', 'lemon')

print(fruits, type(fruits), fruits[0])

# 要素の追加
fruits = fruits + ('grape',) # 一つの要素追加の時はカンマをつけるのが必須
print(fruits)

list_fruits = list(fruits)
print(list_fruits, type(list_fruits))

tupul_fruits = tuple(fruits)
print(tupul_fruits, type(tupul_fruits))

# タプルのメソッド

print(fruits.count('apple')) # appleの数
print(fruits.index('banana')) # bananaの最初のインデックス

coordinates = (135, 35)
# longtitude = coordinates[0] # 経度
# latitude = coordinates[1] # 緯度

# アンパック
longtitude, latitude = coordinates
print(longtitude, type(longtitude))
print(latitude, type(latitude))

# 辞書のキー
countries = {coordinates: 'Japan'}
print(countries.get((135, 35)))