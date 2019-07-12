# 9. A Pythagorean triplet is a set of three natural numbers, a<b<ca<b<c, for which,

# a^2+b^2=c^2 a^2+b^2=c^2 For example, 3^2+4^2=9+16=25=5^2.

# There exists exactly one Pythagorean triplet for which a+b+c=1000.Find the product abc.
import time
start = time.time()

for num in range(1, 1000):
  for dig in range (num, 1000 - num):
    i = 1000 - num - dig
    if num * num + dig * dig == i * i:
      print (num, dig, i)
      print ("product: ")

elapsed = time.time() - start

print (f'Time: {elapsed}')