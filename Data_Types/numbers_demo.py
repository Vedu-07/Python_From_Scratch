import math
import random
from decimal import Decimal
x = 3
y = 2
z = 4

print((x+y)*z)

print(40+98.43)

result = 1 / 3.0

print(result)

print(repr('king')) # To provide a detailed, unambiguous string representation of an object, primarily for debugging and logging.
print(str('king')) # To provide a human-readable, "nicely printable" string representation of an object, intended for end-users.
print('king') # To display information to the standard output device (usually the console).

print(math.floor(3.5)) # takes below value
print(math.floor(-3.5))

print(math.trunc(4.56))
print(math.trunc(-4.56))

print(oct(64))
print(hex(64))
print(bin(64))

print(int('64',8))
print(int('64',16))
print(int('1000',2))

x = random.random()
y = random.randint(1,100)
print(x)
print(y)

dec = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(dec)

setone = {1,2,3,4}
print(setone | {1,3})