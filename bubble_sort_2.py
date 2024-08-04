# bubble sort with for loop

l = list(map(int, input().split(" ")))

for i in range(0, len(l) + 1):
    for j in range(0, len(l) - 1):
        if l[j] > l[j + 1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp

print(*l)


# bubble sort with while loop

def bubble(list_1):
    data_list = len(list_1) - 1
    sorted_1 = False

    while not sorted_1:
        sorted_1 = True
        for i in range(0, data_list):
            if list_1[i] > list_1[i + 1]:
                sorted_1 = False
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
    return list_1


print(bubble([5, 1, 9, 2, 8, 3, 7, 5]))

