numbers_set = {1}
# numbers_list = [prime_lines[prime_line_dimensions[values]]]
numbers_list = []
max_number = int(1 * 10 ** 2)


def fill_prime_line(prime, prime_line):
    dim = 0
    for p_line in numbers_list:
        while dim < len(p_line):
            npl = []
            for i in p_line[dim]:
                product = i * prime
                print(product)
                if product > max_number: break
                numbers_set.add(product)
                npl.append(product)
                print(i, dim, product)

            prime_line.append(npl)
            dim += 1

    return prime_line


def add_new_prime(new_prime):
    numbers_set.add(new_prime)
    new_prime_line_dimension = [new_prime]
    new_prime_line = [new_prime_line_dimension]
    numbers_list.append(new_prime_line)
    print(numbers_list)

    npl = fill_prime_line(new_prime, new_prime_line)
    numbers_list.pop(-1)
    numbers_list.append(npl)

    print(numbers_list)


for n in range(1, max_number + 1):
    if n not in numbers_set:
        add_new_prime(n)

numbers_list = tuple(numbers_list)
print(numbers_list)
print('n', len(numbers_set), 'p', len(numbers_list))
