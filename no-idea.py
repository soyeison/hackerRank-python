if __name__ == '__main__':
    nm = list(map(int, input().split()))
    n = list(map(int, input().split()))
    a = list(set(list(map(int, input().split()))))
    b = list(set(list(map(int, input().split()))))

    # Iterar n 
    happiness =  0
    for i in n:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1

    print(happiness)