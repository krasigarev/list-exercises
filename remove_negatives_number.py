data_list = list(map(int, input().split(" ")))

positive_nums = list(filter(lambda x: x >= 0, data_list))
positive_nums.reverse()

print(positive_nums)