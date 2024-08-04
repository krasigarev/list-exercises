data_list = input().split(" ")

data_new = data_list.pop()
data_list.insert(0, data_new)

print(*data_list)
