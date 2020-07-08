from abc import ABC, abstractmethod


class Foo:
    def __init__(self, int1, int2):
        self.f = int1
        self.bar = int2

    def bar(self):
        print("did something!\n")
        return

    # private methods have two underscores

    def __priv(self):
        return


class FooBar(Foo):
    def __init__(self, i1, i2):
        # inherit from parent subclasses
        super().__init__(i1, i2)

# abstract method implementation
class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass


class Car(Vehicle):
    def engine(self):
        return True
