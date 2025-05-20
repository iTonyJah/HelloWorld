numbers_set = {1}
numbers_list = []
max_number = int(1 * 10 ** 11)


def fill_prime_line(prime, prime_line):
    dim = 0
    while dim < len(prime_line):
        new = True
        for p_line in numbers_list:
            if dim >= len(p_line): break

            for value in p_line[dim]:
                product = value * prime
                if product > max_number: continue
                numbers_set.add(product)
                if new:
                    prime_line.append([])
                    new = False
                prime_line[dim + 1].append(product)
        dim += 1


def add_new_prime(new_prime):
    numbers_set.add(new_prime)
    new_prime_line_dimension = [new_prime]
    new_prime_line = [new_prime_line_dimension]
    numbers_list.append(new_prime_line)

    fill_prime_line(new_prime, new_prime_line)


for n in range(1, max_number + 1):
    if n not in numbers_set:
        print(n)
        add_new_prime(n)

numbers_list = tuple(numbers_list)
for nl in numbers_list:
    print(nl)
print('n', len(numbers_set), 'p', len(numbers_list))
