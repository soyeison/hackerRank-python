def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n - 1)
    return resultado

def calculo(x, y, z, n):
    nFormula = x + y + z
    result = factorial(nFormula) / (factorial(x) * factorial(y) * factorial(z))
    listNumber = [x for x in range(nFormula)]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    calculo(x, y, z, n)

# Falata terminar