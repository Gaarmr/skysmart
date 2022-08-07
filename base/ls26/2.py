def chars(s: str) -> dict:
    res = {}
    for i in s:
        res[i] = res.get(i, 0) + 1
    return res


print(chars('AAABBBCCC'))
