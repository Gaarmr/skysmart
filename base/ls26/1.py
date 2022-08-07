def chars(s: str) -> dict:
    res = {}
    for i in s:
        if res.get(i):
            res[i] += 1
        else:
            res[i] = 1
    return res


print(chars('Mad Hatter'))
