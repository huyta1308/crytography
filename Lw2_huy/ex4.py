# Find multiplicative inverse of x = 65537 in the modulo N = 35256.

# def extended_gcd(a, b):
#     # Trả về (gcd, x, y) sao cho a*x + b*y = gcd
#     if a == 0:
#         return b, 0, 1
#     gcd, x1, y1 = extended_gcd(b % a, a)
    
#     # Cập nhật hệ số x và y
#     x = y1 - (b // a) * x1
#     y = x1
#     return gcd, x, y

# def mod_inverse(x, N):
#     gcd, x_inv, _ = extended_gcd(x, N)
#     if gcd != 1:
#         return "Không tồn tại nghịch đảo nhân (GCD != 1)"
#     else:
#         return x_inv % N  # Tính modulo để đảm bảo kết quả luôn dương

# x = 65537
# N = 35256
# inverse_algo = mod_inverse(x, N)
# print(f"Kết quả theo Thuật toán Euclid mở rộng: {inverse_algo}")

# # ---------------------------------------------------------
# # Cách 2: Sử dụng hàm pow() tích hợp sẵn (Hỗ trợ từ Python 3.8+)
# inverse_builtin = pow(x, -1, N)
# print(f"Kết quả dùng hàm pow() của Python: {inverse_builtin}")

x = 65537
N = 35256
for i in range(1,x):
    if (x*i)%N == 0:
        rs = i
        break
print(rs)
        