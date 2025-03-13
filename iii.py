n = int(input('N: '))

def divide(n):
    if n == 1:    return 1
    return 1/n + divide(n-1)

print(divide(n))