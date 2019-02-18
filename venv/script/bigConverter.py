def exponent(numList):
    result = 0
    current = 0
    exponent = numList[1:9]
    exponent.reverse()

    for x in exponent:
        if x == 1:
            result = result + 2**current
        current = current + 1
    return (result - 127)

def fraction(numList):
    if exponent(numList) == -127:
        result = 0
    else:
        result = 1
    current2 = 1
    fracttion = numList[9:]
    for x in fracttion:
        if x == 1:
            print(current2)
            result = result + 2**-current2
        current2 = current2 + 1
    print(result)
    return result

def exponentToBinary(number):
    newNumber = int(number)
    binNumber = bin(newNumber)
    return binNumber[3:]

def floatingToBinary(number):
    newNumber = float(number)*-1
    binNumber2 = (newNumber - int(number)*-1)
    finalNumber = [0]

    while binNumber2 != 1.0 and binNumber2 != 0.0:
        binNumber2 = binNumber2 * 2
        binBit = int(binNumber2)
        print(binNumber2)
        if binBit == 1:
            binNumber2 = binNumber2 - 1
            finalNumber.append(1)
        else:
            finalNumber.append(0)
    del finalNumber[0]
    return finalNumber

def findTheOne(integer, float):
    for x in integer:
        if x == 1:
            return 7 - integer.index(x)

    for x in float:
        if x == 1:
            return -integer.index(x)


wantsToContinue = True
binToFloat = False

while wantsToContinue:
    binaryNum = input("Ingrese el número que desea imprimir")
    try:
        #binaryNum = int(binaryNum)
        binaryNum = 1101000001000000
        numList = list(map(int, str(binaryNum)))
    except:
        print("No es válido")
    else:
        if binToFloat:
            print("Válido")
            finalResult = 2**exponent(numList)*fraction(numList)
            if numList[0] == 1:
                print(finalResult*-1)
            else:
                print(finalResult)
        else:
            binList = list(map(int, str(exponentToBinary(-158.25))))
            floatList = floatingToBinary(-158.25)
            correction = findTheOne(binList, floatList)
            


