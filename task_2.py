data_list = list(map(int, input().split(" ")))

min_number = min(data_list)

print(min_number)

# max value in list

max_val = data_list[0]

for el in range(len(data_list)):
    if data_list[el] >= max_val:
        max_val = data_list[el]

print(max_val)

# min value in list

min_val = data_list[0]

for el in range(len(data_list)):
    if data_list[el] <= min_val:
        min_val = data_list[el]

print(min_val)