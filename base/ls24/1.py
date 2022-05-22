def cg_composition(s: str) -> int:
    l = len(s)
    count_cg = s.count('C') + s.count('G')
    return count_cg / l * 100

print(cg_composition('ACCCCCCCCC'))
