if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    operationsNumber = int(input())

    # Solve the problem
    for i in range(0, operationsNumber):
        operationsName = input().split()
        if operationsName[0] == 'pop':
            s.pop()
        elif operationsName[0] == 'remove':
            s.remove(int(operationsName[1]))
        elif operationsName[0] == 'discard':
            s.discard(int(operationsName[1]))

    print(sum(list(s)))
