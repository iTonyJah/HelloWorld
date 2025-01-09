numbers = {1}
lines = [[1]]
max_number = int(1 * 10 ** 6)
print(1, 1, '...', '...', '...', len(str(max_number)), max_number)

def add_new_line(prime):
    new_line = []
    for line in lines:
        for number in line:
            product = prime * number
            if product > max_number:
                break

            numbers.add(product)
            new_line.append(product)
    new_line.sort()

    for number2 in new_line:
        product = prime * number2
        if product > max_number:
            break
        numbers.add(product)
        new_line.append(product)

    new_line.sort()
    lines.append(new_line)

    print(len(lines), new_line[0], len(new_line), len(numbers),
          str(int(len(numbers) / max_number * 100)) + '%', len(str(new_line[-1])), new_line[-1])

for i in range(1, max_number + 1):
    if i in numbers: continue
    add_new_line(i)

for l in lines: print(l)
print('n', len(numbers), 'p', len(lines))