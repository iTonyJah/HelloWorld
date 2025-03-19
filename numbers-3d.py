numbers_set = {1}
# numbers_list = [prime_lines[prime_line_dimensions[values]]]
numbers_list = []
max_number = int(1 * 10 ** 2)


def add_new_prime(new_prime):
    numbers_set.add(new_prime)
    new_prime_line_dimension = [new_prime]
    new_prime_line = [new_prime_line_dimension]
    numbers_list.append(new_prime_line)
    print(numbers_list)

    for prime_line in numbers_list:
        print(prime_line)
        for pl_dim in prime_line:
            print('pl_dim', pl_dim)
            npl = []
            for i in pl_dim:
                print(pl_dim, i)
                product = i * new_prime
                if product > max_number: break
                print(product)
                numbers_set.add(product)
                npl.append(product)
                print('npl', npl)
            if npl: new_prime_line.append(npl)

    numbers_list.append(new_prime_line)
    print(numbers_set)


for n in range(1, max_number + 1):
    if n not in numbers_set:
        add_new_prime(n)

numbers_list = tuple(numbers_list)
print(numbers_list)
print('n', len(numbers_set), 'p', len(numbers_list))
