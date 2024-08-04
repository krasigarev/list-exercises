data_list = list(map(int, input().split(" ")))

# data_list.reverse()
#
# print(*data_list)

new_list = []

for el in data_list[::-1]:
    new_list.insert(0, el)

print(new_list)

data_new = [el for el in reversed(data_list)]

print(" ".join(map(str, data_new)))
