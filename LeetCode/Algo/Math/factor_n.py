# Python program to print prime factors

import math
# A function to print all prime factors of
# a given number n

def primeFactors(n):
    array = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        array.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    # print(math.sqrt(n))
    
    for i in range(3,int(math.sqrt(n))+1,2):

    # while i divides n , print i and divide n
        while n % i== 0:
            array.append(i)
            n = n / i
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        array.append(n)

    return array
    

n = 7943
print(primeFactors(n))
