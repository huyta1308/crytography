# Exercise 3

# Based on the provided description of the square- and-multiply algorithm, calculate exponentiation:

# x^2 mod m

# Compute:

# 856^25 mod 7

# Show the manual computation using the algorithm and compare it to returned results
# from your program.


#Manual computation
# 856 mod 7 = 2 = > Calculate 2^25 mod 7.
#25 is: 11001_2

# Bit 1: 1
#   Initial result (r) = 2

#  Bit 2: 1
#   Square : r = 2^2 mod 7 = 4
#   Multiply: r = (4 * 2) mod 7 = 8 mod 7 = 1

# Bit 3,4: 0
#   Square: r = 1^2 mod 7 = 1
#   (No multiplication because the bit is 0)

# Bit 5 (Rightmost): 1
#   Square : r = 1^2 mod 7 = 1
#   Multiply: r = (1 * 2) mod 7 = 2

#The final result from manual computation is: 2.




a = pow(856,25,7)

print("Cách 1 Rs:",a)



def mod_exp(base, expo, mod):
    x = base%mod
    bin_e_str = bin(expo)[2:]
    rs = x
    for i in bin_e_str[1:]:
        if int(i) == 1:
            rs = (rs**2)%mod
            rs = (rs*x)%mod
        else:
            rs = (rs**2)%mod
    return rs
print("Cách 2 Rs",mod_exp(856,25,7))    


