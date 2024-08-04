data_list = list(map(int, input().split(" ")))

data_square = []

for item in sorted(data_list):
    if int(pow(item, 0.5)) ** 2 == item:
        data_square.append(item)

data_square.reverse()

for el in data_square:
    print(abs(el), end=" ")

