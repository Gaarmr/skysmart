def dna(s: str) -> int:
    a = s.count('A')
    t = s.count('T')
    c = s.count('C')
    g = s.count('G')

    return a, t, c, g

print(dna('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))