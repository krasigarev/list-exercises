# bubble sort - https://www.programiz.com/dsa/bubble-sort
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data_list = list(map(int, input().split(" ")))

bubble_sort(data_list)
print(*data_list)
