def calculo(x, y, z, n):
    listX = [number for number in range(x + 1)]
    listY = [number for number in range(y + 1)]
    listZ = [number for number in range(z + 1)]

    result = [[x, y, z] for x in listX for y in listY for z in listZ if x + y + z != n]
    print(result)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    calculo(x, y, z, n)

# Falata terminar