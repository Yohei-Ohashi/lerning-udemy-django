class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Swimmer:

    def swim(self):
        return f"{self.name} is swimming"

    def fly(self):
        return f"{self.name} don't flying"


class Flyer:
    def fly(self):
        return f"{self.name} is flying"

    def speak(self):
        return "speaking"


class Duck(Animal, Swimmer, Flyer):

    def speak(self):
        return f"{self.name} says quack!"


duck = Duck("Donald")
print(duck.speak())  # Donald says quack!
print(duck.swim())  # Donald is swimming
print(duck.fly())  # Donald is flying

print(Duck.__mro__)
"""
(
    <class '__main__.Duck'>,
    <class '__main__.Animal'>,
    <class '__main__.Swimmer'>,
    <class '__main__.Flyer'>,
    <class 'object'>
)
"""


class A:
    def mthod(self):
        return "A"


class B(A):
    def method_b(self):
        return "B"


class C(A):
    def method(self):
        return "C"


class D(B, C):
    pass


print(D.__mro__)
"""
(
    <class '__main__.D'>,
    <class '__main__.B'>,
    <class '__main__.C'>,
    <class '__main__.A'>,
    <class 'object'>
)
"""

d = D()
print(d.method())