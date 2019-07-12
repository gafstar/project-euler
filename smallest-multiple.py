# 5. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#returns smallest multiples that is evenly divisible by all numbers from 1 to n and return -1 if multiple doesn't exist
def findSmallesMultiple(n):
    for i in range (n, factorial(n)+1, n):
        if isMultiple(i, n):
            return i
    return -1

#checks every number between 1 and n to see if x is a multiple of every number

def isMultiple(x, n):
    for i in range (1, n):
        if x %i != 0:
            return False
    return True

# returns the n factorial, or -1 if it doesn't exist

def factorial (n):
    if n > 1:
        return n*factorial(n-1)
    elif n >=0:
        return 1
    else: 
        return -1
    
print (findSmallesMultiple(10))
print (findSmallesMultiple(20))