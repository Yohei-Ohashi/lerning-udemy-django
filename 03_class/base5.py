class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)
v4 = str(v3)
print(v4)

print(Vector.__name__)
print(v3.__class__.__name__)

class Person:
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"  # {self.name} -> str(self.name) -> 花子, {self.name!r} -> repr(self.name) -> "花子"
    
    def __str__(self):
        return f"{self.name}"
    

p = Person("花子")
print(p)  # strを呼ぶ。ない場合はreprを呼ぶ。
print(repr(p))  # Person(name=花子)
print(f"{p!r}")  # Person(name=花子)
print(str(p))  # 花子

val = eval(repr(p))  # eval(Person(name=花子))
print(val)