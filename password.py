import string
from random import randint

# created the password object that adds the functionality of generating
# a weird but kinda good combination of password
# that will be a feature in the password manager that i am creating


class Password:
    def __init__(self):
        self.alphabet = string.ascii_letters
        self.collection = []
    
    def start(self):
        for item in self.alphabet:
            self.collection.append(item)
        for i in range(10):
            self.collection.append(str(i))

    def generate(self):
        self.start()
        _password_len = 12 # change base on how long you want your password
        _limit = len(self.collection) - 1
        created = "" # holds the created password combination
        for _ in range(_password_len):
            created += self.collection[randint(0,_limit)]
        return created


pas = Password()
