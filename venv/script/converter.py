#
#Script dummy para covnertir binario a punto flotante
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
    return (result - 15)

def fraction():
    if(exponent() == 0):
        result = 0
    else:
        result = 1

    current2 = 1
    fracttion = numList[6:]
    for x in fracttion:
        if x == 1:
            result = result + 2**-current2
        current2 = current2 + 1
    return result


final = 2**exponent() * fraction()

if numList[0] == 1:
    print(final * -1)
else:
    print(final)
