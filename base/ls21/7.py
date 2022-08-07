def twinkle_twinkle():
    print('''
            Twinkle, twinkle, little star,
            How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.

            When the blazing sun is gone,
            When he nothing shines upon,
            Then you show your little light,
            Twinkle, twinkle, all the night
        ''')


def repeat_twinkle(n=1):
    for i in range(n):
        twinkle_twinkle()


repeat_twinkle(2)
