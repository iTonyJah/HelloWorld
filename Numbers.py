numbers = {1}
lines = [[1]]
max_number = int(1 * 10 ** 2)
print(1, 1, '...', '...', '...', len(str(max_number)), max_number)

def add_new_line(prime):
    numbers.add(prime)
    new_line = [prime]
    lines.append(new_line)
    for line in lines:
        for number in line:
            product = prime * number
            if product > max_number or product in numbers : break
            new_line.append(product)
            numbers.add(product)
    print(new_line)
    print(lines[-1])
    new_line.sort()
    print(new_line)
    print(lines[-1])
    print(len(lines), new_line[0], len(new_line), len(numbers),
          str(int(len(numbers) / max_number * 100)) + '%', len(str(new_line[-1])), new_line[-1])

for i in range(1, max_number + 1):
    if i in numbers: continue
    add_new_line(i)

for l in lines: print(l)
print('n', len(numbers), 'p', len(lines))