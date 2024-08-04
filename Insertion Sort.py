#  Insertion Sort

# function for insertion sort
def insertionsort(data_list):
    for i in range(len(data_list)):
        curr = data_list[i]
        j = i - 1
        while j >= 0 and curr < data_list[j]:
            data_list[j + 1] = data_list[j]
            data_list[j] = curr
            j = j - 1


# function for pint list
def print_list(data_list):
    for i in data_list:
        print(i, end=" ")
    print("\n")


data_list = [1, 10, 23, 50, 4, 9, -4]
print("Original List")
print_list(data_list)

insertionsort(data_list)
print("Sorted List")
print_list(data_list)
