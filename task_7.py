lst = ["cat", "blue", "skt", "umbrells", "paddy"]
lst2 = ["cat", "blue", "sky", "umbrella", "paddy"]
result = []

for word in lst:
    for word2 in lst2:
        if word == word2:
            result.append("1")
            break
    else:
        result.append("-1")
print(result)