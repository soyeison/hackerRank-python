if __name__ == '__main__':
    nEnglish = int(input())
    nData = set(map(int, input().split()))
    bFrench = int(input())
    bData = set(map(int, input().split()))

    unionSet = nData.symmetric_difference(bData)

    print(len(list(unionSet)))
