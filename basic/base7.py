# 文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit *10
print(fruit_10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[-1])

# encode, decode => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))
