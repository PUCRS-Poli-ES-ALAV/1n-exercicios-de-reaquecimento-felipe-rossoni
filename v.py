def F(n):
    if n < 2: return n
    else: return 2*F(n-1) + 3 * F(n-2)

print(F(3))