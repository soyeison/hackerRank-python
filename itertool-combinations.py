from itertools import combinations

if __name__ == '__main__':
    params = list(input().split())
    
    # Convertir los elementos en numeros
    params[1] = int(params[1])

    # Ordenar la lista
    paramList = list(params[0])
    paramList.sort()

    # List of different elements
    for i in range(1, params[1] + 1):
        listaResp = list(combinations(paramList, i))
        listaResp.sort()
        for p in listaResp:
            print(''.join(p))
    
    
    