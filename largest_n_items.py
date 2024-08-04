
def max_numbers(data_list, n):
    final_list = []

    for i in range(0, n):
        max_1 =  0

        for j in range(len(data_list)):
            if data_list[j] > max_1:
                max_1 = data_list[j]

        data_list.remove(max_1)
        final_list.append(max_1)

    print(*final_list)


data_list = list(map(int, input().split(" ")))
n = int(input())

max_numbers(data_list, n)