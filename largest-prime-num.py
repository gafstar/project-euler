# 3. The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#return True if parameter n is a prime number, False if composit and neither if 'neither prime nor composite'
def isPrime(n):
    if n < 2: 
        return 'Neither prime nor composite'
    for i in range (2, int(n**0.5)+1):
        if n %i ==0:
            return False
    return True

# returns the smallest prime factor of parameter n
def findSmallestFactor(n, i):
    if not n % i:
        return i
    elif i > n:
        return -1
    else:
        return findSmallestFactor(n, i+1)
    
def greatestPrimeFactor(n):
    
    #finding smallest factor increases performance IMENSELY with numbers this large
    #for smaller number, just use:
    #for i in range (int (n/2), 1, -1)
    smallestFactor - findSmallestFactor(n, 2)
    for i in range (int(n/smallestFactor), 1, -1): # start with the largest factor and go down to 2
        
        if not n %i:
            if isPrime(i):
                return i
    return n

#This function skips a lot of numbers by dividing by potential factors into the original number; it starts at the 
#smallest