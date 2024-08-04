# insertion sort n the smallest numbers

def largest_bun(data_List):
    for i in range(len(data_List)):
        new = data_List[i]
        j = i - 1

        while j >= 0 and new < data_List[j]:
            data_List[j + 1] = data_List[j]
            data_List[j] = new
            j = j - 1


def print_list(data_list):
    for i in data_list:
        print(i, end=" ")
    print("\n")


data_list = list(map(int, input().split(" ")))
print(f"Original list: ")
print_list(data_list)

largest_bun(data_list)
print("Sorted list: ")
print_list(data_list)