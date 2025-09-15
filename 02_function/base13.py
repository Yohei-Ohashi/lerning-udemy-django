list_a = [1, 2, 3, 4, 5]

# map関数
map_a = map(lambda x: x * 2, list_a)

print(type(map_a))
print(list(map_a))

# ジェネレータ内包表記
list_b = (x * 2 for x in list_a)

print(list(list_b))


man = {"name": "Ichiro", "age": "18", "country": "Japan"}
map_man = map(lambda x: x + "," + man.get(x), man)
print(list(map_man))

map_man_b = (x + "," + man.get(x) for x in man)
print(list(map_man_b))


def calcurate(x, y, z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        return x / y


# print(calcurate(10, 20, "+"))
# print(calcurate(10, 20, "-"))
# print(calcurate(10, 20, "*"))
# print(calcurate(10, 20, "/"))

map_calcurate = map(calcurate, range(5), [3, 3, 3, 3, 3], ["+", "-", "*", "/", "+"])

print(list(map_calcurate))

map_calcurate_b = (
    calcurate(x, y, z)
    for x, y, z in zip(range(5), [3, 3, 3, 3, 3], ["+", "-", "*", "/", "+"])
)

print(list(map_calcurate_b))
