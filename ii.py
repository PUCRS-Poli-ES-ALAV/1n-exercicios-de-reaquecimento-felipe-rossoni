n1 = int(input('input1: '))
n2 = int(input('input2: '))

def soma(x, y):
    if x == 0: return y
    return soma(x-1, y+1)

print(soma(n1,n2))