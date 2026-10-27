# Given two numbers: a = 52698, b = 61430, compute great common divisor of a and b.

a = 52698
b = 61430

def gcd( a, b):
    if (a==0): return b
    return gcd(b%a, a)

c = gcd(a,b)

print(c)