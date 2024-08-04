data_list = list(map(int, input().split(" ")))

result = min(data_list)
print(result)

min_element = data_list[0]

for i in range(len(data_list)):
    if data_list[i] < min_element:
        min_element = data_list[i]

print(min_element)
