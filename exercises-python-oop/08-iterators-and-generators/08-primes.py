def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False

    return num not in (0, 1)


def get_primes(sequence):
    return (x for x in sequence if is_prime(x))
