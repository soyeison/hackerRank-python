if __name__ == '__main__':
    lenA = int(input())
    setA = set(map(int, input().split()))
    numberOfSets = int(input())

    for i in range(0, numberOfSets):
        operation = input().split()
        operationsName = operation[0]
        anotherSetLength = int(operation[1])

        anotherSetData = set(map(int, input().split()))

        if operationsName == 'intersection_update':
            setA.intersection_update(anotherSetData)
        elif operationsName == 'update':
            setA.update(anotherSetData)
        elif operationsName == 'symmetric_difference_update':
            setA.symmetric_difference_update(anotherSetData)
        elif operationsName == 'difference_update':
            setA.difference_update(anotherSetData)

        
    print(sum(list(setA)))
