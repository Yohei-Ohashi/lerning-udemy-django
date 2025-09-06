# 辞書

car = {
    'brand': 'TOYOTA',
    'model': 'Prius',
    'year': 2050
}

print(car['brand']) # TOYOTA
# print(car['manufacturer']) # KeyError
brand = car.get('manufacturer', '不明') # エラーがない場合はNoneを返す
print(brand, type(brand))

car = dict(
    brand = 'SUZUKI',
    model = 'ジムニー',
    year = 2500
)
print(car, type(car))