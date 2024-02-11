def executeOperations(lista):
    arrResp = []
    for i in range(0, len(lista)):
        method = lista[i][0]

        if method == 'append':
            arrResp.append(int(lista[i][1]))
        elif method == 'insert':
            arrResp.insert(int(lista[i][1]), int(lista[i][2]))
        elif method == 'print':
            print(arrResp)
        elif method == 'remove':
            arrResp.remove(int(lista[i][1]))
        elif method == 'sort':
            arrResp.sort()
        elif method == 'pop':
            arrResp.pop()
        elif method == 'reverse':
            arrResp.reverse()

if __name__ == '__main__':
    N = int(input())
    
    operations = []
    # Iterar el numero de operaciones
    for i in range(0, N):
        rule = input()
        operations.append(rule.split())

    executeOperations(operations)