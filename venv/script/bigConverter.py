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
    binNumber = binNumber[3:]
    while len(binNumber) < 8:
        binNumber = "0" + binNumber
    return binNumber

def floatingToBinary(number):
    newNumber = float(number)
    binNumber2 = (newNumber - int(number))
    finalNumber = [0]

    while (binNumber2 != 1.0 and binNumber2 != 0.0) and len(finalNumber) < 8:
        binNumber2 = binNumber2 * 2
        binBit = int(binNumber2)
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
            return len(integer) - 1 - integer.index(x)

    for x in float:
        if x == 1:
            return -(float.index(x))
def isValid(input):
    if input == "1" or input == "2":
        return True
    return False


wantsToContinue = True

while wantsToContinue:
    print("Ingrese 1 para convertir de binario a flotante")
    print("Ingrese 2 para convertir de flotante a binario")
    direction = input("Ingrese 3 para salir")

    if isValid(direction):
        try:
            binaryNum = input("Ingrese el número que desea convertir")
            if direction == 1:
                binaryNum = int(binaryNum)
                numList = list(map(int, str(binaryNum)))

            else:
                binaryNum = float(binaryNum)

        except ValueError:
            print("No es válido")
        else:
            if direction == 1:
                print("Válido")
                finalResult = 2**exponent(numList)*fraction(numList)
                if numList[0] == 1:
                    print(finalResult*-1)
                else:
                    print(finalResult)
            else:
                numToBinary = abs(binaryNum)

                integerToBinary = list(map(int, str(bin(int(abs(numToBinary))))[2:]))

                pointToBinary = floatingToBinary(numToBinary)

                correction = findTheOne(integerToBinary, pointToBinary)

                if correction != 0:
                    finalExponent = list(map(int, str(bin(correction + 127))[2:]))
                else:
                    finalExponent = list(map(int, str(bin(correction + 126))[2:]))

                finalFraction = integerToBinary + pointToBinary
                del finalFraction[0]

                if binaryNum < 0:
                    signPrefix = [1]
                    finalNumber = signPrefix + finalExponent + finalFraction
                else:
                    signPrefix = [0]
                    finalNumber = signPrefix + finalExponent + finalFraction

                while len(finalNumber) < 16:
                    finalNumber.append(0)

                print("Su resultado final es", finalNumber)
    elif direction == 3:
        wantsToContinue = False
    else:
        print("Ingreso no válido, favor intentar nuevamente")


