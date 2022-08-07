# def dna(s: str) -> bool:
#     for i in s:
#         if not (i == 'A' or i == 'T' or i == 'C' or i == 'G'):
#             return False
#     return True


def dna(s: str) -> bool:
    ln = len(s)
    a = s.count('A')
    t = s.count('T')
    c = s.count('C')
    g = s.count('G')
    if a+t+c+g == ln:
        return True
    else:
        return False


print(dna('AGCTTTTCATTCTGACTGCAACUGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
