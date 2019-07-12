# 2^15=32768 and the sum of its digits is 3+2+7+6+8=26.

# What is the sum of the digits of the number 21000?

num = 2**1000
result = 0

while num > 0:
  rem = num % 10
  result += rem
  num = int(num/10)
#return result

print (f'The sum of the digits of the number {num} is: ', result)