# from typing import List


def excl(s: str):
    if s[-1] == '1':
        s = s[:-1] + '!'
        print(s)
    else:
        print(s)


excl(input())


# def func(n: int) -> List[int]:
#     return list(range(n))


# func(input())
