number = ["100101"]
result = []

def true_false(numbr, rezultat):
    for num in numbr:
        for num2 in num:
            if num2 == "1":
                result.append(True)
            else:
                result.append(False)
    print(rezultat)


true_false(numbr=number, rezultat=result)