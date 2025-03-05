def multiply(x, y):
    if x == 0:
        return 0
    return y + multiply(x - 1, y)

n1 = int(input('insira primeiro numero natural: '))
n2 = int(input('insira segundo numero natural: '))


print(multiply(n1, n2))