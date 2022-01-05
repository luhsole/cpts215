
# MA 2: Primality Test
# Version: 1.0
# Date: September 12, 2021
#
# This program prompts user for an input and determines if the input is a prime number.

def is_prime(n):
    '''
    Determines if the number is a prime number
    :param n: integer >= 2 input by user
    :return: True/False of primality
    '''
    a = int(n ** 0.5)
    for m in range(2, a + 1):
        if n % m == 0:
            return False
    return True


def validity_test(n):
    '''
    Handles invalid and corner cases of n
    :param n: input by user
    :return: True/False of validity
    '''
    if n >= 2:
        return True
    else:
        return False


def sum_primes(n):
    '''
    Computes sum of prime numbers from 2 to n
    :param n: integer >= 2 input by user
    :return: sum of prime numbers
    '''
    sum = 0
    for m in range(2, n + 1):
        primality = True
        for l in range(2, m):
            if m % l == 0:
                primality = False
        if primality:
            sum += m
    return sum


def main():
    n = int(input("Please enter an integer >= 2: "))
    if validity_test(n):
        if is_prime(n):
            print(n, "is prime!")
        elif not is_prime(n):
            print(n, "is not prime!")
        print("Sum of primes from 2 to %s is %s!" % (n, sum_primes(n)))
    elif not validity_test(n):
        print("Input is not valid. Please enter an integer >= 2. ")


main()
