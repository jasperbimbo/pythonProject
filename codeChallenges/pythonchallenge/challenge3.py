class Animal:
    sound = "Hiss"

    def get_sound(self):
        return self.sound


class Cat(Animal):
    sound = "Meow"
    pass


class Dog(Animal):
    sound = "Bark"
    pass


animal = Animal()
cat = Cat()
dog = Dog()
print("Animal Sound:", animal.get_sound())
print("Cat Sound:", cat.get_sound())
print("Dog Sound:", dog.get_sound())