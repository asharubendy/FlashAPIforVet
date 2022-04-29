from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age, colour):
        self.value = "Animal"
        self.can_eat = [""]
        self.name = name
        self.age = age
        self.colour = colour
        
    def sleep(self):
        pass

    def eat(self, animal):
        for prey in self.can_eat:
            if animal.value == prey:
                return True

        return False

    def type(self):
        return self.value

    
