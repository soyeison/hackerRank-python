from collections import Counter

if __name__ == '__main__':
    numberOfShoes = int(input())
    shoesList = list(input().split())
    shoesListNumber = [int(i) for i in shoesList]
    numberOfCustomers = int(input())

    # Lista de ventas
    sales = []
    for i in range(0, numberOfCustomers):
        eachSale = list(input().split())
        eachSaleNumbers = [int(i) for i in eachSale]
        sales.append(eachSaleNumbers)

    # I need to know how many shoes there are of each size
    eachSize = Counter(shoesListNumber)

    # Begin to iterate the sales for to calculate the result
    result = 0
    for i in sales:
        # Search the size in the shoesListNumber
        if eachSize[i[0]] > 0:
            eachSize[i[0]] -= 1
            result += i[1]
    
    print(result)