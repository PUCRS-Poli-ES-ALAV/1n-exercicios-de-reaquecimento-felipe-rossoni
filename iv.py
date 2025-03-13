x = input('Insira string: ')


def reversing_string(string):
    if (string == ""):
        return ""
    return reversing_string(string[1:]) + string[0]


str = reversing_string(x)
print(str)