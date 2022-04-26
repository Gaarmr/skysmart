# def dna(s: str) -> dict:
#     res = {}
#     for i in s:
#         if res.get(i):
#             res[i] += 1
#         else:
#             res[i] = 1
#     return res



# print(dna('AATTCCGG'))



# def dna(s: str) -> dict:
#     res = {}
#     for i in s:
#         if i in res:
#             res[i] += 1
#         else:
#             res[i] = 1
#     return res



# print(dna('AATTCCGG'))


def dna(s:str): 
    a=s.count("A") 
    t=s.count("T") 
    c=s.count("C") 
    g=s.count("G") 
    return {"A":a,"T":t,"C":c,"G":g} 
    
print(dna("AAATCCCG"))