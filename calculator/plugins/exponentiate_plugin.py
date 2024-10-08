from calculator.commands import Command

class ExponentiateCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a ** self.b

def register():
    return ExponentiateCommand
