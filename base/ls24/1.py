def cg_composition(s: str) -> int:
    ln = len(s)
    count_cg = s.count('C') + s.count('G')
    return (count_cg * 100) / ln


print(cg_composition('AAACCCCCCC'))
