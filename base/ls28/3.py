class Cat():
    def __init__(self):
        print('Я родился')

    def speak(self, name):
        self.my_name = name
        print('Meow, my name is ', self.my_name)

    def introduce_youself(self):
        print('My name is ', self.my_name, ' and I am a cat')


murzik = Cat()
murzik.speak('Murzik')
