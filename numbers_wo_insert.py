numbers = {1}
primes = []
max_number = int(1 * 10 ** 1)

def fill_line(prime, line):
    for number in line:
        product = prime * number
        if product > max_number: break
        if product in numbers: continue
        numbers.add(product)
        print(numbers)
        line.append(product)
    return line

def add_new_prime(prime):
    numbers.add(prime)
    self = fill_line(prime, [prime])

    prev = []
    print('primes', primes)
    for prime_set in primes:
        for line in prime_set:
            prev.append(fill_line(prime, line))

    print('prev', prev)
    prime_set = prev
    self_prev = []
    prime_set += self
    primes.append(prime_set)
    print(primes)

for i in range(2, max_number + 1):
    if i not in numbers:
        add_new_prime(i)

primes = tuple(primes)
for pr in primes: print(pr)
print('n', len(numbers), 'p', len(primes) - 1)
