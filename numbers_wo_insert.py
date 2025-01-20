numbers = {1}
lines = []
max_number = int(0.5 * 10 ** 1)

def fill_line(prime, line):
    for number in line:
        product = prime * number
        if product > max_number: break
        # if product in numbers: continue
        numbers.add(product)
        print(numbers)
        line.append(product)
    return line

def add_new_prime(prime):
    numbers.add(prime)
    print(numbers)
    self = fill_line(prime, [prime])
    new_line = [self]
    print('new_line_self', new_line)
    print('lines', lines)
    prev = []
    for prime_set in lines:
        print('prime_set', prime_set)
        for line in prime_set:
            print('prime, line', prime, line)
            pre = fill_line(prime, line)
            print('pre', pre)
            prev.append(pre)

    print('prev', prev)
    new_line += prev
    print('new_line+prev', new_line)

    self_prev = []
    for p in prev:
        self_prev.append(fill_line(prime, p))

    new_line += self_prev
    print('new_line+self_prev', new_line)

    lines.append(new_line)
    print('lines', lines)

for i in range(2, max_number + 1):
    if i not in numbers:
        print('i', i)
        add_new_prime(i)

lines = tuple(lines)
for pr in lines: print(pr)
print('n', len(numbers), 'p', len(lines))
