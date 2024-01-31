def findSecondPlace(arr):
    # Ordenar la lista
    arr.sort()
    
    # Eliminar los repetidos
    filtered = []
    for x in arr:
        if x not in filtered:
            filtered.append(x)

    # Itero y encuentro el penultimo dato
    print(filtered[len(filtered) - 1 - 1])
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    findSecondPlace(arr)