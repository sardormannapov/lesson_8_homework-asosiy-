unique_sort = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]
result = []

def unique_sorted(number, rezultat):
    for num in number:
        if num not in rezultat:
            result.append(num)
            result.sort()

    print(rezultat)


unique_sorted(number=unique_sort, rezultat=result)