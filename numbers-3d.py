numbers_set = {1}
numbers_list = []
max_number = int(1 * 10 ** 6)
sort_count = 0

def fill_prime_line(prime, prime_line):
    global sort_count

    dim = 0
    while dim < len(prime_line):
        max_prod = 0
        sort = False
        new = True
        for p_line in numbers_list:
            if p_line[dim][0] * prime > max_number:
                break

            for value in p_line[dim]:
                product = value * prime
                if product > max_number:
                    break
                numbers_set.add(product)

                if new:
                    prime_line.append([])
                    new = False
                prime_line[dim + 1].append(product)

                if product < max_prod:
                    sort = True
                max_prod = max(product, max_prod)

        if sort:
            prime_line[dim + 1].sort()
            sort_count += 1
        dim += 1


def add_new_prime(new_prime):
    numbers_set.add(new_prime)
    new_prime_line_dimension = [new_prime]
    new_prime_line = [new_prime_line_dimension]
    numbers_list.append(new_prime_line)

    fill_prime_line(new_prime, new_prime_line)


for n in range(1, max_number + 1):
    if n not in numbers_set:
        print(len(numbers_list) + 1, n, len(numbers_set), sort_count)
        add_new_prime(n)


for number_line in numbers_list:
    print(number_line)
print('n', len(numbers_set), 'p', len(numbers_list), 'sorted', sort_count)
