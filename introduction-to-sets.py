# Sets are used for membership testing and eliminating duplicate entries

def average(array):
    # eliminate duplicate entries
    withoutDuplicates = list(set(array))
    
    # clculate average
    return round(sum(withoutDuplicates) / len(withoutDuplicates), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) # => Linea muy importante
    result = average(arr)
    print(result)