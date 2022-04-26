class Animal:
    def __init__(self, name, age, breed):
        self.my_name = name
        self.my_age = age
        self.my_breed = breed
        print('Я родился.')

    def speak(self):
        print('Gav, my name is ', self.my_name)
    
    def introduce_youself(self):
        print(f'My name is {self.my_name}. Im a {self.my_age} years old. Im a {self.my_breed}')


class Cat(Animal):
    def meow(self):
        print(f'Meow. My name is {self.my_name}.')

class Dog(Animal):
    pass


cheshire = Cat('Cheshire', 4, 'Munchkin')
cheshire.meow()