import bisect
numbers = {1}
multipliers = [1]
lines = [[1]]
max_number = 10 ** 100
print(1, 1, '...', '...', '...', len(str(max_number)), max_number)

def add_new_line(prime):
    new_line = []
    k = 0
    skip = False
    print_empty_line = False
    while True:
        product = prime * multipliers[k]
        if product > max_number : break
        k += 1
        if k % 100000 == 0:
            print_empty_line = True
            print(k, end = ' ')
        new_line.append(product)
        numbers.add(product)
        if product > max_number / prime:
            if skip: continue
            else: skip = True
        multipliers.insert(bisect.bisect_left(multipliers, product), product)

    lines.append(new_line)
    if print_empty_line: print('')
    print(len(lines), new_line[0], len(new_line), len(numbers),
          str(int(len(numbers) / max_number)) + '%',
          len(multipliers), len(str(new_line[-1])), new_line[-1])


for i in range(1, max_number + 1):
    if i in numbers: continue
    add_new_line(i)

print(len(numbers), len(lines))
for line in lines: print(line)