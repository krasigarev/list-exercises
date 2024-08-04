data_list = list(map(int, input().split(" ")))

result = []

for item in data_list:
    if item < 0:
        continue
    else:
        result.append(item)

result.reverse()

if len(result) == 0:
    print(f"empty")
else:
    print(*result)
