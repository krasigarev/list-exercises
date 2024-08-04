data_list = list(map(int, input().split(" ")))

data_list.sort()
new_list = []

for el in data_list:
    new_list.append(el)

print(*new_list, sep=" <= ")
print(*new_list, sep="\n")
