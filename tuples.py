if __name__ == '__main__':
    N = int(input())

    # Number in tuple
    numberString = list(input().split())
    listNumber = tuple([int(number) for number in numberString])

    # Generate Hash
    hashGenerated = hash(listNumber)

    print(hashGenerated)