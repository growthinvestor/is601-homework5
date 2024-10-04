from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def execute(self):
        return self.a + self.b

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def execute(self):
        return self.a - self.b
    
class ModulusCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a % self.b

class ExponentiateCommand(Command):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def execute(self):
        return self.base ** self.exponent