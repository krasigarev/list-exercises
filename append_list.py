data_list = list(map(str, input().split("|")))

result = []

for i in data_list:
    for val in data_list:
        result.append(val)

result.reverse()
print(result)