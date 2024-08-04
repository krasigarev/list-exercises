data_list = list(map(int, input().split(" ")))

for index, value in enumerate(data_list):
    if index % 2 == 1 and value % 2 == 1:
        print(f"Index {index} -> {value}")

print(f"No index and value")