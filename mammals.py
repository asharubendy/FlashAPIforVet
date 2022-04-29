from animal import Animal


class Mammal(Animal):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.value = "Mammal"
        self.can_eat = [""]

    def type(self):
        return self.value


class Cat(Mammal):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.value = "Cat"
        self.can_eat = ["mice"]

    def type(self):
        return self.value


class Dog(Mammal):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.value = "Dog"
        self.can_eat = ["dog food"]

    def type(self):
        return self.value


class Bat(Mammal):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.value = "Bat"
        self.can_eat = ["flies"]

    def type(self):
        return self.value
