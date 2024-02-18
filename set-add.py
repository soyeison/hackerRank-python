if __name__ == '__main__':
    n = int(input())

    respSet = set()
    # Create set empty
    for i in range(0, n):
        value = input()
        respSet.add(value)

    print(len(list(respSet)))