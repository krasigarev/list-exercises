data_list = list(map(int, input().split(" ")))
n = int(input())


if all(x == n for x in data_list):
    print("yes")
else:
    print("no")
