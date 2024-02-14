from itertools import permutations

if __name__ == '__main__':
    params = list(input().split())
    
    # Convertir los elementos en numeros
    params[1] = int(params[1])

    # Permutaciones
    permuted = list(permutations(params[0], params[1]))
    permuted.sort()

    # Darle el formato
    for p in permuted:
        print(''.join(p))
    
    