numbers = [1]
lines = [[1]]
max_number = 1000000
print(1, '...', '...', len(str(max_number)), max_number)

def add_new_line(prime):
    new_line = []
    k = 0
    while k > -1:
        product = prime * numbers[k]
        if product > max_number : break
        new_line.append(product)
        numbers.append(product)
        numbers.sort()
        k += 1
    lines.append(new_line)
    print(new_line[0], len(new_line), len(numbers), len(str(new_line[-1])), new_line[-1])
    return

for i in range(1, max_number + 1):
    if i in numbers: continue
    add_new_line(i)

print(len(numbers), len(lines))
for line in lines: print(line)
