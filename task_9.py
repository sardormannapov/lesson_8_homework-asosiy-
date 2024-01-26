lst1 = [3, 2, 5]
lst2 = [5, 3, 7, 9, 2]
for num in lst1:
    if num in lst2:
        print(True)
        break
else:
    print(False)