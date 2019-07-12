# 4. A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# determines whether or not an integer is a palindrom
def isPalindrome(n):
    s = str (n)
    reverseString= ""
    
    for i in range(len(s)-1, -1, -1):
        reverseString += s[i]
    return reverseString == s

#returns lagest palindrom that is a multiple of two 3 digit numbers
def findLargestPal():
    palindrome = -1
    
    for i in range (999, 99, -1):
        for j in range (i, 99, -1):
            
            #if product is palindrom and is greater than the last recorded palindrom
            if isPalindrome(i*j) and i*j> palindrome:
                palindrome = i* j
    return palindrome
print (findLargestPal())