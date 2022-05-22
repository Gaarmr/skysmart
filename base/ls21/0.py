def greet_people(*args):
    print(args)
    for name in args:
        print('Hello', name)

greet_people('Vasya', 'Petya', 'Sasha', 'Vasya')