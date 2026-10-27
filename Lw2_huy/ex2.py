# Given a set of numbers
# A = {290345, 218585, 143231, 164172, 155768, 423151, 239707, 153544, 287390, 480837}
# find all pairs of number that are relatively prime to each other.

A = [290345, 218585, 143231, 164172, 155768, 423151, 239707, 153544, 287390, 480837]

def gcd( a, b):
    if (a==0): return b
    return gcd(b%a, a)

def relative_prime(A):
    result = []

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if gcd(A[i], A[j]) == 1:
                result.append((A[i], A[j]))

    return result

pairs = relative_prime(A)
print(pairs)





