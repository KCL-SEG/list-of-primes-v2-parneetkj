"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i = 0
    if number_of_primes <= 0:
        raise ValueError(f'Input={number_of_primes} should have been a positive number greater than 0')
    else:
        while(len(list) < number_of_primes):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    list.append(i)
            i += 1
    return list
