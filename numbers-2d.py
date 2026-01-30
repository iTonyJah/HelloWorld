import bisect
numbers = {1}
lines = [(1,)]
max_number = int(1 * 10 ** 6)
print(1, 1, '...', '...', '...', len(str(max_number)), max_number)

def fill_line(prime, line, new_line, sort):
    for number in line:
        product = prime * number
        if product > max_number: break
        if product in numbers: continue
        numbers.add(product)
        if sort:
            bisect.insort_left(new_line, product)
        else:
            new_line.append(product)
    return new_line

def add_new_line(prime):
    new_line = []
    for line in lines:
        if line[0] * prime > max_number : break
        new_line = fill_line(prime, line, new_line, sort=False)
    new_line.sort()

    new_line = fill_line(prime, new_line, new_line, sort=True)
    lines.append(tuple(new_line))
    print(len(lines), new_line[0], len(new_line), len(numbers),
          str(int(len(numbers) / max_number * 100)) + '%',
          len(str(new_line[-1])), new_line[-1])

for i in range(1, max_number + 1):
    if i not in numbers:
        add_new_line(i)

lines = tuple(lines)
for l in lines: print(l)
print('n', len(numbers), 'p', len(lines) - 1)
