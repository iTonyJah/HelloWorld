numbers = {1}
lines = []
max_number = int(1 * 10 ** 2)

def fill_line(prime, line):
    self = True if line[0] == prime else False
    new_line = []
    print('prime, line, new_line', prime, line, new_line)
    for number in line:
        product = prime * number
        if product > max_number: break
        numbers.add(product)
        print(numbers)
        if self:
            line.append(product)
        else:
            new_line.append(product)
    return line if self else new_line

def add_new_prime(prime):
    numbers.add(prime)
    print(numbers)
    self = fill_line(prime, [prime])
    new_prime = [self]
    print('new_prime_self', new_prime)
    print('lines', lines)

    prev = []
    for prime_set in lines:
        print('prime_set', prime_set)
        for line in prime_set:
            print('prime, line', prime, line)
            pre = fill_line(prime, line)
            print('pre', pre)
            prev.append(pre)
            print('prev.append(pre)', prev)
            print('lines', lines)
    print('prev', prev)
    if prev:
        print('new_prime.append(prev)', prev)
        new_prime.append(prev)
    print('new_prime+prev', new_prime)

    self_prev = []
    for prev_line in prev:
        print('prev_line, prev for', prev_line, prev)
        self_prev_line = fill_line(prime, prev_line)
        if self_prev_line:
            self_prev.append(self_prev_line)

    if self_prev:
        new_prime.append(self_prev)
    print('new_prime+self_prev', new_prime)

    lines.append(new_prime)
    print('lines', lines)

for i in range(2, max_number + 1):
    if i not in numbers:
        print('i', i)
        add_new_prime(i)

lines = tuple(lines)
for pr in lines: print(pr)
print('n', len(numbers), 'p', len(lines))
