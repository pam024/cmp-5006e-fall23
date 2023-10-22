import math

# Given values
p = 233
q = 349
e = 119

# Calculate n and φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Find the modular multiplicative inverse of e modulo φ(n)
d = pow(e, -1, phi_n)

print("Public Key (e, n):", e, n)
print("Private Key (d, n):", d, n)
