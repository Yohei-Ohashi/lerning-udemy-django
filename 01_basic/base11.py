car = {
    'brand': 'TOYOTA',
    'model': 'Prius',
    'year': 2050
}

car['year'] = 2040
# car.get('year) = 2040 コレはできない
car['city'] = 'Toyota'
print(car)

# update
tmp_dict = {
    'country': 'Japan',
    'prefecture': 'Aichi',
    'city': 'Toyota city'
}
car.update(tmp_dict)
print(car)
# modelの内容を取得して、元の辞書から削除
value = car.pop('model')
print(car, value)

del car['city']
print(car)

# 中身を前削除
car.clear()
print(car)