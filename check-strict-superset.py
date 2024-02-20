if __name__ == '__main__':
    dataSetA = set(list(map(int, input().split())))
    otherSets = int(input())

    isSuperset = True
    for i in range(0, otherSets):
        dataThisSet = set(list(map(int, input().split())))

        if len(dataSetA) <= len(dataThisSet):
            isSuperset = False
        else:
            isSuperset = dataSetA.issuperset(dataThisSet)
            if not isSuperset:
                break
    
    print(isSuperset)