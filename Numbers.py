numbers = {1}
multipliers = [1]
lines = [[1]]
max_number = 10000000000000
print(1, 1, '...', '...', len(str(max_number)), max_number)

def add_new_line(prime):
    new_line = []
    k = 0
    skip = False
    while True:
        product = prime * multipliers[k]
        if product > max_number : break
        k += 1
        new_line.append(product)
        numbers.add(product)
        if product > max_number / prime:
            if skip:
                continue
            else:
                skip = True
        multipliers.append(product)
        multipliers.sort()

    lines.append(new_line)
    print(len(lines), new_line[0], len(new_line), len(numbers), len(multipliers), len(str(new_line[-1])), new_line[-1])
    return

for i in range(1, max_number + 1):
    if i in numbers: continue
    add_new_line(i)

print(len(numbers), len(lines))
for line in lines: print(line)