from animal import Animal


class Bird(Animal):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.value = "Bird"
        

    def type(self):
        return self.value


class Pigeon(Bird):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.value = "Pigeon"
        self.can_eat = ["litter"]

    def type(self):
        return self.value


class Penguin(Bird):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.value = "Penguin"
        self.can_eat = ["fish"]

    def type(self):
        return self.value
