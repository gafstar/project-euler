# 10. The sum of the primes below 1010 is 2+3+5+7=172+3+5+7=17.

# Find the sum of all the primes below two million.

import time
start = time.time()

def isPrime(n):
    if n < 2: 
        return 'Neither prime nor composite'
    for i in range (2, int(n**0.5)+1):
        if n %i ==0:
            return False
    return True

def sum_primes_less_n(n):
    
  prime_total=0
#generates a list of numbers.
  for number in range(2, 101):
    if is_prime(number):
      prime_total += number
  print (prime_total)
  
sum_primes_less_n(20)

elapsed = time.time() - start

print (f'Time: {elapsed}')
