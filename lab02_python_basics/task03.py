list = list(map(int, input('Enter list of nums: ').split()))

sum_num = sum(list)
max_num = max(list)
sqr_list = []
for i in list:
    sqr_list.append(i**2)

print(f'sum={sum_num}, max={max_num}, squares={sqr_list}')