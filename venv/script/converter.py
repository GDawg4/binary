#
#Script para covnertir binario a punto flotante
#Rodrigo Garoz
#

num = 1100101110
numList = list(map(int, str(num)))

def exponent():
    result = 0
    current = 0
    exponent = numList[1:6]
    exponent.reverse()

    for x in exponent:
        if x == 1:
            result = result + 2**current
        current = current + 1
    return result - 15

def fraction():
    result = 1
    current = 0
    fracttion = numList[6:]
    fracttion.reverse()
    for x in fracttion:
        if x == 1:
            result = result + 2**-current
        current = current + 1

    return result

final = exponent() * fraction()

if numList[0] == 1:
    print(final * -1)
else:
    print(final)
