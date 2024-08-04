data_list = input().split("|")

result = []

for el in data_list:
    if el == " ":
        data_list.remove(el)
    else:
        result.append(el)

result.reverse()
print(*result)
