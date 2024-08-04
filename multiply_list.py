# multiply a list

data_list = list(map(int, input().split(" ")))
p = int(input())
result_list = []

for element in data_list:
    result_list.append(element * p)

print(result_list)
print(*result_list)

