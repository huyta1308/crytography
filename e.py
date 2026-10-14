x = '1111101010101010101'
y = '1100110011001100110011'
z = '11100001111000011110000'

x = [int(i) for i in x]
y = [int(i) for i in y]
z = [int(i) for i in z]

print(len(x), len(y), len(z))

x_id = [13, 16, 17, 18]
y_id = [20, 21]
z_id = [20, 21, 22]

def new_x0(params, x_bits):
    x_r = x[x_id[0]]
    for i in x_id[1:]:
        x_r = x_r ^ x[i]
    return x_r

def new_y0(params, y_bits):
    y_r = y[y_id[0]]
    for i in y_id[1:]:
        y_r = y_r ^ y[i]
    return y_r

def new_z0(params, z_bits):
    z_r = z[z_id[0]]
    for i in z_id[1:]:
        z_r = z_r ^ z[i]
    return z_r

def majority(x_i, y_i, z_i):
    s = sum([x[x_i], y[y_i], z[z_i]])
    return 0 if s <= 1 else 1

def new_s0():
    return x[-1]^y[-1]^z[-1]

bit_generation = 100

for i in range(bit_generation):
    m = majority(8, 10, 10)
    s0 = new_s0()


    if m == x[8]:
        x0 = new_x0(x_id, x)
        x.pop()
        x = [x0] + x

    if m == y[10]:
        y0 = new_y0(y_id, y)
        y.pop()
        y = [y0] + y

    if m == z[10]:
        z0 = new_z0(z_id, z)
        z.pop()
        z = [z0] + z


    print(s0, end = '')