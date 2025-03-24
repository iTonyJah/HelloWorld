numbers_set = {1}
numbers_list = []
primes = []
max_number = int(1 * 10 ** 3)


def add_new_prime(new_prime):
    numbers_set.add(new_prime)
    numbers_list.append([new_prime])
    primes.append(new_prime)

    max_k = 1
    for prime in primes:
        k = 1
        product = new_prime * prime ** k
        if product > max_number: break
        numbers_set.add(product)
        numbers_list[-1].append(product)
        while True:
            k += 1
            product = new_prime * prime ** k
            if product > max_number: break
            numbers_set.add(product)
            numbers_list[-1].append(product)
            max_k = max(max_k, k)


for n in range(1, max_number + 1):
    if n not in numbers_set:
        add_new_prime(n)

for nl in numbers_list:
    print(nl)
print('n', len(numbers_set), 'p', len(numbers_list))
