# insertion sort version 2

def insertion_sort(my_list):
    for i in range(len(my_list)):
        cur = my_list[i]
        j = i - 1

        while j >= 0 and cur < my_list[j]:
            my_list[j + 1] = my_list[j]
            my_list[j] = cur
            j = j - 1


def print_data_list(my_list):
    for i in my_list:
        print(i, end=" ")
    print("\n")


# test my code

my_list = list(map(int, input().split(" ")))
print(f"Original list: ")
print_data_list(my_list)

insertion_sort(my_list)
print("Sorted list: ")
print_data_list(my_list)

