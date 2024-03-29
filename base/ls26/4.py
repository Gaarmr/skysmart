import string


def count_of_words(text: str) -> dict:
    dct = {}
    text = text.translate(text.maketrans('', '', string.punctuation))
    text = text.lower()
    # print(text)
    for word in text.split():
        dct[word] = dct.get(word, 0) + 1
    return dct


print(count_of_words('''
    "Would you tell me, please, which way I ought to go from here?"
    "That depends a good deal on where you want to get to," said the Cat.
    "I don't much care where," said Alice.
    "Then it doesn't matter which way you go," said the Cat.
    "-so long as I get somewhere," Alice added as an explanation.
    "Oh, you're sure to do that," said the Cat, "if you only walk long enough."
'''))
