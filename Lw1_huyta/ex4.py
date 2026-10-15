X = 513365
Y = 3355443
Z = 7401712

x = bin(X)[2:].zfill(19)
y = bin(Y)[2:].zfill(22)
z = bin(Z)[2:].zfill(23)

x_arr =[]
y_arr=[]
z_arr=[]
for i in x:
    x_arr.append(int(i))
for i in y:
    y_arr.append(int(i))
for i in z:
    z_arr.append(int(i))

print("x: ", x_arr)
print("y: ", y_arr)
print("z: ", z_arr)

x_id = [13, 16, 17, 18]
y_id = [20, 21]
z_id = [7, 20, 21, 22]
ind_m = [8, 10, 10]

def ini_bits(index, arr):
    x_i = arr[index[0]]
    for i in index[1:]:
        x_i = x_i^arr[i]
    return x_i
print("X: ",ini_bits(x_id, x_arr))
print("Y ",ini_bits(y_id, y_arr))
print("Z ",ini_bits(z_id, z_arr))

def to_major(ind_m, x_arr, y_arr, z_arr):
    total = x_arr[ind_m[0]] + y_arr[ind_m[1]] + z_arr[ind_m[2]]
    if total >= 2: 
        return 1
    else: 
        return 0

print("major: ", to_major(ind_m, x_arr, y_arr, z_arr))

def compute_S( x, y, z):
    return x[-1]^y[-1]^z[-1]

def bit_gen(x, y, z, ind_m, length, x_id, y_id, z_id):
    s_arr = []
    for i in range(length):
        m = to_major(ind_m, x, y, z)
        
        s = compute_S(x, y, z)
        s_arr.append(s)
        if m == x[ind_m[0]]:
            x_ini = ini_bits(x_id, x)
            x.pop()                   
            x.insert(0, x_ini)        
            
        if m == y[ind_m[1]]:
            y_ini = ini_bits(y_id, y)
            y.pop()
            y.insert(0, y_ini)
            
        if m == z[ind_m[2]]:
            z_ini = ini_bits(z_id, z)
            z.pop()
            z.insert(0, z_ini)
            
        
    return s_arr
n = 10
keystream = bit_gen(x_arr, y_arr, z_arr, ind_m, n, x_id, y_id, z_id)

print("========RESULTS=========")
for key in keystream:
    print (key, end="")

        
