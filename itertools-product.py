from itertools import product

if __name__ == '__main__':
    elementsA = list(input().split())
    elementsB = list(input().split())
    
    # Convertir los elementos en numeros
    elementsANumber = [int(i) for i in elementsA]
    elementsBNumber = [int(i) for i in elementsB]
    
    # Usar la herramienta itertool
    listResp = list(product(elementsANumber, elementsBNumber))
    print(listResp)

    # Iterar para imprimir la respuesta
    respString = ''
    for i in listResp:
        if respString == '':
            respString = str(i)
        else:
            respString = respString + ' ' + str(i)
    print(respString)