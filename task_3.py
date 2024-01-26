number = [3, 3, 3, 2, 1]
result = []

def setify(num, rezultat):
    for numbr in num:
        if numbr not in rezultat:
            result.append(numbr)
            result.sort()
    print(rezultat)


setify(num=number, rezultat=result)