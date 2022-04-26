# def dna(s: str) -> str:
#     res = ''
    
#     for i in s:
#         if i == 'A':
#             res += 'T'
#         elif i == 'T':
#             res += 'A'
#         elif i == 'C':
#             res += 'G'
#         elif i == 'G':
#             res += 'C'
    
#     return res


# def dna(dna_string: str) -> str:
#     dct = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     return ''.join(map(dct.get, dna_string))


def dna(dna_string: str) -> str:
    dct = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    tbl = dna_string.maketrans(dct)
    print(tbl)
    return dna_string.translate(dna_string.maketrans(dct))


print(dna('ATCG'))



