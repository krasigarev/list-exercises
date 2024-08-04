number_list = list(map(int, input().split(" ")))

counter = 0

for num in number_list:
    if not num % 2 == 0:
        counter += 1

print(counter)

odd_list_num = len([element for element in number_list if element % 2 == 1])
print(odd_list_num)