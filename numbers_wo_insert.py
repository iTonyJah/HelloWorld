numbers = {1}
lines =[]
max_number = int(1 * 10 ** 2)

def fill_line(prime, line, new_line):
    for number in line:
        product = prime * number
        if product > max_number: break
        if product in numbers: continue
        numbers.add(product)
        new_line.append(product)
    return new_line

def add_new_line(prime):

    temp_line = [prime]
    temp_line = fill_line(prime, temp_line, temp_line)
    temp_lines = [temp_line]

    for temp_line in temp_lines:
        if len(temp_line) == 0: continue
        if temp_line[0] * prime > max_number : break
        new_line = []
        new_line = fill_line(prime, temp_line, new_line)
        temp_lines.append(new_line)
    print(temp_lines)
    new_line = [m for subarray in temp_lines for m in subarray]
    print(temp_lines)

    lines.append(tuple(new_line))
    print(len(lines), new_line[0], len(new_line), len(numbers),
          str(int(len(numbers) / max_number * 100)) + '%',
          len(str(new_line[-1])), new_line[-1])

for i in range(2, max_number + 1):
    if i not in numbers:
        add_new_line(i)

lines = tuple(lines)
for l in lines: print(l)
print('n', len(numbers), 'p', len(lines) - 1)
