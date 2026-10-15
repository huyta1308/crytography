a = 123
b = 543



a_bin = bin(a)[2:]
b_bin = bin(b)[2:]

a_xor_b = bin(a^b)[2:]


print("binary of a: ", a_bin)
print("binary of aXORb: ", a_xor_b)
print("decimal of aXORb ", int(a_xor_b,2))
