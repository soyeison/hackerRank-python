if __name__ == '__main__':
    T = int(input())
    for i in range(0,T):
        nSetA = int(input())
        dataSetA = set(list(map(int, input().split())))

        nSetB = int(input())
        dataSetB = set(list(map(int, input().split())))

        if dataSetB.intersection(dataSetA) == dataSetA and dataSetB.union(dataSetA) == dataSetB:
            print(True)
        else:
            print(False)