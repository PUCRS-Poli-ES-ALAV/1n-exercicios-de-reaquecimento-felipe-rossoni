def produto(x):
    r = 1
    for i in x:
        r *= i 
    return r

def soma(x):
    r = 0
    for i in x:
        r += i 
    return r

print(soma([1,2,3,4]))
print(produto([1,2,3,4]))