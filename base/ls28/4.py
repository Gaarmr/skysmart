class Dog():
    def __init__(self, name, age, breed):
        self.my_name = name
        self.my_age = age
        self.my_breed = breed
        print('Гав. Я родился.')

    def speak(self):
        print('Gav, my name is ', self.my_name)

    def age(self):
        print('My age is ', self.my_age)

    def breed(self):
        print('My breed is ', self.my_breed)

    def introduce_youself(self):
        print(f'My name is {self.my_name} and I am a dog. Im a {self.my_age} years old. Im a {self.my_breed}')



sharik = Dog('Sharik', 3, 'mongrel dog')
belka = Dog('Strelka', 2, 'mongrel dog')
strelka = Dog('Belka', 2, 'mongrel dog')


sharik.speak()
belka.speak()
strelka.speak()

strelka.age()
strelka.breed()

strelka.introduce_youself()

