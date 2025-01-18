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
    prime_line = [prime]
    print(type(prime_line), type(prime))
    prime_line = fill_line(prime, prime_line, prime_line)
    print(prime_line)
    lines.append(tuple(prime_line))

    new_line = [multiplier for line in lines for multiplier in line]
    print(new_line)
    lines.append(new_line)

    print(len(lines), new_line[0], len(new_line), len(numbers),
          str(int(len(numbers) / max_number * 100)) + '%',
          len(str(new_line[-1])), new_line[-1])

for i in range(2, max_number + 1):
    if i not in numbers:
        add_new_line(i)

lines = tuple(lines)
for l in lines: print(l)
print('n', len(numbers), 'p', len(lines) - 1)
