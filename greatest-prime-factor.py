# returns True if parameter n is a prime number, False if composite and "Neither prime, nor composite" if neither
def isPrime(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# returns smallest factor of parameter n
def findSmallestFactor(n, i):
    if n % i == 0: # found it
        return i
    elif i > n: # can't find it; something's wrong
        return -1 
    else: # keep trying
        return findSmallestFactor(n, i + 1)
                
def greatestPrimeFactor(n):

    # finding smallest factor increases performance IMMENSELY with numbers this large.
    # for smaller numbers, just use:
    # for i in range (int(n / 2), 1, -1):
    smallestFactor = findSmallestFactor(n, 2)
    for i in range (int(n / smallestFactor), 1, -1): # start with the largest factor and go down to 2

        if n % i == 0: # check if it's even a factor before checking if it's prime
            if isPrime(i): # THEN check if it's prime (better performance to do it now instead of before)
                return i
    return n # if it didn't already return something, there's nothing left to look for, so the number itself is prime

# This function skips a lot of numbers by dividing by potential factors into the original number;
# it starts at the smallest factor, and continues until the largest factor (number / smallest factor)
def greatestPrimeFactor2(n):
    
    smallestFactor = findSmallestFactor(n, 2)

    # this loops through the small factors first, but tests the large factors by dividing the number by the factors, i
    for i in range (smallestFactor, int(n / smallestFactor) + 1): # for the smallest factor to the largest factor (inclusive for both)
        
        if float(n)/i == int(n/i) and n % n/i == 0: # if it's an integer and the number is divisible by the corresponding factor
            if isPrime(n/i): # THEN check if it's prime (better performance to do it now instead of before)
                return n/i
            
    return n # if it didn't already return something, there's nothing left to look for, so the number itself is prime

print (greatestPrimeFactor(600851475143))
print (greatestPrimeFactor2(600851475143))