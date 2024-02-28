from collections import defaultdict

if __name__ == '__main__':
    nm = list(map(int, input().split()))
    d = defaultdict(list)

    for n in range(0, nm[0]):
        d['A'].append(input())


    for m in range(0, nm[1]):
        d['B'].append(input())

    # Comenzar a iterar el grupo B
    for i in range(0, len(d['B'])):
        result = []
        for j in range(0, len(d['A'])):
            if d['B'][i] == d['A'][j]:
                result.append(j + 1)
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(map(str, result)))