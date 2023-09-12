class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def info(self):
        return f"I am {self.name} and I am {self.age} years old."


class Dog(Animal):
    def make_sound(self):
        return "汪汪汪"


class Bird(Animal):
    def make_sound(self):
        return "啾啾啾"


class Cat(Animal):
    def make_sound(self):
        return "喵喵喵"


dog = Dog("大黄", 2)
print(dog.info())
print(dog.make_sound())

bird = Bird("条子", 34)
print(bird.info())
print(bird.make_sound())

cat = Cat("大橘", 1)
print(cat.info())
print(cat.make_sound())
