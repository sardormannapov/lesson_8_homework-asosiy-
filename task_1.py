lst = ["Adam", "Sarah", "Malcolm"]
lst.sort()
result = []

def first_index(msv, rezultat):
    for name in msv:
        result.append(name[0])
    print(rezultat)


first_index(msv=lst, rezultat=result)