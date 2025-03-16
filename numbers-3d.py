numbers = {1}
primes = []
max_number = int(1 * 10 ** 2)


def add_new_prime(new_prime):
    numbers.add(new_prime)
    primes.append([[new_prime]])
    for prime in primes:
        print(prime)
        for dim in prime:
            for d in dim:

                print(d)
                product = d * new_prime
                print(product, max_number)
                if product > max_number: break
                numbers.add(product)
                prime.append([product])


for i in range(1, max_number + 1):
    if i not in numbers:
        add_new_prime(i)

primes = tuple(primes)
for p in primes: print(p)
print('n', len(numbers), 'p', len(primes) - 1)
